import requests
import time
import os 
import random

peticiones = int(input("Número de peticiones: "))

servers = ["http://127.0.0.1:8080","http://127.0.0.1:5000","http://127.0.0.1:5001","http://127.0.0.1:5002"]

s = 1

print("servers")
for server in servers:
    print(s,"->",server)
    s+=1
server=int(input("donde se haran las peticiones:"))

tiempos_de_respuesta = []

inicio_peticiones = time.time()
for i in range(peticiones):
    print("Peticiónes:", i + 1)
    type_request= random.randint(1,3)
    inicio = time.time()
    response = requests.get(f"{servers[server-1]}/{type_request}")
    fin = time.time()
    tiempo_de_respuesta = fin - inicio
    tiempos_de_respuesta.append(tiempo_de_respuesta)

    os.system('cls')
fin_peticiones = time.time()
    

print("Peticiones recibidas:", peticiones)
print("server solicitado:", servers[server-1])

# Calcular estadísticas
tiempo_promedio = sum(tiempos_de_respuesta) / len(tiempos_de_respuesta)
tiempo_maximo = max(tiempos_de_respuesta)
tiempo_minimo = min(tiempos_de_respuesta)
tiempo_general_ejecucion = fin_peticiones - inicio_peticiones

print("Tiempo que tomaron todas las peticiones:", tiempo_general_ejecucion, "segundos")
print("Tiempo promedio de respuesta:", tiempo_promedio, "segundos")
print("Tiempo máximo de respuesta:", tiempo_maximo, "segundos")
print("Tiempo mínimo de respuesta:", tiempo_minimo, "segundos")
