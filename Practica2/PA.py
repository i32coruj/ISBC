#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 18:13:20 2026

@author: Javier Jesús Costa Ruiz-canela
"""

# Importamos los módulos necesarios
import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Creamos una etiqueta con el texto "ZetCode" y la agregamos a la ventana
        lbl1 = QLabel('ZetCode', self)
        lbl1.move(15, 10)  # La movemos a la posición (15, 10)

        # Creamos una segunda etiqueta con el texto "tutorials"
        lbl2 = QLabel('tutorials', self)
        lbl2.move(35, 40)  # La movemos a la posición (35, 40)

        # Creamos una tercera etiqueta con el texto "for programmers"
        lbl3 = QLabel('for programmers', self)
        lbl3.move(55, 70)  # La movemos a la posición (55, 70)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Posicionamiento Absoluto')
        self.show()

def main():
    app = QApplication(sys.argv) 
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()