#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 12:58:45 2026

@author: Javier Jesús Costa Ruiz-canela
"""

from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QFileDialog, QApplication
from PyQt5.QtGui import QIcon 
import sys 
from pathlib import Path  


class Example(QMainWindow):

    def __init__(self): 
        super().__init__()  
        self.initUI() 

    def initUI(self):  # Método que configura la interfaz gráfica
        self.textEdit = QTextEdit()  # Crea un área de texto
        self.setCentralWidget(self.textEdit)  # Establece el QTextEdit como widget central
        self.statusBar()  # Agrega una barra de estado

        openFile = QAction(QIcon('open.png'), 'Abrir', self)
        openFile.setShortcut('Ctrl+O')  # Asigna el atajo de teclado Ctrl+O
        openFile.setStatusTip('Abrir un archivo nuevo')  
        openFile.triggered.connect(self.showDialog) 

        menubar = self.menuBar()  # Crea la barra de menú
        fileMenu = menubar.addMenu('&Archivo') 
        fileMenu.addAction(openFile) 

        self.setGeometry(300, 300, 550, 450) 
        self.setWindowTitle('Abrir Archivo') 
        self.show() 

    def showDialog(self):  # Método que muestra el cuadro de diálogo de selección de archivo
        home_dir = str(Path.home())  # Obtiene la ruta del directorio de inicio del usuario
        fname = QFileDialog.getOpenFileName(self, 'Open file', home_dir)  # Abre el cuadro de diálogo

        if fname[0]:  # Si se selecciona un archivo
            f = open(fname[0], 'r')  # Abre el archivo en modo lectura

            with f:  # Asegura que el archivo se cierre automáticamente después de leerlo
                data = f.read()  # Lee el contenido del archivo
                self.textEdit.setText(data)  # Muestra el contenido en el área de texto


def main():
    app = QApplication(sys.argv) 
    ex = Example() 
    sys.exit(app.exec_()) 


if __name__ == '__main__': 
    main()  