#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 17:51:58 2026

@author: Javier Jesús Costa Ruiz-canela
"""


import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        qbtn = QPushButton('Salir', self) # Creamos un botón con el texto "Salir"
        qbtn.clicked.connect(QApplication.instance().quit) # Conectamos el clic a la función para salir
        qbtn.resize(qbtn.sizeHint()) # Ajustamos el tamaño del botón
        qbtn.move(50, 50) # Movemos el botón dentro de la ventana

        self.setGeometry(300, 300, 350, 250) # Asignamos posición y tamaño de la ventana
        self.setWindowTitle('Cerrar Ventana') # Nombramos el título de la ventana
        self.show() # Mostramos la ventana


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
