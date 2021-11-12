# ---<=> MODULOS <=>---
import Funciones

# ---<=> DICCIONARIOS <=>---
menu = {
    1: 'Buscar Pokemon por Nombre',
    2: 'Buscar Pokemon por ID',
    3: 'Buscar Pokemon por Tipo',
    4: 'Ver Todos los Nombres de Pokemons',
    5: 'Salir'
}

# ---<=> INICIALIZACION <=>---
if __name__ == '__main__':
    while True:
        while True:
            try:
                print('\n<=><=><=> POKEMON API <=><=><=>')
                for clave, valor in menu.items():
                    print(clave, valor)
                eleccion = int(input('\nEleccion: '))
                
                if eleccion >= 1 and eleccion <= 5:
                    break
                Funciones.Limpieza()
                print("Valor Invalido")
            
            except: 
                Funciones.Limpieza()
                print('Valor Invalido')

        if eleccion == 1:
            Funciones.Limpieza()
            Funciones.Busqueda_Nombre()
            Funciones.Limpieza()
        elif eleccion == 2:
            Funciones.Limpieza()
            Funciones.Busqueda_ID()
            Funciones.Limpieza()
        elif eleccion == 3:
            Funciones.Limpieza()
            Funciones.Tipo_Pokemon()
            Funciones.Limpieza()
        elif eleccion == 4:
            Funciones.Limpieza()
            Funciones.Lista_Pokemon()
            Funciones.Limpieza()
        elif eleccion == 5:
            break

    # ---<=> SALIDA <=>---    
    Funciones.Limpieza()
    print('--- FIN DEL PROGRAMA ---')
    input("\nPresionar ENTER Para Salir")
