import requests
import time
import os 
import random




servers = ["http://127.0.0.1:8080","http://127.0.0.1:5000","http://127.0.0.1:5001","http://127.0.0.1:5002"]

s = 1

print("servers")
for server in servers:
    print(s,"->",server)
    s+=1
server=int(input("donde se haran las peticiones:"))


# info peticiones
info_requests = {
    "A":0,
    "B":0,
    "C":0
}


def limited_request():
    tiempos_de_respuesta = []
    peticiones = int(input("Número de peticiones: "))
    inicio_peticiones = time.time()
    for i in range(peticiones):
        print("Peticiónes:", i + 1)
        type_request= random.randint(1,3)
        if type_request==1:
            info_requests["A"]+=1
        elif type_request==2:
            info_requests["B"]+=1
        else:
            info_requests["C"]+=1
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

    for k,v in info_requests.items():
        print(k,":",v)



def serial_requests():
    while True:
        type_request = random.randint(1,3)
        response = requests.get(f"{servers[server-1]}/{type_request}")

        

print(" tipo de test a probar")
print("1-> peticones finitas")
print("2-> peticones infinitas y reporte de rendimiento")

test= int(input("------->"))



if test==1:
    limited_request()
else:
    serial_requests()



