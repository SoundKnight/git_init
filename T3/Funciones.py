# ---<=> MODULOS <=>---
import requests
import os
from requests.exceptions import RequestException
from requests.models import Response

# ---<=> FUNCIONES <=>---
def Limpieza():
    os.system('cls')


def Busqueda_Nombre():
    # ---<=> VARIABLES <=>---
    api_url = 'https://pokeapi.co/api/v2/pokemon/'
    
    # ---<=> PROCESOS <=>---
    print('<=><=><=> BUSCAR POKEMON POR NOMBRE <=><=><=>')
    print('Ingrese el Nombre del Pokemon a Buscar')
    pokemon = input('NOMBRE: ')
    pokemon_url = api_url + pokemon

    Data_Pokemon(pokemon_url)


def Busqueda_ID():
    # ---<=> VARIABLES <=>---
    api_url = 'https://pokeapi.co/api/v2/pokemon/'
    
    # ---<=> PROCESOS <=>---
    print('<=><=><=> BUSCAR POKEMON POR ID <=><=><=>')
    print('Ingrese la ID del Pokemon a Buscar')
    pokemon = input('ID: ')
    pokemon_url = api_url + pokemon

    Data_Pokemon(pokemon_url)


def Tipo_Pokemon():
    # ---<=> VARIABLES <=>---
    api_url = 'https://pokeapi.co/api/v2/type/'
    i = 1

    # ---<=> PROCESOS <=>---
    
    while True:
        try:
            print('\n<=><=><=> BUSCAR POKEMON POR TIPO <=><=><=>')
            while i <= 18:
                url = api_url + str(i)
                response = requests.get(url)
                if response.status_code == 200:
                    data = response.json()
                    Tipo = data['name']
                    print(str(i) + ':', Tipo)
                    i += 1
                else:
                    print('No se Encontro el Tipo')
            print('\nSeleccionar Tipo de Pokemon')
            eleccion = int(input('Eleccion: '))

            if eleccion >= 1 or eleccion <= 18:
                break      

            i = 1
            Limpieza()
            print('Valor Invalido')

        except ValueError:
            i = 1
            Limpieza()
            print('Valor Invalido')

    pokemon_url = api_url + str(eleccion)
    Limpieza()
    Lista_Tipo(pokemon_url)


def Lista_Tipo(pokemon_url = ''):
    # ---<=> VARIABLES <=>---
    j = 1
    k = 1

    # ---<=> PROCESOS <=>---
    response = requests.get(pokemon_url)

    if response.status_code == 200:
        data = response.json()

        tipo = data['name']
        name = [pokemon['pokemon']['name'] for pokemon in data['pokemon']]

        print('<=><=><=> LISTA TIPO <=><=><=>')
        print('TIPO: ', tipo)

        for poke_tipo in name:
            print(str(j) + ': ' , poke_tipo)
            j += 1
            
        while True:
            print('\n¿Desea Guardar en un Archivo TXT')
            print('la Informacion de los Pokemon? [Y/N]')
            guardar = input('Eleccion: ')

            if guardar == 'y' or guardar == 'Y':
                break
            elif guardar == 'n' or guardar == 'N':
                break

            Limpieza()
            print('Valor Invalido')

        if guardar == 'y' or guardar == 'Y':
            if os.path.exists('./Informacion_Pokemon'):
                nombre = './Informacion_Pokemon/' + str(tipo) + '.txt'
                file = open(nombre, 'a')
                for tipo_poke in name:
                    file.write(str(k))
                    file.write(': ')
                    file.write(str(tipo_poke))
                    file.write('\n')
                    k += 1 
                file.close()
            else:
                os.mkdir('./Informacion_Pokemon')
                nombre = str(tipo) + '.txt'
                file = open(nombre, 'a')
                for tipo_poke in name:
                    file.write(str(k))
                    file.write(': ')
                    file.write(str(tipo_poke))
                    file.write('\n')
                    k += 1
                file.close()

            print('\nArchivo Guardado')

        input("\nPresionar ENTER Para Continuar")

    else:
        print('\nPOKEMON NO ENCONTRADO')
        input("\nPresionar ENTER Para Continuar")


