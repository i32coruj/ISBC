#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 12:39:53 2026

@author: Javier Jesús Costa Ruiz-canela
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox

def saludar():
    # Este es el 'Slot': la función que responde al evento
    mensaje = QMessageBox()
    mensaje.setText("¡HOLA!")
    mensaje.exec_()

# 1. Instanciar la aplicación (esto arranca el Gestor de Eventos de fondo)
app = QApplication(sys.argv)

# 2. Crear la interfaz
ventana = QWidget()
ventana.setWindowTitle('Mi primera conexión')
layout = QVBoxLayout()

boton = QPushButton('Haz clic aquí')

# --- LA CLAVE DEL GESTOR DE EVENTOS ---
# Aquí conectamos el evento 'clicked' con nuestra función 'saludar'
boton.clicked.connect(saludar)
# --------------------------------------

layout.addWidget(boton)
ventana.setLayout(layout)
ventana.show()

# 3. Ejecutar el bucle de eventos (el programa se queda aquí "escuchando")
sys.exit(app.exec_())