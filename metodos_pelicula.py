class Pelicula:
    def __init__(self, name, genero, clasificacion, temporada):
        self.name = name
        self.genero = genero
        self.clasificacion = clasificacion
        self.temporada = temporada

    def ver_pelicula(self):
        print("Viendo la pelicula!....")

name = input("Ingrese el nombre de la pelicula: ")
genero = input("Ingrese el genero: ")
clasificacion = input("Ingrese la clasificación: ")
temporada = input("Ingrese la temporada de estreno: ")

pelicula1 = Pelicula("name", " genero", "clasificacion", "temporada" )

print(f"La pelicula es '{name}', su genero es {genero} con clasificación {clasificacion} y se estreno en la temporada de {temporada}.")
print("Ingrese 'viendo' si usted esta viendo la pelicula.")
while True:
    ver_pelicula = input()
    if ver_pelicula.lower() == "viendo":
        pelicula1.ver_pelicula()