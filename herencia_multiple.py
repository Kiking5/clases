class Persona:
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

    def hablar(self):
        print(f"hola, soy {self.nombre}")

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        print(f"Mi habilidad es {self.habilidad}")

class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, sexo, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, sexo)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Sexo: {self.sexo}")
        print(f"Habilidad: {self.habilidad}")
        print(f"Salario: {self.salario}")
        print(f"Empresa: {self.empresa}")

    def presentarse(self):
        return (f"{super().mostrar_habilidad()}")

empleado = EmpleadoArtista("Juan", 30, "M", "Cantar", 1000, "Sony")
empleado.hablar()
empleado.mostrar_datos()
empleado.mostrar_habilidad()
empleado.presentarse()

herencia = issubclass(EmpleadoArtista, Persona)
herencia2 = issubclass(EmpleadoArtista, Artista)
intancia = isinstance(empleado, Persona) 
intancia2 = isinstance(empleado, Artista)

print(herencia)
print(herencia2)
print(intancia)
print(intancia2)