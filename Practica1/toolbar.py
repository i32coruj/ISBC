#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 16:48:26 2026

@author: Javier Jesús Costa Ruiz-canela
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon  # Importamos QIcon para los iconos

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # Creamos una acción con un icono y un atajo de teclado
        exitAct = QAction(QIcon('salir.png'), 'Salir', self)
        exitAct.setShortcut('Ctrl+Q')  # Asignamos un atajo de teclado
        exitAct.triggered.connect(qApp.quit)  # Conectamos la acción a la función de salida

        self.toolbar = self.addToolBar('Salir')  # Creamos la barra de herramientas
        self.toolbar.addAction(exitAct)  # Agregamos la acción a la barra

        self.setGeometry(300, 300, 300, 200)  
        self.setWindowTitle('Barra de Herramientas')  
        self.show()  

def main():
    app = QApplication(sys.argv)  
    ex = Example()  
    sys.exit(app.exec_())  

if __name__ == '__main__':
    main()  