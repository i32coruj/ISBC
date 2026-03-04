#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 16:39:43 2026

@author: Javier Jesús Costa Ruiz-canela
"""

import sys
from PyQt5.QtWidgets import QMainWindow, qApp, QMenu, QApplication

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menu Contextual')
        self.show()

    def contextMenuEvent(self, event):  # Método para manejar eventos de menú contextual
        cmenu = QMenu(self)  # Creamos un menú contextual

        # Agregamos opciones al menú
        newAct = cmenu.addAction("Nuevo")  
        openAct = cmenu.addAction("Abrir")  
        quitAct = cmenu.addAction("Salir")  

        action = cmenu.exec_(self.mapToGlobal(event.pos()))  # Mostramos el menú en la posición del cursor

        if action == quitAct:  # Si se selecciona la opción "Salir"
            qApp.quit()  # Cerramos la aplicación

def main():
    app = QApplication(sys.argv)  
    ex = Example()  
    sys.exit(app.exec_())  

if __name__ == '__main__':
    main()  