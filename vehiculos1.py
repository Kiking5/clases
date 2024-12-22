class Vehiculo:
    def __init__(self, marca, modelo, year):
        self.marca = marca
        self.modelo = modelo
        self.year = year

vehiculo1 = Vehiculo("Renault", "Logan", "2014")
vehiculo2 = Vehiculo("Aveo", "Emotion", "2008")

print(vehiculo1.marca)
print(vehiculo2.year)