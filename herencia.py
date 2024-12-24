class Persona:
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

    def hablar(self):
        print(f"hola, soy {self.nombre}")

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, carrera):
        super().__init__(nombre, edad, sexo)
        self.carrera = carrera

    def estudiar(self):
        print(f"Estudiando {self.carrera}")

class Profesor(Persona):
    def __init__(self, nombre, edad, sexo, materia):
        super().__init__(nombre, edad, sexo)
        self.materia = materia

    def enseñar(self):
        print(f"Enseñando {self.materia}")

maria = Estudiante("Maria", 20, "F", "Ingenieria de sistemas")
maria.hablar()
maria.estudiar()

juan = Profesor("Juan", 30, "M", "Matematicas")
juan.hablar()
juan.enseñar()

