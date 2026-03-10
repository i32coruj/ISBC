#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 19:18:39 2026

@author: Javier Jesús Costa Ruiz-canela
"""

import sys 
from PyQt5.QtCore import pyqtSignal, QObject 
from PyQt5.QtWidgets import QMainWindow, QApplication  

class Communicate(QObject):  # Define una clase que hereda de QObject
    closeApp = pyqtSignal()  # Define una señal personalizada llamada "closeApp"

class Example(QMainWindow): 

    def __init__(self): 
        super().__init__()  
        self.initUI()  

    def initUI(self): 
        self.c = Communicate()  # Crea una instancia de la clase Communicate
        self.c.closeApp.connect(self.close)  # Conecta la señal "closeApp" con el método "close()"

        self.setGeometry(300, 300, 450, 350) 
        self.setWindowTitle('Cerrar con clic')  
        self.show()  

    def mousePressEvent(self, event):  # Método que maneja el evento de clic del mouse
        self.c.closeApp.emit()  # Emite la señal "closeApp", cerrando la aplicación

def main():
    app = QApplication(sys.argv)  
    ex = Example() 
    sys.exit(app.exec_()) 

if __name__ == '__main__': 
    main() 
