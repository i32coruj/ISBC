#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 12:54:12 2026

@author: Javier Jesús Costa Ruiz-canela
"""


import sys  
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton,
                             QSizePolicy, QLabel, QFontDialog, QApplication)

class Example(QWidget): 

    def __init__(self): 
        super().__init__()  
        self.initUI() 

    def initUI(self):  
        vbox = QVBoxLayout()  # Crea un diseño vertical para los widgets

        btn = QPushButton('Cambiar Fuente', self)
        btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)  
        btn.move(20, 20)
        vbox.addWidget(btn)

        btn.clicked.connect(self.showDialog)

        self.lbl = QLabel('Esto es una frase de ejemplo', self)
        self.lbl.move(130, 20)  # Posiciona la etiqueta en (130, 20)

        vbox.addWidget(self.lbl)  # Agrega la etiqueta al diseño
        self.setLayout(vbox)  # Aplica el diseño a la ventana

        self.setGeometry(300, 300, 450, 350)  
        self.setWindowTitle('Cambiar tipo de letra')  
        self.show()  

    def showDialog(self):  # Método que muestra el cuadro de selección de fuente
        font, ok = QFontDialog.getFont()  # Abre el cuadro de diálogo de fuente

        if ok:  # Si el usuario selecciona una fuente y presiona "Ok"
            self.lbl.setFont(font)  # Aplica la fuente seleccionada a la etiqueta

def main():
    app = QApplication(sys.argv) 
    ex = Example() 
    sys.exit(app.exec_())  

if __name__ == '__main__': 
    main() 
