import requests
import time

ports=[5000,5001,5002]

print("\n esperando servers activos ")
time.sleep(10) 

for port in ports:
    response = requests.get(f"http://127.0.0.1:{port}/conect_proxi")
    print(response.json())

print("\n servers conectados ")
time.sleep(5) 
