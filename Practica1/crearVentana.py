#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 12:22:17 2026

@author: Javier Jesús Costa Ruiz-Canela
"""


# Importamos los módulos
import sys
from PyQt5.QtWidgets import QApplication, QWidget

def main():
  
    # Creamos el objeto de aplicación 
    app = QApplication(sys.argv)
    
    # Creamos la instancia de ventana
    w = QWidget()
    
    
    # Asignamos el tamaño de la ventana
    w.resize(250, 150)
    
    
    # Asignamos la posición de la ventana
    w.move(300, 300)
    
    
    # Ponemos un nombre a la ventana
    w.setWindowTitle('Crear ventana Simple')
    
    # Mostramos la ventana
    w.show()
    
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
    
    