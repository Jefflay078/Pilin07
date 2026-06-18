import random

print("****************************************")
print("**********BIENVENIDO AL ORÁCULO*********")
print("****************************************")
print("Qloke, soy tu panita el oráculo, cuéntame")
Nombre = input("¿Cómo te llamas?: ")
print("Hola", Nombre, "¿Qué deseas saber?")
Pregunta = input("Escribe tu pregunta: ")

Respuesta = random.randint(1, 3)
if Respuesta == 1:
    print("Sí, definitivamente")
elif Respuesta == 2:    print("No, tú ere un duro")
else:    print("Tal vez")

print("Gracias por usar el oráculo, vuelve pronto")