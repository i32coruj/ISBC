#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 16:14:13 2026

@author: javi
"""

# Importamos los módulos necesarios
import sys  # Módulo para interactuar con el sistema.
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication  # Clases de PyQt5.
from PyQt5.QtGui import QIcon  # QIcon para usar íconos.

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAct = QAction(QIcon('salir.png'), '&Salir', self)  # Creamos una acción con un ícono y etiqueta 'Salir'
        exitAct.setShortcut('Ctrl+Q')  # Asignamos un atajo de teclado (Ctrl+Q) para salir
        exitAct.setStatusTip('Salir de la app')  # Agregamos una descripción
        exitAct.triggered.connect(qApp.quit)  # Conectamos la acción al método quit() para cerrar la app

        self.statusBar()  # Creamos la barra de estado

        menubar = self.menuBar()  # Creamos la barra de menú
        fileMenu = menubar.addMenu('&Funciones')  # Agregamos un menú en la barra
        fileMenu.addAction(exitAct)  # Agrega la opción de salida al menú

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menu Simple')
        self.show() 

def main():
    app = QApplication(sys.argv)  # Creamos la aplicación
    ex = Example()  # Instanciamos la clase Example
    sys.exit(app.exec_())  # Ejecutamos la aplicacion

if __name__ == '__main__':
    main()
