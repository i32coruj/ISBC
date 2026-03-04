#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 16:33:57 2026

@author: Javier Jesús Costa Ruiz-canela
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusbar = self.statusBar()  # Creamos la barra de estado
        self.statusbar.showMessage('Listo')  # Mostramos un mensaje en la barra de estado

        menubar = self.menuBar()  # Creamos la barra de menú
        viewMenu = menubar.addMenu('Funciones')  # Agregamos un menú

        # Creamos una acción checkable (puede activarse y desactivarse)
        viewStatAct = QAction('Ver Barra de Estado', self, checkable=True)
        viewStatAct.setStatusTip('Estás viendo la barra de estado')  # Establecemos un mensaje de estado
        viewStatAct.setChecked(True)  # Inicialmente la opción está activada
        viewStatAct.triggered.connect(self.toggleMenu)  # Conectamos la acción a una función

        viewMenu.addAction(viewStatAct)  # Agregamos la acción al menú

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Check menu')
        self.show()

    def toggleMenu(self, state):  # Función que alterna la visibilidad de la barra de estado
        if state:
            self.statusbar.show()  # Si está activado, mostramos la barra de estado
        else:
            self.statusbar.hide()  # Si está desactivado, ocultamos la barra de estado

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

