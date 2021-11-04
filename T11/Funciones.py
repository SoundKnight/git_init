# ---<=> MODULOS <=>---
import os
import random

# ---<=> VARIABLES <=>---
def Globales():
    global GJ1
    GJ1 = 0
    global GJ2
    GJ2 = 0
    global EJJ
    EJJ = 0
    global GCPU
    GCPU = 0
    global PCPU
    PCPU = 0
    global ECPU
    ECPU = 0
    global PJJ
    PJJ = 0
    global PJCPU
    PJCPU = 0
    global PJT
    PJT = 0

# ---<=> DICCIONARIOS <=>---
PPT = {
    1: 'Piedra',
    2: 'Papel',
    3: 'Tijeras'
}

# ---<=> FUNCIONES <=>---
def JvsJ():
    global GJ1
    global GJ2
    global EJJ
    global PJJ
    global PJT
    
    while True:    
        try:
            print('\n<=><=><=> JUGADOR VS JUGADOR <=><=><=>')
            for clave, valor in PPT.items():
                print(clave, valor)
            print('\nJUGADOR 1')
            SJ1 = int(input('Seleccion: '))
            if SJ1 >= 1 and SJ1 <= 3:
                break
            Limpieza()
            print('Valor Invalido')

        except ValueError:
            Limpieza()
            print('Valor Invalido')
    Limpieza()
    
    while True:    
        try:
            print('\n<=><=><=> JUGADOR VS JUGADOR <=><=><=>')
            for clave, valor in PPT.items():
                print(clave, valor)
            print('\nJUGADOR 2')
            SJ2 = int(input('Seleccion: '))
            if SJ2 >= 1 and SJ2 <= 3:
                break
            Limpieza()
            print('Valor Invalido')

        except ValueError:
            Limpieza()
            print('Valor Invalido')

    PJJ += 1
    PJT += 1
    if SJ1 == SJ2:
        Limpieza()
        print('\n<=><=><=> JUGADOR VS JUGADOR <=><=><=>')
        print('Ganador: Empate')
        input("\nPresionar ENTER Para Continuar")
        EJJ += 1
        Limpieza()
    elif SJ1 == 1 and SJ2 == 2:
        Limpieza()
        print('\n<=><=><=> JUGADOR VS JUGADOR <=><=><=>')
        print('Ganador: Jugador 2')
        input("\nPresionar ENTER Para Continuar")
        GJ2 += 1
        Limpieza()
    elif SJ1 == 1 and SJ2 == 3:
        Limpieza()
        print('\n<=><=><=> JUGADOR VS JUGADOR <=><=><=>')
        print('Ganador: Jugador 1')
        input("\nPresionar ENTER Para Continuar")
        GJ1 += 1
        Limpieza()
    elif SJ1 == 2 and SJ2 == 1:
        Limpieza()
        print('\n<=><=><=> JUGADOR VS JUGADOR <=><=><=>')
        print('Ganador: Jugador 1')
        input("\nPresionar ENTER Para Continuar")
        GJ1 += 1
        Limpieza()
    elif SJ1 == 2 and SJ2 == 3:
        Limpieza()
        print('\n<=><=><=> JUGADOR VS JUGADOR <=><=><=>')
        print('Ganador: Jugador 2')
        input("\nPresionar ENTER Para Continuar")
        GJ2 += 1
        Limpieza()
    elif SJ1 == 3 and SJ2 == 1:
        Limpieza()
        print('\n<=><=><=> JUGADOR VS JUGADOR <=><=><=>')
        print('Ganador: Jugador 2')
        input("\nPresionar ENTER Para Continuar")
        GJ2 += 1
        Limpieza()
    elif SJ1 == 3 and SJ2 == 2:
        Limpieza()
        print('\n<=><=><=> JUGADOR VS JUGADOR <=><=><=>')
        print('Ganador: Jugador 1')
        input("\nPresionar ENTER Para Continuar")
        GJ1 += 1
        Limpieza()


