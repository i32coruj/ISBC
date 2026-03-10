#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 19:15:27 2026

@author: Javier Jesús Costa Ruiz-canela
"""

import sys  
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication  

class Example(QMainWindow):  

    def __init__(self):  
        super().__init__() 
        self.initUI() 

    def initUI(self):  # Método para configurar la interfaz gráfica
        btn1 = QPushButton("Botón 1", self)  # Crea un botón
        btn1.move(30, 50)  # Posiciona el botón en (30, 50)

        btn2 = QPushButton("Botón 2", self)  # Crea otro botón
        btn2.move(150, 50)  # Posiciona el botón en (150, 50)

        btn1.clicked.connect(self.buttonClicked)  # Conecta el clic del botón 1 con el método "buttonClicked"
        btn2.clicked.connect(self.buttonClicked)  # Conecta el clic del botón 2 con el mismo método

        self.statusBar()  # Crea una barra de estado en la ventana

        self.setGeometry(300, 300, 450, 350) 
        self.setWindowTitle('¿Qué botón se ha presionado?') 
        self.show() 

    def buttonClicked(self):  # Método que se ejecuta cuando se presiona un botón
        sender = self.sender()  # Obtiene el botón que envió la señal
        self.statusBar().showMessage(sender.text() + ' se ha pulsado')  # Muestra en la barra de estado qué botón fue presionado

def main():
    app = QApplication(sys.argv)  
    ex = Example() 
    sys.exit(app.exec_()) 

if __name__ == '__main__': 
    main() 
