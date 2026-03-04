#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 13:00:57 2026

@author: Javier Jesús Costa Ruiz-canela 
"""


# Importamos los módulos necesarios
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox


class Example(QWidget):  # Definimos una clase que hereda de QWidget

    def __init__(self):  # Constructor de la clase
        super().__init__()  # Llamamos  al constructor de la clase padre (QWidget)
        self.initUI()  # Llamamos al metodo que inicializa la interfaz gráfica

    def initUI(self):  # Método para configurar la ventana
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('Detectar Clics')
        self.show()

    def mousePressEvent(self, event):  # Método que maneja eventos de clic del mouse
        x, y = event.x(), event.y()  # Obtenemos las coordenadas (x, y) del clic
        QMessageBox.information(self, "Clic detectado", f"Has hecho clic en ({x}, {y})")  # Muestramos la posición

def main():
    app = QApplication(sys.argv) 
    ex = Example() 
    sys.exit(app.exec_()) 

if __name__ == '__main__':
    main()  # Llama a la función principal


if __name__ == '__main__':
    main()