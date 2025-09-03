import random

n = random.randint(1, 10)
def guess_the_number (n):
    victory = True
    while True:
        nuser = input("Inserta un número: ")
        nuser= int(nuser)
        if nuser== n:
            print ("has acertado! el número era: ", n)
            break 
        else: 
            if n> nuser:
                print ("MÁS ALTO")
            if n< nuser:
                print("más bajito")
            
    return victory
guess_the_number(n)