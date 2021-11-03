# ---<=> MODULOS <=>---
import requests

# ---<=> SCRIPT <=>---
if __name__ == '__main__':
    url = 'https://api.hunter.io/v2/domain-search?domain=stripe.com&api_key=9b0f56c3fd7372a39c1d0becea9acc692387799b'
    
    print('<=><=> BUSQUEDA DE DOMINIO <=><=>')
    dominio = input('\nDominio: ')

    args = {'domain': dominio}
    response =  requests.get(url, params = args)

    if response.status_code == 200:
        print(response)
        content = response.content
        print(content)
    else:
        print('No se Encontro la Pagina')
        print(response)