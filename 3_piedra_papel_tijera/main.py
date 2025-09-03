import random

def game3 ():
    """Juego de Piedra, Papel o Tijeras"""
    def tie():
        """funcion para el empate"""
        if rival== player:
            return True 
    # Inicializamos opciones y elegimos la del rival
    opciones = ["Piedra", "Papel", "Tijeras"] 
    rival = random.choice (opciones)
    # Bucle principal del juego
    while True: 
        # Pedimos la elección del jugador entre 3 posibles opciones (no validamos)
        player = input(
        "Elige:\n"
        "piedra\n"
        "papel\n"
        "tijeras\n"
)
        #ponemos la primera letra en mayuscula para que coincida con las opciones
        player= player.capitalize()

        #informamos de las elecciones
        print ("el rival elige: ", rival, " VS tú eliges: ", player)

        #comprobamos las condiciones de victoria, derrota o empate
        if player == rival:
            tie()
            print("¡Empate! Juega de nuevo\n")
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