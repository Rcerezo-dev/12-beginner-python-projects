import random 
from words import *

# def hangman():
#     palabra = random.choice(words)
#     vidas = 10 
#     incorrect = [] 
#     partialsol = list("_" * len(palabra))
#     print(" ".join(partialsol))

#     while True:
#         respuesta1 = input("Prueba una letra o intro para resolver: ")
#         respuesta1 = respuesta1.lower()
#         if len(respuesta1) > 1:
#             print("⚠️ Solo puedes introducir una letra o pulsar intro para resolver.")
#             print(" ".join(partialsol))
#             continue  

#         elif respuesta1 == "":
#             finalanswer = input("Introduce la palabra que crees que es: ")
#             finalanswer = finalanswer.lower()
#             if finalanswer == palabra:
#                 print("¡Has ganado!")
#                 break
#             else: 
#                 print("Esa no es la palabra")
#                 vidas -= 1
#                 incorrect.append(finalanswer)
#                 print("Tus intentos fallidos han sido:", ", ".join(incorrect))
#                 print("Te quedan", vidas, "vidas") 

#         else: 
#             acertada = False
#             for i, letra in enumerate(palabra):
#                 if letra == respuesta1:
#                     partialsol[i] = letra
#                     acertada = True

#             if acertada:
#                 print(" ".join(partialsol))
#                 if "".join(partialsol) == palabra:
#                     print("¡Has ganado!")
#                     break
#             else: 
#                 print("Esa letra no está en la palabra")
#                 vidas -= 1
#                 incorrect.append(respuesta1)
#                 print("Tus intentos fallidos han sido:", ", ".join(incorrect))
#                 print("Te quedan", vidas, "vidas")

#         if vidas == 0:
#             print("Has perdido, la palabra era:", palabra)
#             break


def play_hangman():
    word = random.choice(words).upper()
    attempts = 8
    correct_letters = []
    wrong_letters = []

    print("⚠️ You can type a letter or press Enter to guess the word.")
    
    while attempts > 0:
        display_word = [letter if letter in correct_letters else '_' for letter in word]
        print(' '.join(display_word))
        
        if '_' not in display_word:
            print("🎉 Congratulations! You guessed the word:", word)
            break

        guess = input("Try a letter or press Enter to guess the word: ").upper()

        if guess == "":
            full_guess = input("Enter your guess for the full word: ").upper()
            if full_guess == word:
                print("🎉 Amazing! You guessed the word correctly:", word)
                break
            else:
                attempts -= 1
                print(f"❌ Wrong guess. Attempts left: {attempts}")
        elif len(guess) == 1 and guess.isalpha():
            if guess in correct_letters or guess in wrong_letters:
                print("⚠️ You already tried that letter.")
            elif guess in word:
                correct_letters.append(guess)
                print(f"✅ Good job! {guess} is in the word.")
            else:
                wrong_letters.append(guess)
                attempts -= 1
                print(f"❌ {guess} is not in the word. Attempts left: {attempts}")
        else:
            print("⚠️ Invalid input. Please enter a single letter or press Enter.")

    else:
        print("💀 Game over. The word was:", word)

if __name__ == "__main__":
    play_hangman()
