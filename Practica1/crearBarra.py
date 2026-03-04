#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 13:26:02 2026

@author: Javier Jesús Costa Ruiz-canela
"""

# Importamos los módulos necesarios
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

class Example(QMainWindow): # Definimos una clase que hereda de QMainWindow

    def __init__(self):
        super().__init__()  # Llamamos al constructor de la clase padre

        self.initUI()  # Inicializamos la interfaz de usuario

    def initUI(self):
        self.statusBar().showMessage('Listo')  # Creamos la barra de estado y muestra el mensaje "Listo"

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Crear Barra Status')
        self.show()

def main():  # Funcion principal que ejecuta la aplicación.
    app = QApplication(sys.argv)  # Creamos la aplicación con los argumentos del sistema
    ex = Example()  # Instanciamos la clase Example
    sys.exit(app.exec_())  # Ejecutamos la aplicación hasta que se cierre

if __name__ == '__main__':
    main()