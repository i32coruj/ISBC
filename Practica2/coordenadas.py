#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 19:11:35 2026

@author: Javier Jesús Costa Ruiz-canela
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()  # Crea un diseño de cuadrícula

        x = 0
        y = 0
        self.text = f'x: {x},  y: {y}'  # Texto inicial con coordenadas (0,0)

        self.label = QLabel(self.text, self)  # Crea una etiqueta para mostrar coordenadas
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)  # Agrega la etiqueta al layout

        self.setMouseTracking(True)  # Habilita el seguimiento del ratón

        self.setLayout(grid)  # Establece el layout

        self.setGeometry(300, 300, 450, 300)
        self.setWindowTitle('Coordenadas Mouse')
        self.show()

    def mouseMoveEvent(self, e):  # Captura el movimiento del ratón
        x = e.x()  # Obtiene la coordenada X
        y = e.y()  # Obtiene la coordenada Y

        text = f'x: {x},  y: {y}'  # Formatea el texto con nuevas coordenadas
        self.label.setText(text)  # Actualiza el texto en la etiqueta

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
