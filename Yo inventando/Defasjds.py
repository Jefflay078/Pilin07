import time
import random

def saludo():
    print("Qloke men, tamo frío de ete lao")
    pass
def calcular_ataque(minimo, maximo):
    ataque = random.randint(minimo, maximo)
    return ataque
print("Arrancando programa...")
time.sleep(1)
saludo()
time.sleep(0.5)
print("Preparando ataque...")
time.sleep(1)
calcular_ataque(8, 12)
calcular_ataque(20, 50)
time.sleep(0.5)
print("programa finalizado")
