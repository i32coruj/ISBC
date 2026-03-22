#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 13:07:01 2026

@author: Javier Jesús Costa Ruiz-canela
"""

from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication 
from PyQt5.QtCore import Qt  
import sys 

class Example(QWidget): 

    def __init__(self): 
        super().__init__()  
        self.initUI()  

    def initUI(self): 
        cb = QCheckBox('Ver título', self)  # Creamos un checkbox con "Ver título"
        cb.move(20, 20)  # Movemos el checkbox a una posición específica
        cb.toggle()  # Establecemos el estado inicial como activado
        cb.stateChanged.connect(self.changeTitle)  # Conectamos la señal de cambio de estado al método changeTitle

        self.setGeometry(300, 300, 350, 250) 
        self.setWindowTitle('CheckBox') 
        self.show() 

    def changeTitle(self, state):  # Método que cambia el título de la ventana basado en el estado del checkbox
        if state == Qt.Checked:  # Si el estado es activado
            self.setWindowTitle('CheckBox')  
        else:  # Si el estado es desactivado
            self.setWindowTitle(' ')  # Dejamos el título vacío

def main():
    app = QApplication(sys.argv)  
    ex = Example() 
    sys.exit(app.exec_()) 

if __name__ == '__main__': 
    main() 
