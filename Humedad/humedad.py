“””
AUTOR: MICROSIDE TECHNOLOGY S.A. DE C.V.

FECHA: AGOSTO 2019

**************************************************************************

Esta practica consiste en realizar la medicion de Humedad por medio del sensor
incluido en modulo XENSE.

**************************************************************************
“””

from Tkinter import *                             #Libreria para poder realizar interfaz grafica
import RPi.GPIO as GPIO                     # libreria para poder utilizar los GPIO de la raspberry pi
import serial                                          # librera para poder utilizar el puerto serial
import threading                                    # libreria para poder utilizar timers
import time                                                 # libreria de tiempo
import numpy as np                             #libreria para utilizacion de esquemas numericos


RAIZ = Tk()                                          #se crea la variable RAIZ para toda la interfaz y se llama la clase TK()

RAIZ.title(“Humedad”                            # Definimos el nombre de la interfaz

RAIZ.geometry(‘250×60’)                         # Definimos el tamano de la interfaz


puerto= serial.Serial(port = ‘/dev/ttyS0’,                   #escribe el nombre del puerto al que esta conectado el dispositivo
baudrate = 9600,
bytesize = serial.EIGHTBITS,
parity = serial.PARITY_NONE,
stopbits = serial.STOPBITS_ONE)

dato = 0
salto = “\\\\\r”
orden=”H”
def fun():
    while True:
       if (orden is “H”):
       #reset_output_buffer()
       puerto.write(orden.encode())
       time.sleep(0.1)
       puerto.write(salto.encode())
       time.sleep(0.1)
       #reset_input_buffer()
       dato = puerto.readline()
       dato = np.fromstring(dato.decode(‘ascii’, errors = ‘replase’), sep = ‘ ‘)   #convierte los valores para poder utilizarlos como enteros

       etiqueta1.config(text= dato[0])



etiqueta = Label(RAIZ, text=”Valor de la Humedad es:”)
etiqueta.grid(column=4, row=5)

etiqueta1 = Label(RAIZ, text=””)                               #etiqueta de tipo label que nos muestra el valor dela humedad
etiqueta1.grid(column=6, row=5)

timer = threading.Timer(1.1,fun)                               # Activa la funcion led en un tiempo de 0.5 segundos
timer.start()

RAIZ.mainloop()