class Vehiculo:
    def __init__(self, marca, modelo, year):
        self.marca = marca
        self.modelo = modelo
        self.year = year

    def conducir(self):
        print("Conduciendo...")

marca = input("Cual es la marca del vehiculo?: ")
modelo = input("Cual es el modelo?: ")
year = input("Cual es el año?: ")

vehiculo1 = Vehiculo("nombre", "modelo", "year")

print(f"DATOS DEL VEHICULO\n Nombre: {marca}\n Modelo: {modelo}\n year: {year}")
print("Ingrese conducir si usted esta conduciendo.")

while True:
    conducir = input()
    if (conducir.lower() == "conducir"):
        vehiculo1.conducir()