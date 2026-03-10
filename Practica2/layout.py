#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 18:52:26 2026

@author: Javier Jesús Costa Ruiz-canela
"""

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Creamos dos botones con los textos "OK" y "Cancel"
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        # Creamos un layout horizontal
        hbox = QHBoxLayout()
        hbox.addStretch(1)  # Añadimos un espacio flexible para empujar los botones a la derecha
        hbox.addWidget(okButton)  # Añadimos el botón "OK"
        hbox.addWidget(cancelButton)  # Añadimos el botón "Cancel"

        # Creamos un layout vertical
        vbox = QVBoxLayout()
        vbox.addStretch(1)  # Añadimos un espacio flexible para empujar los botones hacia abajo
        vbox.addLayout(hbox)  # Añadimos el layout horizontal al layout vertical

        self.setLayout(vbox)  # Establecemos el layout principal de la ventana

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Botones')
        self.show()

def main():
    app = QApplication(sys.argv)
    ex = Example() 
    sys.exit(app.exec_()) 

if __name__ == '__main__':
    main()
