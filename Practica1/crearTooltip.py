#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 12:52:44 2026

@author: Javier Jesús Costa Ruiz-canela
"""

# Importamos los módulos
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication)
from PyQt5.QtGui import QFont # Para modificar la fuente


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI() # Iniciamos la interfaz


    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10)) # Establecemos la fuente

        self.setToolTip('Hola, soy un <b>QWidget</b>')  # Tooltip para la ventana

        btn = QPushButton('Botón', self)   # Creamos un botón
        btn.setToolTip('Yo soy un <b>QPushButton</b>')   # Tooltip para el botón
        btn.resize(btn.sizeHint()) # Ajustamos el tamaño del botón según su contenido
        btn.move(50, 50)  # Movemos el botón dentro de la ventana

        self.setGeometry(300, 300, 300, 200) # Asignamos posición y tamaño de la ventana
        self.setWindowTitle('CrearTooltips')  # Asignamos un título
        self.show() # Enseñamos la ventana
 

def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
