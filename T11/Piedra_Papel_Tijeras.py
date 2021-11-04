# ---<=> MODULOS <=>---
import Funciones

# ---<=> DICCIONARIOS <=>---
juego= {
    1: 'Jugador vs Jugador',
    2: 'Jugador vs CPU',
    3: 'Estadisticas',
    4: 'Salir'
}

Funciones.Globales()

# ---<=> SCRIPT <=>---
while True:
    while True:
        try:
            print('\n<=><=><=> PIEDRA PAPEL O TIJERAS <=><=><=>')
            for clave, valor in juego.items():
                print(clave, valor)
            jugador = int(input('\nEleccion: '))
            if jugador >= 1 and jugador <= 4:
                break
            Funciones.Limpieza()
            print("Valor Invalido")
            
        except ValueError:
            Funciones.Limpieza()
            print("Valor Invalido")

    if jugador == 1:
        Funciones.Limpieza()
        Funciones.JvsJ()
    elif jugador == 2:
        Funciones.Limpieza()
        Funciones.JvsCPU()
    elif jugador == 3:
        Funciones.Limpieza()
        Funciones.Estadisticas()
        input("\nPresionar ENTER Para Continuar")
        Funciones.Limpieza()
    elif jugador == 4:
        Funciones.Limpieza()
        Funciones.Estadisticas()
        input("\nPresionar ENTER Para Salir")
        Funciones.Limpieza()
        break

# ---<=> SALIDA <=>---
Funciones.Limpieza()
print("Fin del Programa")