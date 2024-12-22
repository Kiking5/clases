class Pelicula:
    def __init__(self, name, genero, clasificacion, temporada):
        self.name = name
        self.genero = genero
        self.clasificacion = clasificacion
        self.temporada = temporada

pelicula1 = Pelicula("Viernes trece", "Terror", "PG-18", "Octubre")
pelicula2 = Pelicula("Avengers", "Acción", "PG-13","Junio")
pelicula3 = Pelicula("Mi Pobre Angelito", "Infantil", "Todos", "Diciembre")

print(pelicula1.name)
print(pelicula1.genero)
print(pelicula2.clasificacion)
print(pelicula3.temporada)