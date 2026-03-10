#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 18:55:57 2026

@author: Javier Jesús Costa Ruiz-canela
"""

import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()  # Creamos un layout de tipo grid
        self.setLayout(grid)  # Establecemos el grid como layout de la ventana

        # Definimos los nombres de los botones de la calculadora
        names = ['Cls', 'Bck', '', 'Cerrar',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        # Creamos una lista de posiciones para los botones
        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):  # Iteramos sobre las posiciones y los nombres
            if name == '':  # Si el nombre está vacío, lo ignoramos
                continue
            button = QPushButton(name)  # Creamos un botón
            grid.addWidget(button, *position)  # Añadimos el botón a la celda correspondiente

        self.move(300, 150)
        self.setWindowTitle('Calculadora')
        self.show()

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()