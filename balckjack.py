

import random
import time

x = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

cartas_compu = []

def juego():
    r = False
    y = random.choice(x)
    z = random.choice(x)
    cy = random.choice(x)
    cz = random.choice(x)
    computadora = cy + cz
    cartas_compu.append(cy)
    cartas_compu.append(cz)
    if y == 1 and z == 1:
        y = 11
        z = 10
    if y == 1:
        a = int(input("Tu carta es 1. Queres sumar 1 u 11?"))
        if a == 1:
            y = 1
        elif a == 11:
            y = 11
    elif  z == 1:
        a = int(input("Tu carta es 1. Queres sumar 1 u 11?"))
        if a == 1:
            z = 1
        elif a == 11:
            z = 11
    player = y + z
    if player == 21:
        print("Tus cartas son 1 y 1. Total:", player)
    else:        
        print("Tus cartas son ", y, " y ", z, " Total: ", player)
    print("Computadora tiene ", cz)
    if computadora <= 18:
        while computadora <= 17:
            cr = random.choice(x)
            computadora = computadora + cr
            cartas_compu.append(cr)
    else:
        computadora
    while r == False:
        n = input("Otra o te plantas? ")
        time.sleep(1)
        if n == "p":
            print("Te plantas")
            print(" Total: ", player)
            r = True
        elif n == "o":
            print("Otra")
            y = random.choice(x)
            if y == 1:
                h = int(input("Tu carta es 1. Queres sumar 1 u 11? "))
                if h == 1:
                    player = player + h
                    print("Total: ", player)
                elif h == 11:
                    player = player + h
                    print("Total: ", player)
            else: 
                player = player + y
                if player <= 21:
                    print("Tu carta es ", y, " Total: ", player)
                else:
                    print("Tu carta es ", y, " Total: ", player)
                    r = True
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

j = input("¿Cómo te llamas? ")
print("Bienvenido ", j, "!")
time.sleep(1)
print("En este casino, las reglas son las siguientes:")
time.sleep(1)
print("Escribí 'o' cuando quieras otra carta. Escribí 'p' cuando quieras plantarte.")
time.sleep(1)

juego()       



