# Crear una clase persona que tenga como atributos nombre, edad y pais de origen.
# Crear un metodo que imprima el nombre de la persona
# Crear un metodo que imprima la edad de la persona
# Crear un metodo que imprima el pais de origen de la persona
# Crear un metodo que imprima todos los atributos de la persona
 # Crear una instancia de la clase persona 
# Imprimir todos los atributos de la persona

class Persona:
    def __init__(self, nombre, edad, pais):
        self.nombre = nombre
        self.edad = edad
        self.pais = pais

    def imprimir_nombre(self):
        print(self.nombre)

    def imprimir_edad(self):
        print(self.edad)

    def imprimir_pais(self):
        print(self.pais)

    def imprimir_atributos(self):
        print(f'Nombre: {self.nombre}')
        print(f'Edad: {self.edad}')
        print(f'Pais: {self.pais}') 

persona1 = Persona('Juan', 25, 'Colombia')
persona1.imprimir_atributos()

#crear una clase llamada estudiante que herede de la clase persona
#crear un metodo que imprima el nombre del estudiante
#crear un metodo que imprima la edad del estudiante
#crear un metodo que imprima el pais de origen del estudiante
#crear un metodo que imprima todos los datos del estudiante
#crear una instancia de la clase estudiante
#imprimir todos los atributos del estudiante

class Estudiante(Persona):
    def __init__(self, nombre, edad, pais):
        super().__init__(nombre, edad, pais)

    def imprimir_atributos(self):
        super().imprimir_atributos()
    
estudiante1 = Estudiante('Maria', 20, 'Colombia')
estudiante1.imprimir_atributos()

#crear una clase llamada profesor que herede de la clase persona
#crear un metodo que imprima el nombre del profesor
#crear un metodo que imprima la edad del profesor
#crear un metodo que imprima el pais de origen del profesor
#crear un metodo que imprima todos los datos del profesor
#crear una instancia de la clase profesor
#imprimir todos los atributos del profesor

class Profesor(Persona):
    def __init__(self, nombre, edad, pais):
        super().__init__(nombre, edad, pais)

    def imprimir_atributos(self):
        super().imprimir_atributos()    
    
profesor1 = Profesor('Pedro', 30, 'Colombia')
profesor1.imprimir_atributos()

#crear una clase llamada curso
#crear un metodo que imprima el nombre del curso
#crear un metodo que imprima la duracion del curso
#crear una instancia de la clase curso

class Curso:
    def __init__(self, nombre, duracion):
        self.nombre = nombre
        self.duracion = duracion

    def imprimir_nombre(self):
        print(self.nombre)

    def imprimir_duracion(self):
        print(self.duracion)
    
curso1 = Curso('Python', '3 meses')
curso1.imprimir_nombre()
curso1.imprimir_duracion()

#crear una clase llamada materia
#crear un metodo que imprima el nombre de la materia
#crear un metodo que imprima el curso de la materia
#crear un metodo que imprima el profesor de la materia
#crear un metodo que imprima los estudiantes de la materia
#crear una instancia de la clase materia

class Materia:
    def __init__(self, nombre, curso, profesor, estudiantes):
        self.nombre = nombre
        self.curso = curso
        self.profesor = profesor
        self.estudiantes = estudiantes

    def imprimir_nombre(self):
        print(self.nombre)

    def imprimir_curso(self):
        print(self.curso)

    def imprimir_profesor(self):
        print(self.profesor)

    def imprimir_estudiantes(self):
        print(self.estudiantes)

materia1 = Materia('Matematicas', 'Python', 'Pedro', ['Maria', 'Juan'])
materia1.imprimir_nombre()
materia1.imprimir_curso()
materia1.imprimir_profesor()
materia1.imprimir_estudiantes()

#crear una clase llamada grupo
#crear un metodo que imprima el nombre del grupo
#crear un metodo que imprima el curso del grupo
#crear un metodo que imprima el profesor del grupo
#crear un metodo que imprima los estudiantes del grupo
#crear una instancia de la clase grupo

class Grupo:
    def __init__(self, nombre, curso, profesor, estudiantes):
        self.nombre = nombre
        self.curso = curso
        self.profesor = profesor
        self.estudiantes = estudiantes

    def imprimir_nombre(self):
        print(self.nombre)

    def imprimir_curso(self):
        print(self.curso)

    def imprimir_profesor(self):
        print(self.profesor)

    def imprimir_estudiantes(self):
        print(self.estudiantes)

