# Monitor Concurrente de Sensores

Este proyecto simula tres sensores industriales (temperatura, presión y flujo) que funcionan de forma concurrente usando hilos (`threading`) en Python.

## Archivos incluidos

- `monitor.py`: Código fuente con sensores concurrentes.
- `Parte_Práctica_Programación_Concurrente.docx`: Documento explicativo de la parte práctica.
- `Conclusiones_y_Bibliografía.docx`: Conclusiones y referencias bibliográficas.

## Ejecución

Requiere Python 3.x. Para ejecutar el sistema:



import threading
import time
import random
import queue

datos_sensor = queue.Queue()

class Sensor(threading.Thread):
    def __init__(self, nombre, intervalo):
        super().__init__()
        self.nombre = nombre
        self.intervalo = intervalo
        self.daemon = True

def run(self):
        while True:
            valor = round(random.uniform(20.0, 100.0), 2)
            tiempo_actual = time.strftime('%H:%M:%S')
            datos_sensor.put((self.nombre, valor, tiempo_actual))
            time.sleep(self.intervalo)

def monitor_datos():
    while True:
        if not datos_sensor.empty():
            nombre, valor, timestamp = datos_sensor.get()
            print(f"[{timestamp}] Sensor {nombre}: {valor}")
        time.sleep(0.5)

sensor_temp = Sensor("Temperatura", 2)
sensor_pres = Sensor("Presión", 3)
sensor_flujo = Sensor("Flujo", 4)

sensor_temp.start()
sensor_pres.start()
sensor_flujo.start()

monitor_datos()
