#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 19:04:44 2026

@author: Javier Jesús Costa Ruiz-canela
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication


class Example(QWidget):

    def __init__(self): 
        super().__init__() 
        self.initUI()  

    def initUI(self): 

        lcd = QLCDNumber(self)  # Crea un widget LCD para mostrar números
        sld = QSlider(Qt.Horizontal, self)  # Crea un slider horizontal

        vbox = QVBoxLayout()  # Crea un diseño vertical (VBox)
        vbox.addWidget(lcd)  # Agrega el LCD al layout
        vbox.addWidget(sld)  # Agrega el slider al layout

        self.setLayout(vbox)  # Establece el layout en la ventana
        sld.valueChanged.connect(lcd.display)  # Conecta la señal del slider con el método "display"

        self.setGeometry(300, 300, 250, 150) 
        self.setWindowTitle('Eventos y señales') 
        self.show()

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()