#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 12:18:57 2026

@author: Javier Jesús Costa Ruiz-canela
"""

import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI() # Inicializar la interfaz de usuario

    def initUI(self):

        self.setGeometry(300, 300, 250, 150) # Posición y tamaño de la ventana
        self.setWindowTitle('Crear mensaje al cerrar') # Título de la ventana
        self.show() # Mostrar la ventana

    def closeEvent(self, event):
        # Se muestra un cuadro de diálogo con una pregunta de confirmación
        reply = QMessageBox.question(self, 'Mensaje',
                                     "¿Estás seguro de querer salir?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:

            event.accept() # Si el usuario acepta, cierra la ventana
        else:

            event.ignore() # Si el usuario cancela, se ignora el evento y no se cierra


def main():
    app = QApplication(sys.argv) # Crea la aplicación PyQt
    ex = Example() # Instancia la clase Example
    sys.exit(app.exec_()) # Inicia el ciclo de eventos y espera a que se cierre la app
 

if __name__ == '__main__':
    main() # Ejecuta la función main cuando el script se ejecuta
