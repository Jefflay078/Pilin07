import time
import random
print("****************")
print("Derrota al slime")
print("*****************")
print("Un slime se interpone en tu camino, ¿qué harás?")
print("1. Atacar con tu espada")
print("2. Huir")
opciones = input("Elige una opción bbrgrl (1 o 2): ")
if opciones == "1":
    time.sleep(0.5)
    print("Decides atacar al slime con tu espada.")
    vida_jugador = 500
    vida_slime = 100
    daño_slime = 14
    ataque_minimo = 3
    daño_critico = 8
    while (vida_slime > 0):
        ataque_jugador = random.randint(ataque_minimo, daño_critico)
        vida_slime -= ataque_jugador
        print(f"Atacas al slime y le haces {ataque_jugador} de daño. Vida del slime: {vida_slime}")
        time.sleep(0.5)
        if vida_slime <= 0:
            print("¡Has derrotado al slime!")
            break
        vida_jugador -=daño_slime
        print(f"El slime te ataca y te hace {daño_slime} de daño. Tu vida: {vida_jugador}")
        time.sleep(0.5)
        if vida_jugador <= 0:
            print("Has sido derrotado por el slime, cagaste kasdjaksdjasdjaskjdajk")
            break
elif (opciones == "2"):
    time.sleep(0.5)
    print("Intentas huir, pero tropiezas con una roca y caes inconsciente, lo ultimo que ves es el slime acercándose... Cagaste")
else:
    print("Opción no válida, el slime se aburre de tu indecisión y te ataca, cagaste")