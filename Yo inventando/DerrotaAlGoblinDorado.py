#DerrotaAlGoblinDorado

##Creacion de personajes...

Jugadores = ["Player", "Goblin"]

Player = {"Nombre": "Ethan", "Salud": 100, "Daño": 15, "Especial": 35, "Defensa": 0.5 }
Goblin = {"Nombre": "Goblin Dorado", "Salud": 100, "Daño": 12, "DañoCritico": 30, "Curacion": 10}

def AtaqueComun (Player, Goblin):
    Goblin["Salud"] -= Player["Daño"]
    print(f"\n-> Has atacado al {Goblin['Nombre']} y ha recibido {Player['Daño']} de daño.")
    return

def AtaqueEspecial (Player, Goblin):
    Goblin["Salud"] -= Player["Especial"]
    print(f"\n-> ¡Bárbaro! Has atacado al {Goblin['Nombre']} y le has causado {Player['Especial']} DE DAÑOOO!!!")
    return

def DefensaJugador (Player, Goblin):
    # La defensa se procesa aquí visualmente, pero la reducción de daño real se calcula en el turno del Goblin
    print("\n-> Te has defendido. Concentras energía para el próximo turno y reducirás el daño recibido a la mitad.")
    return

def AtaqueGoblin(Goblin, Player, esta_defendido):
    dano_real = Goblin["Daño"]
    if esta_defendido:
        dano_real *= Player["Defensa"] # Reduce al 50%
    Player["Salud"] -= dano_real
    print(f"<- {Player['Nombre']} ha sido atacado por el {Goblin['Nombre']} causándole {dano_real} de daño.")
    return

def CriticoGoblin(Goblin, Player, esta_defendido):
    dano_real = Goblin["DañoCritico"]
    if esta_defendido:
        dano_real *= Player["Defensa"] # Reduce al 50%
    Player['Salud'] -= dano_real
    print(f"<- {Player['Nombre']} ha sido atacado por el {Goblin['Nombre']} causándole {dano_real} de daño, ¡CAGASTEEE!")
    return

def Recuperacion(Goblin):
    Goblin["Salud"] += Goblin["Curacion"]
    print(f"<- EL {Goblin['Nombre']} HA RECUPERADO {Goblin['Curacion']} DE SALUD.")
    return

##EMPEZAREMOS CON LA INTERFAZ GRÁFICA..............

print("********************************************************************")
print("**********************DERROTA AL GOBLIN DORADO**********************")
print("********************************************************************")

# Variables de control del bucle de juego
turno_actual = 1
defendido_anterior = False # Es pa' saber si el jugador se cubrió en el turno anterior
# Ciclo principal de combate
while Player["Salud"] > 0 and Goblin["Salud"] > 0:
    print(f"\n=== TURNO {turno_actual} ===")
    print(f"--- Estado: {Player['Nombre']}: {Player['Salud']} HP | {Goblin['Nombre']}: {Goblin['Salud']} HP ---")
    
    # --- TURNO DEL JUGADOR ---
    print("Elige tu acción:")
    print("1. Ataque Normal (15 HP de daño)")
    print("2. Ataque Cargado (35 HP de daño - Requiere haberse defendido el turno anterior)")
    print("3. Defensa y Concentración (Reduce daño a la mitad este turno y carga energía)")
    
    opcion = input("Selecciona (1-3): ")
    
    se_defendio_este_turno = False # Reinicia el estado de defensa para el turno actual
    
    if opcion == "1":
        AtaqueComun(Player, Goblin)
        defendido_anterior = False # Pierde la carga si no se defiende de nuevo
    elif opcion == "2":
        if defendido_anterior:
            AtaqueEspecial(Player, Goblin)
            defendido_anterior = False # Consume la carga
        else:
            print("\n-> ¡FALLO PENALIZADO! Intentaste un ataque cargado sin energía. Haces 0 de daño y pierdes el turno. MARICÓN")
            defendido_anterior = False
    elif opcion == "3":
        DefensaJugador(Player, Goblin)
        se_defendio_este_turno = True
        # NO cambiamos 'defendido_anterior' a True todavía, lo haremos al final del turno completo.
    else:
        print("\n-> Acción inválida. Te quedaste pasmado mirando al Goblin y perdiste el turno. Gay")
        defendido_anterior = False

    # Verificar si el Goblin murió tras el ataque del jugador
    if Goblin["Salud"] <= 0:
        break

    # --- TURNO DEL GOBLIN (Patrón predictivo) ---
    print(f"\n[Acción del {Goblin['Nombre']}]:")
    
    if turno_actual % 2 != 0:
        # Turnos impares: 1, 3, 5, 7...
        AtaqueGoblin(Goblin, Player, se_defendio_este_turno)
    elif turno_actual % 4 == 0:
        # Turnos múltiplos de 4: 4, 8, 12...
        CriticoGoblin(Goblin, Player, se_defendio_este_turno)
    else:
        # Demás turnos pares: 2, 6, 10...
        Recuperacion(Goblin)

    # Actualizar la carga para el siguiente turno basándonos en si se defendió EN ESTE turno
    defendido_anterior = se_defendio_este_turno
    
    # Avanzar el contador de turnos
    turno_actual += 1

# --- FIN DEL JUEGO ---
print("\n********************************************************************")
print("*************************** FIN DEL COMBATE ************************")
print("********************************************************************")

if Player["Salud"] <= 0 and Goblin["Salud"] <= 0:
    print(f"¡Un empate mortal! Ambos cayeron en el turno {turno_actual}.")
elif Player["Salud"] > 0:
    print(f"¡VICTORIA! {Player['Nombre']} ha derrotado al {Goblin['Nombre']}.")
    print(f"El combate duró: {turno_actual} turnos.")
else:
    print(f"¡DERROTA! El {Goblin['Nombre']} te ha destruido... Más suerte la próxima vez.")
    print(f"Caíste en el turno: {turno_actual}.")