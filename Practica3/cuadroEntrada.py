#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 12:32:40 2026

@author: Javier Jesús Costa Ruiz-canela
"""

import sys 
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QInputDialog, QApplication

class Example(QWidget): 

    def __init__(self): 
        super().__init__()  
        self.initUI() 

    def initUI(self): 
        self.btn = QPushButton('Introducir', self)  # Crea un botón
        self.btn.move(20, 20)  # Posiciona el botón en (20, 20)
        self.btn.clicked.connect(self.showDialog)  # Conecta el clic del botón con showDialog

        self.le = QLineEdit(self)  # Crea un campo de texto (QLineEdit)
        self.le.move(130, 22)  # Posiciona el campo de texto en (130, 22)

        self.setGeometry(300, 300, 450, 350) 
        self.setWindowTitle('Cuadro de entrada')  
        self.show()  

    def showDialog(self):  # Método que muestra el cuadro de diálogo
        text, ok = QInputDialog.getText(self, 'Cuadro de entrada',  # Abre un cuadro de entrada
                                        'Introduce tu nombre:')  # Muestra un mensaje solicitando el nombre

        if ok:  # Si el usuario presiona "Ok"
            self.le.setText(str(text))  # Muestra el texto ingresado en el campo de texto

def main():
    app = QApplication(sys.argv)  
    ex = Example() 
    sys.exit(app.exec_()) 

if __name__ == '__main__': 
    main() 
