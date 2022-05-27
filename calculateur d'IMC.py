from time import sleep
import os

imc = 0

while True :

    print('''
Ceci est un calculateur d'IMC
''')

    height = input("Quelle taille fait-tu ? (en cm)     ")
    print('')
    mass = input("Quelle poids fait-tu ? (en kg)     ")
    print('')

    height = int(height)/100
    height = height*height
    mass = int(mass)

    imc = mass/height

    print('')
    if imc < 18.5 :
        print(imc)
        print()
        print('Tu est en sous poids')
        sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')
    
    if imc > 18.5 and imc < 25 :
        print(imc)
        print()
        print('Tu est en poids normal')
        sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')

    if imc > 25 and imc < 30 :
        print(imc)
        print()
        print('Tu est en surpoids')
        sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')

    if imc > 30 and imc < 35 :
        print(imc)
        print()
        print('Tu est en faible obésité')
        sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')

    if imc > 35 and imc < 40 :
        print(imc)
        print()
        print('Tu est en obésité moyenne')
        sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')

    if imc > 40 :
        print(imc)
        print()
        print('Tu est en obésité sevère')
        sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')
