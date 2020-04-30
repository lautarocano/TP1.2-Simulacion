import random as rnd
import matplotlib.pyplot as plt
import numpy as np
import os
 
 
def ruleta():
    return rnd.randint(0,36)
 
def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
 
def juego(calculaPromedio, estrategia, capital = None):
    if capital == None:
        dineroDisp = 0
    else:
        dineroDisp = capital
    valorApuesta = 1
    cantApFav = 0
 
    resultados = []
    resultados.append(dineroDisp)
    frecRelativa = []
    #1 = IMPAR, 0 = PAR
    apuesta = 1
    if (estrategia == "Martingala Pleno"):
        contPerdida = 0
    elif (estrategia == "Fibonacci"):
        contafib = 1
 
    for i in range(iteraciones):
        result = ruleta()
        if (estrategia == "Martingala Par-Impar"):
            if (result%2 == apuesta) & (result != 0):
                dineroDisp += valorApuesta
                valorApuesta = 1
                cantApFav+=1
            else:
                dineroDisp -= valorApuesta
                valorApuesta = valorApuesta*2
        elif (estrategia == "Martingala Pleno"):
            if (result == apuesta):
                dineroDisp += valorApuesta*35
                valorApuesta = 1
                contPerdida = 0
                cantApFav+=1
            else:
                dineroDisp -= valorApuesta
                contPerdida += valorApuesta
                if (valorApuesta*36 <= contPerdida+valorApuesta):
                    valorApuesta += 1
        elif (estrategia == "Fibonacci"):
            if (result%2 == apuesta) & (result != 0):
                dineroDisp += valorApuesta        
                cantApFav += 1
                if contafib<3:
                    contafib = 1
                else:
                    contafib-= 2
            else:
                dineroDisp -= valorApuesta
                contafib+=1
            valorApuesta = fib(contafib)
        resultados.append(dineroDisp)
        frecRelativa.append(cantApFav/(i+1))
        if calculaPromedio:
            promedio[0][i]=promedio[0][i]+dineroDisp/numSim
            promedio[1][i]=promedio[1][i]+cantApFav/(i+1)/numSim
        if capital != None:
            if dineroDisp == 0:
                break
            elif dineroDisp<valorApuesta:
                valorApuesta = dineroDisp
 
    results = []
    results.append(frecRelativa)
    results.append(resultados)
    return results
 
 
def analisisIndividual(estrategia, capital = None):
    results = juego(False, estrategia, capital)
 
    plt.plot(results[0])
    plt.title(estrategia + " - Frecuencia relativa de apuestas ganadas")
    if (estrategia == "Martingala Par-Impar" or estrategia == "Fibonacci"):
        plt.hlines((18/37),0,iteraciones, color='green')
    elif (estrategia == "Martingala Pleno"):
        plt.hlines((1/37),0,iteraciones, color='green')
    plt.ylabel('Frecuencia relativa')
    plt.xlabel('Numero total de apuestas')
    plt.show()
 
    plt.plot(results[1])
    plt.title(estrategia)
    if capital != None:
        plt.ylabel('Dinero')
        plt.hlines(capitalInicial,0,iteraciones, color='green')
    else:
        plt.ylabel('Beneficio acumulado')
        plt.hlines(0,0,iteraciones, color='green')
    plt.xlabel('Numero de apuestas')
    plt.show()
 
def analisisPromedio(estrategia, capital = None):
    global promedio
    promedio = [[],[]]
    din = []
    fr = []
    for i in range(iteraciones):
        promedio[0].append(0)
        promedio[1].append(0)
    for j in range(numSim):
        results = juego(True, estrategia, capital)
        fr.append(results[0])
        din.append(results[1])
 
    for i in range(numSim):
        plt.plot(fr[i])
    plt.plot(promedio[1], color='black', label='Promedio')
    plt.legend(loc="lower left")
    plt.title(estrategia + " - Frecuencia relativa de apuestas ganadas")
    if (estrategia == "Martingala Par-Impar" or estrategia == "Fibonacci"):
        plt.hlines((18/37),0,iteraciones, color='green')
    elif (estrategia == "Martingala Pleno"):
        plt.hlines((1/37),0,iteraciones, color='green')
    plt.ylabel('Frecuencia relativa')
    plt.xlabel('Numero total de apuestas')
    plt.show()
 
    for i in range(numSim):
        plt.plot(din[i])
    plt.plot(promedio[0], color='black', label='Promedio')
    plt.legend(loc="lower left")
    plt.title(estrategia)
    if capital != None:
        plt.ylabel('Dinero')
        plt.hlines(capitalInicial,0,iteraciones, color='green')
    else:
        plt.ylabel('Beneficio acumulado')
        plt.hlines(0,0,iteraciones, color='green')
    plt.xlabel('Numero de apuestas')
    plt.show()
 
 
 
 
