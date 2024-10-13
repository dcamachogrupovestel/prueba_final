/**
 * A simple SQLite CLI for the sqlite3 module.
 *
 * Apart from using 'commander' for the command-line interface,
 * this module implements the REPL using the 'readline' module.
 */
const sqlite3 = require('sqlite3').verbose();
const readline = require('readline');
const { Command } = require('commander');
const process = require('process');

function execute(db, sql, suppressErrors = true) {
    /**
     * Helper that wraps execution of SQL code.
     *
     * This is used both by the REPL and by direct execution from the CLI.
     *
     * 'db' is the database connection.
     * 'sql' is the SQL string to execute.
     */
    db.all(sql, [], (err, rows) => {
        if (err) {
            console.error(`${err.name}: ${err.message}`);
            if (!suppressErrors) {
                process.exit(1);
            }
        } else {
            rows.forEach((row) => {
                console.log(row);
            });
        }
    });
}

class SqliteInteractiveConsole {
    /**
     * A simple SQLite REPL.
     */
    constructor(db) {
        this.db = db;
        this.rl = readline.createInterface({
            input: process.stdin,
            output: process.stdout,
            prompt: 'sqlite> '
        });
    }

    start() {
        this.rl.prompt();
        this.rl.on('line', (line) => {
            this.runsource(line.trim());
            this.rl.prompt();
        }).on('close', () => {
            console.log('Exiting REPL.');
            process.exit(0);
        });
    }

    runsource(source) {
        /**
         * Handle the input source.
         *
         * Return true if more input is needed; buffering is done automatically.
         * Return false if input is a complete statement ready for execution.
         */
        switch (source) {
            case '.version':
                console.log(sqlite3.VERSION);
                break;
            case '.help':
                console.log('Enter SQL code and press enter.');
                break;
            case '.quit':
                process.exit(0);
                break;
            default:
                if (!source.endsWith(';')) {
                    return true;
                }
                execute(this.db, source);
        }
        return false;
    }
}

function main() {
    const program = new Command();
    program
        .name('sqlite3-cli')
        .description('Node.js sqlite3 CLI')
        .version(sqlite3.VERSION);

    program
        .argument('[filename]', 'SQLite database to open (defaults to ":memory:")', ':memory:')
        .argument('[sql]', 'An SQL query to execute. Any returned rows are printed to stdout.')
        .parse(process.argv);

    const options = program.opts();
    const [filename, sql] = program.args;

    const db = new sqlite3.Database(filename, (err) => {
        if (err) {
            console.error(err.message);
            process.exit(1);
        }
    });

    if (filename === ':memory:') {
        db_name = 'a transient in-memory database';
    } else {
        db_name = filename;
    }

    const banner = `
        sqlite3 shell, running on SQLite version ${sqlite3.VERSION}
        Connected to ${db_name}

        Each command will be run using execute() on the cursor.
        Type ".help" for more information; type ".quit" to quit.
    `.trim();

    console.log(banner);

    if (sql) {
        // SQL statement provided on the command-line; execute it directly.
        execute(db, sql, false);
    } else {
        // No SQL provided; start the REPL.
        const console = new SqliteInteractiveConsole(db);
        console.start();
    }
}

if (require.main === module) {
    main();
}