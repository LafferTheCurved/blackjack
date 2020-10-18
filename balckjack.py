

import random
import time

mazo = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

cartas_compu = []

def juego():
    plantado = False
    carta1 = random.choice(mazo)
    carta2 = random.choice(mazo)
    carta_compu1 = random.choice(mazo)
    carta_compu2 = random.choice(mazo)
    computadora = carta_compu1 + carta_compu2
    cartas_compu.append(carta_compu1)
    cartas_compu.append(carta_compu2)
    if carta1 == 1 and carta2 == 1:
        carta1 = 11
        carta2 = 10
    if carta1 == 1:
        inp = int(input("Tu carta es 1. Queres sumar 1 u 11?"))
        if inp == 1:
            carta1 = 1
        elif inp == 11:
            carta1 = 11
    elif  carta2 == 1:
        inp = int(input("Tu carta es 1. Queres sumar 1 u 11?"))
        if inp == 1:
            carta2 = 1
        elif inp == 11:
            carta2 = 11
    player = carta1 + carta2
    if player == 21:
        print("Tus cartas son 1 y 1. Total:", player)
    else:        
        print("Tus cartas son ", carta1, " y ", carta2, " Total: ", player)
    print("Computadora tiene ", carta_compu2)
    if computadora <= 18:
        while computadora <= 17:
            carta_compu3 = random.choice(mazo)
            computadora = computadora + carta_compu3
            cartas_compu.append(carta_compu3)
    else:
        computadora
    while plantado == False:
        n = input("Otra o te plantas? ")
        time.sleep(1)
        if n == "p":
            print("Te plantas")
            print(" Total: ", player)
            plantado = True
        elif n == "o":
            print("Otra")
            carta1 = random.choice(mazo)
            if carta1 == 1:
                inp2 = int(input("Tu carta es 1. Queres sumar 1 u 11? "))
                if inp2 == 1:
                    player = player + inp2
                    print("Total: ", player)
                elif inp2 == 11:
                    player = player + inp2
                    print("Total: ", player)
            else: 
                player = player + carta1
                if player <= 21:
                    print("Tu carta es ", carta1, " Total: ", player)
                else:
                    print("Tu carta es ", carta1, " Total: ", player)
                    plantado = True
    print("Computadora tiene estas cartas: ",cartas_compu, " Total: ", computadora)
    time.sleep(0.5) 
    if player == 21:
        print("Blackjack! Tu ganas")
    elif computadora > player and computadora <= 21:
        print("La casa gana!")
    elif player > computadora and player <= 21:
        print("Ganaste!")
    elif player == computadora:
        print("Empate")
    elif player > 21 and computadora > 21:
        print("Ambos perdieron")
    elif player > 21 and computadora <= 21:
        print("La casa gana!")
    elif computadora > 21 and player <= 21:
        print("Ganaste!")

nombre = input("¿Cómo te llamas? ")
print("Bienvenido ", nombre, "!")
time.sleep(1)
print("En este casino, las reglas son las siguientes:")
time.sleep(1)
print("Escribí 'o' cuando quieras otra carta. Escribí 'p' cuando quieras plantarte.")
time.sleep(1)

juego()       



