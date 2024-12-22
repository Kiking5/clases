class Comida:
    def __init__(self, desayuno, almuerzo, cena):
        self.desayuno = desayuno
        self.almuerzo = almuerzo
        self.cena = cena

comida_dia_uno = Comida("cereales", "costillas", "caldo")
comida_dia_dos = Comida("Recalentado", "Pezcado", "Arepa")
comida_dia_tres = Comida("Cruasan", "Costillas", "Sandwish")

print(comida_dia_uno.desayuno)
print(comida_dia_dos.almuerzo)
print(comida_dia_tres.cena)