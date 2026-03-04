#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 13:03:50 2026

@author: Javier Jesús Costa Ruiz-canela
"""

# Importamos los módulos necesarios
import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(250, 150)
        self.center()
        self.setWindowTitle('Centrar')
        self.show()

    def center(self):
        qr = self.frameGeometry()  # Obtenemos el tamaño de la ventana
        cp = QDesktopWidget().availableGeometry().center()  # Centro de la pantalla
        qr.moveCenter(cp)  # Movemos el cuadro de la ventana al centro de la pantalla
        self.move(qr.topLeft())  # Movemos la esquina superior izquierda de la ventana

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