def menumc():
    os.system('cls')
    print ("MENÚ MARTINGALA CLASICA - Selecciona una opción")
    print ("1 - MC simple - dinero infinito")
    print ("2 - MC simple - dinero acotado")
    print ("3 - MC promedio - dinero infinito")
    print ("4 - MC promedio - dinero acotado")
    print ("9 - Menu principal")    
 
 
 
def menump():
    os.system('cls')
    print ("MENÚ MARTINGALA PROLONGADA - Selecciona una opción")
    print ("1 - M Prol. simple - dinero infinito")
    print ("2 - M Prol. simple - dinero acotado")
    print ("3 - M Prol. promedio - dinero infinito")
    print ("4 - M Prol. promedio - dinero acotado")
    print ("9 - Menu principal")
 
def menufb():
    os.system('cls')
    print ("MENÚ FIBONACCI - Selecciona una opción")
    print ("1 - FIB simple - dinero infinito")
    print ("2 - FIB simple - dinero acotado")
    print ("3 - FIB promedio - dinero infinito")
    print ("4 - FIB promedio - dinero acotado")
    print ("9 - Menu principal")
 
 
 
def menu():
    os.system('cls')
    print ("MENÚ PRINCIPAL - Selecciona una opción")
    print ("1 - Martingala Clasica")
    print ("2 - Martingala Prolongada")
    print ("3 - Fibonacci")
    print ("9 - Salir")
 
 
 
 
 
promedio = [[],[]]
numSim = 8
capitalInicial = 1000
iteraciones = 500
while True:
    menu()
   
    opcionMenu = input("Inserte su opcion >> ")
 
    if opcionMenu=="1":
        while True:
            menumc()
            opcionMenu = input("Inserte su opcion >> ")
            if opcionMenu=="1":
                analisisIndividual("Martingala Par-Impar")
            elif opcionMenu=="2":
                analisisIndividual("Martingala Par-Impar",capitalInicial)
            elif opcionMenu=="3":
                analisisPromedio("Martingala Par-Impar")
            elif opcionMenu=="4":
                analisisPromedio("Martingala Par-Impar",capitalInicial)
            elif opcionMenu=="9":
                break
            else:
                print(" ")
                input("No has pulsado ninguna opción correcta... \n Pulsa una tecla para continuar")
            os.system('cls')
   
    elif opcionMenu=="2":
        while True:
            menump()
            opcionMenu = input("Inserte su opcion >> ")
            if opcionMenu=="1":
                analisisIndividual("Martingala Pleno")
            elif opcionMenu=="2":
                analisisIndividual("Martingala Pleno",capitalInicial)
            elif opcionMenu=="3":
                analisisPromedio("Martingala Pleno")
            elif opcionMenu=="4":
                analisisPromedio("Martingala Pleno",capitalInicial)
            elif opcionMenu=="9":
                break
            else:
                print(" ")
                input("No has pulsado ninguna opción correcta... \n Pulsa una tecla para continuar")
            os.system('cls')
 
    elif opcionMenu=="3":
        while True:
            menufb()
            opcionMenu = input("Inserte su opcion >> ")
            if opcionMenu=="1":
                analisisIndividual("Fibonacci")
            elif opcionMenu=="2":
                analisisIndividual("Fibonacci",capitalInicial)
            elif opcionMenu=="3":
                analisisPromedio("Fibonacci")
            elif opcionMenu=="4":
                analisisPromedio("Fibonacci",capitalInicial)
            elif opcionMenu=="9":
                break
            else:
                print(" ")
                input("No has pulsado ninguna opción correcta... \n Pulsa una tecla para continuar")
            os.system('cls')
 
 
    elif opcionMenu=="9":
        break
 
    else:
        print ("")
        input("No has pulsado ninguna opción correcta...\nPulsa una tecla para continuar")