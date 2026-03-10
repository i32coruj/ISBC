#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 11:20:13 2026

@author: Javier Jesús Costa Ruiz-canela
"""

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, 
                             QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, 
                             QGridLayout, QAction, QMessageBox)

class AplicacionBasica(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 1. Configuración del Widget Central y Layouts
        widget_central = QWidget()
        self.setCentralWidget(widget_central)
        
        layout_principal = QVBoxLayout()
        grid_datos = QGridLayout()
        
        # 2. Controles dentro de la ventana (Grid)
        self.label_nombre = QLabel('Nombre:')
        self.input_nombre = QLineEdit()
        self.label_email = QLabel('Email:')
        self.input_email = QLineEdit()
        
        grid_datos.addWidget(self.label_nombre, 0, 0)
        grid_datos.addWidget(self.input_nombre, 0, 1)
        grid_datos.addWidget(self.label_email, 1, 0)
        grid_datos.addWidget(self.input_email, 1, 1)
        
        # 3. Botones con Layout Horizontal
        layout_botones = QHBoxLayout()
        btn_enviar = QPushButton('Enviar Datos')
        btn_limpiar = QPushButton('Limpiar')
        
        layout_botones.addStretch(1)
        layout_botones.addWidget(btn_enviar)
        layout_botones.addWidget(btn_limpiar)
        
        layout_principal.addLayout(grid_datos)
        layout_principal.addLayout(layout_botones)
        widget_central.setLayout(layout_principal)

        # 4. Menú, Barra de Herramientas y Estado
        self.statusBar().showMessage('Listo')
        
        menu_archivo = self.menuBar().addMenu('&Opciones')
        accion_salir = QAction('Salir', self)
        accion_salir.setShortcut('Ctrl+Q')
        accion_salir.triggered.connect(self.close)
        menu_archivo.addAction(accion_salir)
        
        toolbar = self.addToolBar('Principal')
        toolbar.addAction(accion_salir)

        # 5. Conexiones (Signals y Slots)
        btn_enviar.clicked.connect(self.mostrar_info)
        btn_limpiar.clicked.connect(self.input_nombre.clear)
        btn_limpiar.clicked.connect(self.input_email.clear)

        # Configuración de Ventana
        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle('Aplicación Básica ISBC')
        self.show()

    def mostrar_info(self):
        nombre = self.input_nombre.text()
        self.statusBar().showMessage(f'Datos enviados por: {nombre}')
        QMessageBox.information(self, 'Éxito', f'Información de {nombre} procesada.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AplicacionBasica()
    sys.exit(app.exec_())