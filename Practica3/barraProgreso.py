#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 13:33:12 2026

@author: Javier Jesús Costa Ruiz-canela
"""

from PyQt5.QtWidgets import QWidget, QProgressBar, QPushButton, QApplication
from PyQt5.QtCore import QBasicTimer 
import sys 

class Example(QWidget): 

    def __init__(self): 
        super().__init__()  
        self.initUI()  

    def initUI(self):  
        self.pbar = QProgressBar(self)  # Creamos un widget QProgressBar
        self.pbar.setGeometry(30, 40, 200, 25)  # Establecemos la posición y tamaño de la barra de progreso

        self.btn = QPushButton('Empezar', self)  # Creamos un botón para iniciar y detener el progreso
        self.btn.move(40, 80)  # Establecemos la posición del botón
        self.btn.clicked.connect(self.doAction)  # Conectamos el clic del botón con el método 'doAction'

        self.timer = QBasicTimer()  # Creamos un temporizador básico
        self.step = 0  # Establecemos el valor inicial del progreso

        self.setGeometry(300, 300, 280, 170) 
        self.setWindowTitle('Barra de progreso') 
        self.show()  

    def timerEvent(self, e):  # Método que se llama cada vez que se activa el temporizador
        if self.step >= 100:  # Si el progreso llega al 100%
            self.timer.stop()  # Detenemos el temporizador
            self.btn.setText('Detener') 
            return  # Salimos del método

        self.step = self.step + 1  # Incrementamos el progreso en 1
        self.pbar.setValue(self.step)  # Actualizamos el valor de la barra de progreso

    def doAction(self):  # Método que maneja el botón para iniciar/detener el progreso
        if self.timer.isActive():  # Si el temporizador está activo
            self.timer.stop()  # Detenemos el temporizador
            self.btn.setText('Empezar')
        else:  # Si el temporizador no está activo
            self.timer.start(100, self)  # Iniciamos el temporizador con un intervalo de 100 ms
            self.btn.setText('Detener')  

def main(): 
    app = QApplication(sys.argv) 
    ex = Example() 
    sys.exit(app.exec_()) 

if __name__ == '__main__': 
    main() 
