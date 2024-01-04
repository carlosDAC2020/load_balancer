from flask import Flask, request, jsonify
import sys
import time
import requests

app = Flask(__name__)

# URL del servidor proxy
proxy_url = 'http://127.0.0.1:8080'  

# Obtén el puerto de los argumentos de la línea de comandos
if len(sys.argv) != 2:
    print("Uso: python main.py <puerto>")
    sys.exit(1)

puerto = int(sys.argv[1])

# Variables para medir la tasa de llegada y tasa de servicio
tiempo_inicio = time.time()
tiempo_pibote = tiempo_inicio
cant_peticiones_intervalo = 0


# cantidad de peticiones totales 
cant_peticiones=0

def report(tiempo_actual):
    global cant_peticiones_intervalo
    global tiempo_pibote
    # intervalo de tiempo en que se hace reporte
    intervalo = 600 # 600 segundos = 10 minutos

    # si aun se esta en el intervalo de 10 minutias de revision se van contando las peticiones y vamos guardando el tiempo piblote
    if tiempo_actual-tiempo_pibote<intervalo:
        cant_peticiones_intervalo+=1
    else:
        tasa_llegada= cant_peticiones_intervalo / (tiempo_actual-tiempo_pibote)
        tiempo_pibote=tiempo_actual
        
        report ={
            "server":f"http:/{request.host}",
            "tasa_llegada":tasa_llegada,
            "cant requests":cant_peticiones_intervalo
        } 

        cant_peticiones_intervalo=0

        # enviamos el reporte al balanceador
        response = requests.get(f'{proxy_url}/report/{report}')
        print(response.json())








@app.route('/')
def info():
    return {
        "hola":"mundo"
    }


@app.route('/conect_proxi')
def conect_proxi():
    global proxy_url
    ip = request.host
    # Envia tu IP al servidor proxy al iniciar
    response = requests.get(f'{proxy_url}/conect/{ip}')
    print("ip enviada")
    return response.json()

@app.route('/<type_request>')
def index(type_request):
    print()
    global cant_peticiones
    cant_peticiones+=1

    # vamos obteniendo datos de rendimiento
    report(time.time())
        
    # Simular diferentes tipos de peticiones con tiempos de respuesta variables
    if type_request == 1:
        # Simular una petición rápida
        time.sleep(1)  # Tiempo de espera corto
        response_data = {"tipo_peticion": "A"}
    elif type_request==2:
        # Simular una petición media
        time.sleep(2)  # Tiempo de espera medio
        response_data = {"tipo_peticion": "B"}
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
