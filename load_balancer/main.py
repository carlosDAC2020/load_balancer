from flask import Flask, request, redirect
import requests
import random

app = Flask(__name__)



servers=[]

# Variable para llevar el control del servidor actual
current_server_index = 0

# funciones auxiliares 
def validations():
    global servers
    if "favicon.ico" in servers:
        servers.remove("favicon.ico")


@app.route('/<tipo_peticion>')
def index(tipo_peticion=None):
    global current_server_index
    global servers

    validations()

    if len(servers) > 0:
        if current_server_index == len(servers):
            current_server_index = 0
            
        # Seleccionar el próximo servidor en la lista
        selected_server = servers[current_server_index]
        print("entro al server", current_server_index + 1)
        current_server_index += 1

        ip, port = selected_server.split(':')  # Dividir la dirección IP y el puerto
        
        # Construir la URL con el tipo de petición 
        url = f'http://{ip}:{port}/{tipo_peticion}' 
        
        response = requests.get(url)

        return response.json()
    else:
        return 'Sin servidores activos'

list_servers=set()
@app.route('/conect/<ip>')
def get_servers(ip):
    list_servers.add(ip)
    
    global servers
    servers = list(list_servers)
    print(servers)
    return {
        "mensaje":"ip resivida",
        "ip":ip
    }

    
if __name__ == '__main__':
    app.run(port=8080, debug=True)
