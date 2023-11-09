from flask import Flask, request, jsonify
import sys
import time
import requests

app = Flask(__name__)

# Obtén el puerto de los argumentos de la línea de comandos
if len(sys.argv) != 2:
    print("Uso: python main.py <puerto>")
    sys.exit(1)

puerto = int(sys.argv[1])


cant_peticiones=0


@app.route('/')
def info():
    return {
        "hola":"mundo"
    }


@app.route('/conect_proxi')
def conect_proxi():
    ip = request.host
    # URL del servidor proxy
    proxy_url = 'http://127.0.0.1:8080'  # Reemplaza con la URL del servidor proxy
    # Envia tu IP al servidor proxy al iniciar
    response = requests.get(f'{proxy_url}/conect/{ip}')
    print("ip enviada")
    return response.json()

@app.route('/<type_request>')
def index(type_request):
    print()
    global cant_peticiones
    cant_peticiones+=1
        
    # Simular diferentes tipos de peticiones con tiempos de respuesta variables
    if type_request == 1:
        # Simular una petición rápida
        time.sleep(1)  # Tiempo de espera corto
        response_data = {"tipo_peticion": "A"}
    elif type_request==2:
        # Simular una petición media
        time.sleep(2)  # Tiempo de espera medio
        response_data = {"tipo_peticion": "A"}
    else:
        # Simular una petición más lenta
        time.sleep(3)  # Tiempo de espera más largo
        response_data = {"tipo_peticion": "b"}

    return {
        "mensaje": f"Server en puerto {puerto}",
        "cant_peticiones": cant_peticiones,
        "ip": request.host,
        **response_data  # Agregar detalles de tipo de petición y tiempo de espera
    }


if __name__ == '__main__':
    app.run(port=puerto, debug=True)
