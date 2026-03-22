#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 12:49:11 2026

@author: Javier Jesús Costa Ruiz-canela
"""

import sys 
from PyQt5.QtWidgets import QWidget, QPushButton, QFrame, QColorDialog, QApplication
from PyQt5.QtGui import QColor 

class Example(QWidget): 

    def __init__(self):  
        super().__init__() 
        self.initUI() 

    def initUI(self): 
        col = QColor(0, 0, 0)  # Define el color inicial como negro

        self.btn = QPushButton('Cambiar Color', self)  # Crea un botón
        self.btn.move(20, 20)  # Posiciona el botón en (20, 20)
        self.btn.clicked.connect(self.showDialog)  # Conecta el clic del botón con showDialog

        self.frm = QFrame(self)  # Crea un marco (QFrame)
        self.frm.setStyleSheet("QWidget { background-color: %s }"
                               % col.name())  # Aplica el color inicial negro al marco
        self.frm.setGeometry(130, 22, 200, 200)  # Posiciona y da tamaño al marco

        self.setGeometry(300, 300, 450, 350)
        self.setWindowTitle('Cambiar Color') 
        self.show() 

    def showDialog(self):  # Método que muestra el cuadro de selección de color
        col = QColorDialog.getColor()  # Abre el cuadro de selección de color

        if col.isValid():  # Si el usuario seleccionó un color válido
            self.frm.setStyleSheet("QWidget { background-color: %s }"
                                   % col.name())  # Cambia el fondo al color seleccionado

def main():
    app = QApplication(sys.argv)  
    ex = Example() 
    sys.exit(app.exec_()) 

if __name__ == '__main__': 
    main() 