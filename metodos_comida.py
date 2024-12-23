class Comida:
    def __init__(self, desayuno, almuerzo, cena):
        self.desayuno = desayuno
        self.almuerzo = almuerzo
        self.cena = cena

    def comer(self):
        print("Esta satisfecho")

desayuno = input("Ingrese que desayuno: ")
almuerzo = input("Ingrese que almorzo: ")
cena = input("Ingrese que ceno: ")

comida_hoy = Comida("desayuno", "almuerzo", "cena")

print(f"Hoy desayuno {desayuno}, almorzo {almuerzo} y ceno {cena}")
print("Si usted ha comido hoy ingrese 'lleno'. ")
while True:
    comer = input()
    if comer.lower() == "lleno":
        comida_hoy.comer()
