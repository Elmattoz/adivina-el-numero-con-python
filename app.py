import random


def juego_adivinanza():
    print("¡Bienvenido al juego de adivinanza!")
    nombre = input("¿Cuál es tu nombre? ")
    print(f"Bueno, {nombre}, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinarlo.")

    numero_secreto = random.randint(1, 100)
    intentos = 8

    while intentos > 0:
        try:
            numero_usuario = int(input("Ingresa un número entre 1 y 100: "))

            if numero_usuario < 1 or numero_usuario > 100:
                print("Número fuera del rango permitido. Intenta de nuevo.")
            elif numero_usuario < numero_secreto:
                print("Incorrecto. El número es mayor.")
                intentos -= 1
            elif numero_usuario > numero_secreto:
                print("Incorrecto. El número es menor.")
                intentos -= 1
            else:
                print(f"¡Felicidades, {nombre}! Adivinaste el número en {8 - intentos + 1} intentos.")
                break

            if intentos == 0:
                print(f"Lo siento, {nombre}. Se acabaron los intentos. El número era {numero_secreto}.")
            else:
                print(f"Te quedan {intentos} intentos.")

        except ValueError:
            print("Por favor, ingresa un número válido.")


juego_adivinanza()