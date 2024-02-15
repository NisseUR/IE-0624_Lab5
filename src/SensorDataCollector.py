#!/usr/bin/python3

# Para leer datos de aceleración y giroscopio 
# desde el puerto serie, procesarlos y guardarlos en un archivo CSV

import serial
import csv

# Obtener el nombre del archivo CSV del usuario
csv_filename = input("Ingrese el nombre del archivo CSV a generar: ")

# Open a csv file and set it up to receive comma delimited input
logging = open(csv_filename, 'w', newline='')
writer = csv.writer(logging)


# Puerto serial de la placa
# serial_port = '/dev/ttyACM0'  # puerto de la placa
serial_port = 'COM4'  # puerto placa a PC
baudrate = 9600  # Velocidad de baudios del puerto serie

conexion_serial = serial.Serial(serial_port, baudrate)  # Iniciar conexión serial
conexion_serial.flushInput()

#Write out a single character encoded in utf-8; this is defalt encoding for Arduino serial comms
#This character tells the Arduino to start sending data
conexion_serial.write(bytes('x', 'utf-8'))

data = []  # Lista para almacenar los datos recopilados

try:
    while True:
        if conexion_serial.in_waiting > 0:
            linea = conexion_serial.readline().decode('utf-8').strip()
            print(linea) # Para ver en terminal el movimiento

            #Write received data to CSV file
            values = linea.split(',')
            writer.writerow(values)

except KeyboardInterrupt:
    print("\nInterrupción por el usuario. Guardando datos...")


# Close port and CSV file to exit
conexion_serial.close()
logging.close()
print(f"Datos guardados en '{csv_filename}'.")
