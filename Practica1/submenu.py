#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 16:29:02 2026

@author: Javier Jesús Costa Ruiz-canela
"""

# Importamos los módulos necesarios
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        menubar = self.menuBar()  # Creamos la barra de menú
        fileMenu = menubar.addMenu('Funciones')  # Agregamos el menú

        impMenu = QMenu('Subir', self)  # Creamos un submenú
        impAct = QAction('Subir correo', self)  # Creamos una acción
        impMenu.addAction(impAct)  # Agregamos la acción al submenú

        newAct = QAction('Nuevo', self)  # Creamos una acción

        fileMenu.addAction(newAct)  # Agregamos la acción "Nuevo" al menú principal
        fileMenu.addMenu(impMenu)  # Agregamos el submenú "Subir" al menú principal

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Submenu')
        self.show()

def main():
    app = QApplication(sys.argv)  # Crea la aplicación
    ex = Example()  # Instancia la clase Example
    sys.exit(app.exec_())  # Ejecuta la aplicación

if __name__ == '__main__':
    main()
    