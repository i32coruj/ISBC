#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 13:30:31 2026

@author: Javier Jesús Costa Ruiz-canela
"""

from PyQt5.QtWidgets import QWidget, QSlider, QLabel, QApplication
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QPixmap
import sys 

class Example(QWidget):  

    def __init__(self): 
        super().__init__() 
        self.initUI()  

    def initUI(self): 
        sld = QSlider(Qt.Horizontal, self)  # Creamos un QSlider en orientación horizontal
        sld.setFocusPolicy(Qt.NoFocus)  # Establecemos la política de foco
        sld.setGeometry(30, 40, 200, 30)  # Establecemos la geometría del slider
        sld.valueChanged[int].connect(self.changeValue)  # Conectamos el cambio de valor a un método

        self.label = QLabel(self)  # Creamos un QLabel para mostrar una imagen
        self.label.setPixmap(QPixmap('mute.png'))  # Establecemos una imagen de mute como predeterminada
        self.label.setGeometry(250, 40, 80, 30)  # Establecemos la geometría del QLabel

        self.setGeometry(300, 300, 350, 250) 
        self.setWindowTitle('Controlar Volumen') 
        self.show() 

    def changeValue(self, value):  # Método que cambia la imagen basada en el valor del slider
        if value == 0:
            self.label.setPixmap(QPixmap('mute.png'))  # Muestra imagen mute
        elif 0 < value <= 30:
            self.label.setPixmap(QPixmap('min.png'))  # Muestra imagen de volumen bajo
        elif 30 < value < 70:
            self.label.setPixmap(QPixmap('medium.png'))  # Muestra imagen de volumen medio
        else:
            self.label.setPixmap(QPixmap('max.png'))  # Muestra imagen de volumen máximo

def main():
    app = QApplication(sys.argv) 
    ex = Example()  
    sys.exit(app.exec_())  

if __name__ == '__main__':
    main() 