def JvsCPU():
    global GCPU
    global PCPU
    global ECPU
    global PJCPU
    global PJT

    while True:    
        try:
            print('\n<=><=><=> JUGADOR VS CPU <=><=><=>')
            for clave, valor in PPT.items():
                print(clave, valor)
            print('\nJUGADOR')
            SJ = int(input('Seleccion: '))
            if SJ >= 1 and SJ <= 3:
                break
            Limpieza()
            print('Valor Invalido')

        except ValueError:
            Limpieza()
            print('Valor Invalido')

    SCPU = random.randrange(1, 4)
    Limpieza()

    PJCPU += 1
    PJT += 1
    if SJ == SCPU:
        Limpieza()
        print('\n<=><=><=> JUGADOR VS CPU <=><=><=>')
        print('Seleccion CPU:', SCPU)
        print('\nGanador: Empate')
        input("\nPresionar ENTER Para Continuar")
        ECPU += 1
        Limpieza()
    elif SJ == 1 and SCPU == 2:
        Limpieza()
        print('\n<=><=><=> JUGADOR VS CPU <=><=><=>')
        print('Seleccion CPU:', SCPU)
        print('\nGanador: CPU')
        input("\nPresionar ENTER Para Continuar")
        PCPU += 1
        Limpieza()
    elif SJ == 1 and SCPU == 3:
        Limpieza()
        print('\n<=><=><=> JUGADOR VS CPU <=><=><=>')
        print('Seleccion CPU:', SCPU)
        print('\nGanador: Jugador')
        input("\nPresionar ENTER Para Continuar")
        GCPU += 1
        Limpieza()
    elif SJ == 2 and SCPU == 1:
        Limpieza()
        print('\n<=><=><=> JUGADOR VS CPU <=><=><=>')
        print('Seleccion CPU:', SCPU)
        print('\nGanador: Jugador')
        input("\nPresionar ENTER Para Continuar")
        GCPU += 1
        Limpieza()
    elif SJ == 2 and SCPU == 3:
        Limpieza()
        print('\n<=><=><=> JUGADOR VS CPU <=><=><=>')
        print('Seleccion CPU:', SCPU)
        print('\nGanador: CPU')
        input("\nPresionar ENTER Para Continuar")
        PCPU += 1
        Limpieza()
    elif SJ == 3 and SCPU == 1:
        Limpieza()
        print('\n<=><=><=> JUGADOR VS CPU <=><=><=>')
        print('Seleccion CPU:', SCPU)
        print('\nGanador: CPU')
        input("\nPresionar ENTER Para Continuar")
        PCPU += 1
        Limpieza()
    elif SJ == 3 and SCPU == 2:
        Limpieza()
        print('\n<=><=><=> JUGADOR VS CPU <=><=><=>')
        print('Seleccion CPU:', SCPU)
        print('\nGanador: Jugador')
        input("\nPresionar ENTER Para Continuar")
        GCPU += 1
        Limpieza()

def Estadisticas():
    global GJ1
    global GJ2
    global EJJ
    global GCPU
    global PCPU
    global ECPU
    global PJJ
    global PJCPU
    global PJT
    
    print('<=><=><=> ESTADISTICAS <=><=><=>')
    print('--- PARTIDAS ---')
    print('Partidas Jugadas JvsJ:', PJJ)
    print('Partidas Jugadas JvsCPU:', PJCPU)
    print('Total de Partidas Jugadas:', PJT)
    print('\n--- JUGADOR VS JUGADOR ---')
    print('Partidas Ganadas Jugador 1:', GJ1)
    print('Partidas Ganadas Jugador 2:', GJ2)
    print('Partidas Empatadas:' , EJJ)
    print('\n--- JUGADOR VS CPU ---')
    print('Partidas Ganadas:', GCPU)
    print('Partidas Perdidas:', PCPU)
    print('Partidas Empatadas:' , ECPU)

def Limpieza():
    os.system('cls')