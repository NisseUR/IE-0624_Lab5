#!/usr/bin/python3

# para leer datos de aceleración y giroscopio 
# desde el puerto serie, procesarlos y guardarlos en un archivo CSV

import serial
import csv

# Puerto serial de la placa
serial_port = '/dev/ttyACM0'  # puerto de la placa
baudrate = 9600  # Velocidad de baudios del puerto serie

conexion_serial = serial.Serial(serial_port, baudrate)  # Iniciar conexión serial

data = []  # Lista para almacenar los datos recopilados

try:
    while True:
        if conexion_serial.in_waiting > 0:
            linea = conexion_serial.readline().decode('utf-8').strip()

            valores = linea.split(' | ')[1:]  # Divide en 'Acceleration:' y 'Gyro:'
            valores = [v.split(': ')[1] for v in valores]  # Se extraen los valores después de 'Acceleration:' y 'Gyro:'
            valores = [item for sublist in [v.split(', ') for v in valores] for item in sublist]  # Aplana la lista
            if len(valores) == 6:  # Para asegurar de que se recibieron todos los valores esperados
                data.append(valores)
except KeyboardInterrupt:
    print("\nInterrupción por el usuario. Guardando datos...")

# Obtener el nombre del archivo CSV del usuario
csv_filename = input("Ingrese el nombre del archivo CSV a generar: ")

# Guardar datos en CSV
with open(csv_filename, 'w', newline='') as file:
    escritor = csv.writer(file)
    escritor.writerow(["Aceleracion_X", "Aceleracion_Y", "Aceleracion_Z", "Giro_X", "Giro_Y", "Giro_Z"])  # Escribir los encabezados
    escritor.writerows(data)  # Escribir los datos

print(f"Datos guardados en '{csv_filename}'.")
conexion_serial.close()
