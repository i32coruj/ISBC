#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 19:07:19 2026

@author: Javier Jesús Costa Ruiz-canela
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150) 
        self.setWindowTitle('Manejador Eventos')
        self.show()  

    def keyPressEvent(self, e):  # Método que maneja eventos de teclado
        if e.key() == Qt.Key_Escape:  # Si la tecla presionada es "Escape"
            self.close()  # Cierra la aplicación


def main():
    app = QApplication(sys.argv) 
    ex = Example() 
    sys.exit(app.exec_()) 


if __name__ == '__main__':
    main()
