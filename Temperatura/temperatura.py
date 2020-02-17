#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Nombre: temperatura.py.py 
Creador: MICROSIDE TECHNOLOGY S.A de C.V /  
Fecha: Febrero 2020
Resumen: Codigo que conecta un sensor de Humedad del modulo XIDE 
         por medio de GPIO en Raspberry.
'''

#Librería para poder realizar interfaz grafica
from Tkinter import * 
#Librería para utilizar el GPIO 
import RPi.GPIO as GPIO
#Librería para poder utilizar el puerto serial 
import serial
#Librería para poder utilizar timers                                        
import threading 
#Librería para controlar lapsos de tiempo                                   
import time
#Librería para utilización de esquemas numéricos 
import numpy as np 

'''
Se crea la variable Raiz para tener una ventana
donde viualizar los datos, el título será "Temperatura"
y tendra un tamaño de 250 x 60 píxeles
'''

RAIZ = Tk() 
RAIZ.title("Temperatura")
RAIZ.geometry('250x60')


'''
La variable puerto obtendrá el puerto por el cual esta conectado el dispositivo 
con su configuración.
'''
puerto= serial.Serial(port = '/dev/ttyS0', 
                         baudrate = 9600,
                         bytesize = serial.EIGHTBITS,
                         parity   = serial.PARITY_NONE,
                         stopbits = serial.STOPBITS_ONE)
dato = 0
salto = "\n\r"
orden="T"


'''
Se crean todos los elementos que se mostrarán en la ventana,
la variable etiqueta sólo tendra  el texto "Valor de la temperatura en grados centigrados es",
la variable etiqueta1 cambiará su valor dependiendo del valor obtenido 
del sensor.
'''                                         
etiqueta = Label(RAIZ, text="Valor de la temperatura en\ngrados centigrados es:") 
etiqueta.grid(column=4, row=5)
etiqueta1 = Label(RAIZ, text="")
etiqueta1.grid(column=6, row=5)
#Define en que tiempo y que función sera ejecutada con timer
timer = threading.Timer(1.1,fun)                            
#Inicia el temporizador    
timer.start()
#Se inicia todo el programa 
RAIZ.mainloop()

#-------- Funciones a utilizar ------------

def fun():

    while True:
         if (orden is "T"):
                
                puerto.write(orden.encode())
                time.sleep(0.1)
                puerto.write(salto.encode())
                time.sleep(0.1)
                dato = puerto.readline()
                dato = np.fromstring(dato.decode('ascii', errors = 'replase'), sep = ' ') 
                etiqueta1.config(text= dato[0]) 
         #fin if order is T
    #fin de while true
