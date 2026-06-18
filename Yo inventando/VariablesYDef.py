###Creación de mobs y variables para el combate
import time
import random
Mobs = ["Slime", "Goblin", "Orco", "Troll"]
Slime = {"Nombre": "Slime Azul", "vida": 200, "daño": 14}
Goblin = {"Nombre": "Goblin Ladron","vida": 150, "daño": 18}
Orco = {"Nombre": "Orco Berserker","vida": 300, "daño": 25}
Troll = {"Nombre": "Troll del bosque", "vida": 250, "daño": 20}


def atacar_enemigo(Mobs):
    daño_jugador = random.randint(3, 21)
    Mobs['vida'] -= daño_jugador
    print(f"Atacas al {Mobs['Nombre']} y causas {daño_jugador}. Salud restante del {Mobs['Nombre']}: {Mobs['vida']} ")
    pass

atacar_enemigo(random.choice(Mobs))