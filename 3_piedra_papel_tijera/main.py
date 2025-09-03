import random


def game3 ():

    def tie():
        tie 
        if rival== player:
            return 
    opciones = ["Piedra", "Papel", "Tijeras"]
    rival = random.choice (opciones)
    while True: 
        player = input(
        "Elige:\n"
        "piedra\n"
        "papel\n"
        "tijeras\n"
)
        player= player.capitalize()
        print ("el rival elige: ", rival, " VS tú eliges: ", player)
        if player == rival:
            print("Empate, juega otra vez.\n")
            rival = random.choice(opciones)  # el rival cambia de elección
        elif (player == "Piedra" and rival == "Tijeras") \
          or (player == "Papel" and rival == "Piedra") \
          or (player == "Tijeras" and rival == "Papel"):
            print("¡Ganaste!\n")
            break
        else:
            print("¡Perdiste!\n")
            break

game3()