grupo1 = Grupo('Grupo 1', 'Python', 'Pedro', ['Maria', 'Juan'])
grupo1.imprimir_nombre()
grupo1.imprimir_curso()
grupo1.imprimir_profesor()
grupo1.imprimir_estudiantes()

#crear una clase llamada salon
#crear un metodo que imprima el nombre del salon
#crear un metodo que imprima el grupo del salon
#crear un metodo que imprima el curso del salon
#crear un metodo que imprima el profesor del salon
#crear un metodo que imprima los estudiantes del salon
#crear una instancia de la clase salon

class Salon:
    def __init__(self, nombre, grupo, curso, profesor, estudiantes):
        self.nombre = nombre
        self.grupo = grupo
        self.curso = curso
        self.profesor = profesor
        self.estudiantes = estudiantes

    def imprimir_nombre(self):
        print(self.nombre)

    def imprimir_grupo(self):
        print(self.grupo)

    def imprimir_curso(self):
        print(self.curso)

    def imprimir_profesor(self):
        print(self.profesor)

    def imprimir_estudiantes(self):
        print(self.estudiantes)

salon1 = Salon('Salon 1', 'Grupo 1', 'Python', 'Pedro', ['Maria', 'Juan'])
salon1.imprimir_nombre()
salon1.imprimir_grupo()
salon1.imprimir_curso()
salon1.imprimir_profesor()
salon1.imprimir_estudiantes()

#crear una clase llamada escuela
#crear un metodo que imprima el nombre de la escuela
#crear un metodo que imprima el salon de la escuela
#crear un metodo que imprima el grupo de la escuela
#crear un metodo que imprima el curso de la escuela
#crear un metodo que imprima el profesor de la escuela
#crear un metodo que imprima los estudiantes de la escuela
#crear una instancia de la clase escuela

class Escuela:
    def __init__(self, nombre, salon, grupo, curso, profesor, estudiantes):
        self.nombre = nombre
        self.salon = salon
        self.grupo = grupo
        self.curso = curso
        self.profesor = profesor
        self.estudiantes = estudiantes

    def imprimir_nombre(self):
        print(self.nombre)

    def imprimir_salon(self):
        print(self.salon)

    def imprimir_grupo(self):
        print(self.grupo)

    def imprimir_curso(self):
        print(self.curso)

    def imprimir_profesor(self):
        print(self.profesor)

    def imprimir_estudiantes(self):
        print(self.estudiantes)

escuela1 = Escuela('Escuela 1', 'Salon 1', 'Grupo 1', 'Python', 'Pedro', ['Maria', 'Juan'])
escuela1.imprimir_nombre()
escuela1.imprimir_salon()
escuela1.imprimir_grupo()
escuela1.imprimir_curso()
escuela1.imprimir_profesor()
escuela1.imprimir_estudiantes()

#crear una clase llamada universidad
#crear un metodo que imprima el nombre de la universidad
#crear un metodo que imprima el salon de la universidad
#crear un metodo que imprima el grupo de la universidad
#crear un metodo que imprima el curso de la universidad
#crear un metodo que imprima el profesor de la universidad
#crear un metodo que imprima los estudiantes de la universidad
#crear una instancia de la clase universidad

class Universidad:
    def __init__(self, nombre, salon, grupo, curso, profesor, estudiantes):
        self.nombre = nombre
        self.salon = salon
        self.grupo = grupo
        self.curso = curso
        self.profesor = profesor
        self.estudiantes = estudiantes

    def imprimir_nombre(self):
        print(self.nombre)

    def imprimir_salon(self):
        print(self.salon)

    def imprimir_grupo(self):
        print(self.grupo)

    def imprimir_curso(self):
        print(self.curso)
        
    def imprimir_profesor(self):
        print(self.profesor)

    def imprimir_estudiantes(self):
        print(self.estudiantes)

universidad1 = Universidad('Universidad 1', 'Salon 1', 'Grupo 1', 'Python', 'Pedro', ['Maria', 'Juan'])
universidad1.imprimir_nombre()
universidad1.imprimir_salon()
universidad1.imprimir_grupo()
universidad1.imprimir_curso()
universidad1.imprimir_profesor()
universidad1.imprimir_estudiantes()



