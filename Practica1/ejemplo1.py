#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 12:52:19 2026

@author: Javier Jesús Costa Ruiz-canela
"""

# Importamos los módulos necesarios
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtCore import Qt


class Example(QWidget):  # Definimos una clase que hereda de QWidget (ventana básica)

    def __init__(self):  # Constructor de la clase
        super().__init__()  # Llamamos al constructor de la clase padre (QWidget)
        self.initUI()  # Llamamos al metodo que inicializa la interfaz gráfica

    def initUI(self):  # Metodo para configurar la interfaz
        self.setGeometry(300, 300, 400, 300)  # Asignamos la posición y tamaño de la ventana
        self.setWindowTitle('Presiona una tecla')
        self.show()

    def keyPressEvent(self, event):  # Método que maneja la pulsación de teclas
        key = event.text()  # Obtenemos el carácter de la tecla presionada
        if key:  # Verificamos si se ha presionado una tecla válida
            respuesta = QMessageBox.question(  # Mostramos un cuadro de diálogo de confirmación
                self,
                "Confirmar cambio",
                f"¿Deseas cambiar el título de la ventana por '{key}'?",  # Preguntamos si desea cambiar el título
                QMessageBox.Yes | QMessageBox.No,  # Opciones de respuesta (Sí o No)
                QMessageBox.No  # Opción predeterminada (No)
            )

            if respuesta == QMessageBox.Yes:  # Si el usuario elige "Sí"
                self.setWindowTitle(f'Tecla presionada: {key}')  # Cambia el título de la ventana

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()  # Llama a la funcion principal