def Data_Pokemon(pokemon_url = ''):
    # ---<=> DICCIONARIOS <=>---
    pokemon_data = {
        'Nombre': '',
        'Altura': '',
        'Habilidades': '',
        'Tipo': '',
        'Peso': ''
    }

    # ---<=> PROCESOS <=>---
    response = requests.get(pokemon_url)
    if response.status_code == 200:
        data = response.json()

        pokemon_data['Nombre'] = data['name']
        pokemon_data['Altura'] = data['height']
        pokemon_data['Habilidades'] = [abilities['ability']['name'] for abilities in data['abilities']]
        pokemon_data['Tipo'] = [types['type']['name'] for types in data['types']]
        pokemon_data['Peso'] = data['weight']
        
        Limpieza()
        print('<=><=><=> POKEMON <=><=><=>')
        for clave, valor in pokemon_data.items():
            print(clave + ':', valor)
        input("\nPresionar ENTER Para Continuar")

    else:
        print('\nPOKEMON NO ENCONTRADO')
        input("\nPresionar ENTER Para Continuar")



def Lista_Pokemon(url = 'https://pokeapi.co/api/v2/pokemon?limit=20&', offset = 0, i = 1):
    args = {'offset': offset} if offset else {}

    # ---<=> PROCESOS <=>---
    response = requests.get(url, params = args) 
    if response.status_code == 200:
        data = response.json()
        results = data.get('results', [])

        print('<=><=><=> LISTA POKEMON <=><=><=>')
        if results:
            for pokemon in results:
                name = pokemon['name']
                print(str(i) + ':', name)
                i += 1

        while True:
            print('\n¿Desea Guardar en un Archivo TXT')
            print('la Informacion de los Pokemon? [Y/N]')
            guardar = input('Eleccion: ')

            if guardar == 'y' or guardar == 'Y':
                break
            elif guardar == 'n' or guardar == 'N':
                break

            Limpieza()
            print('Valor Invalido')

        if guardar == 'y' or guardar == 'Y':
            api_url = 'https://pokeapi.co/api/v2/pokemon/'
            for pokemon in results:
                name = pokemon['name']
                pokemon_url = api_url + name
                if os.path.exists('./Informacion_Pokemon'):
                    Lista_Informacion(pokemon_url, offset)
                else:
                    os.mkdir('./Informacion_Pokemon')
                    Lista_Informacion(pokemon_url, offset)

            print('\nArchivo Guardado')
            
        while True:
            print('\n¿Seguir Avanzando en la Lista Pokemon? [Y/N]')
            seguir = input('Eleccion: ')

            if seguir == 'y' or seguir == 'Y':
                break
            elif seguir == 'n' or seguir == 'N':
                break

            Limpieza()
            print('Valor Invalido')

        if seguir == 'y' or seguir == 'Y':
            Limpieza()
            Lista_Pokemon(offset = offset + 20, i = i)


def Lista_Informacion(pokemon_url = '', offset = 0):
    # ---<=> DICCIONARIOS <=>---
    pokemon_data = {
        'Nombre': '',
        'Altura': '',
        'Habilidades': '',
        'Tipo': '',
        'Peso': ''
    }

    # ---<=> PROCESOS <=>---
    response = requests.get(pokemon_url)

    if response.status_code == 200:
        data = response.json()

        pokemon_data['Nombre'] = data['name']
        pokemon_data['Altura'] = data['height']
        pokemon_data['Habilidades'] = [abilities['ability']['name'] for abilities in data['abilities']]
        pokemon_data['Tipo'] = [types['type']['name'] for types in data['types']]
        pokemon_data['Peso'] = data['weight']
        
        nombre = './Informacion_Pokemon/PokeLista_' + str(offset) + '.txt'
        file = open(nombre, 'a')
        file.write('Nombre: ')
        file.write(str(pokemon_data['Nombre']))
        file.write('\n')
        file.write('Altura: ')
        file.write(str(pokemon_data['Altura']))
        file.write('\n')
        file.write('Habilidades: ')
        file.write(str(pokemon_data['Habilidades']))
        file.write('\n')
        file.write('Tipo: ')
        file.write(str(pokemon_data['Tipo']))
        file.write('\n')
        file.write('Peso')
        file.write(str(pokemon_data['Peso']))
        file.write('\n\n')
        file.close()
