#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 13:37:15 2026

@author: Javier Jesús Costa Ruiz-canela
"""


from PyQt5.QtWidgets import QWidget, QCalendarWidget, QLabel, QApplication, QVBoxLayout
from PyQt5.QtCore import QDate 
import sys 

class Example(QWidget):  

    def __init__(self): 
        super().__init__() 
        self.initUI()  

    def initUI(self): 
        vbox = QVBoxLayout(self)  # Creamos un layout vertical

        cal = QCalendarWidget(self)  # Creamos un widget de calendario
        cal.setGridVisible(True)  # Hacemos visibles las líneas de la cuadrícula del calendario
        cal.clicked[QDate].connect(self.showDate)  # Conectamos la señal 'clicked' con 'showDate'

        vbox.addWidget(cal)  # Añadimos el widget del calendario al layout

        self.lbl = QLabel(self)  # Creamos un widget de etiqueta para mostrar la fecha seleccionada
        date = cal.selectedDate()  # Obtenemos la fecha seleccionada del calendario
        self.lbl.setText(date.toString())  # Establecemos el texto de la etiqueta con la fecha seleccionada

        vbox.addWidget(self.lbl)  # Añadimos la etiqueta al layout

        self.setLayout(vbox)  # Establecemos el layout principal de la ventana

        self.setGeometry(300, 300, 350, 300) 
        self.setWindowTitle('Calendario')  
        self.show()  

    def showDate(self, date):  # Método que maneja el evento de clic en una fecha del calendario
        self.lbl.setText(date.toString())  # Actualiza la etiqueta con la fecha seleccionada

def main(): 
    app = QApplication(sys.argv) 
    ex = Example() 
    sys.exit(app.exec_()) 

if __name__ == '__main__': 
    main() 
