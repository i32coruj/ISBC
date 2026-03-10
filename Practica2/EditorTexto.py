#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 19:42:46 2026

@author: Javier Jesús Costa Ruiz-canela
"""

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit, QAction, 
                             QFileDialog, QMessageBox)

class EditorTexto(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 1. Configuración del área central
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.ruta_archivo = None  # Variable para recordar dónde está guardado el archivo actual

        # 2. Configuración de la Barra de Estado
        self.statusBar().showMessage('Listo para escribir')

        # 3. Creación de las Acciones (Eventos)
        abrirAct = QAction('Abrir', self)
        abrirAct.setShortcut('Ctrl+O')
        abrirAct.setStatusTip('Abrir un documento existente')
        abrirAct.triggered.connect(self.abrir_fichero)

        salvarAct = QAction('Guardar', self)
        salvarAct.setShortcut('Ctrl+S')
        salvarAct.setStatusTip('Guardar el documento actual')
        salvarAct.triggered.connect(self.salvar_fichero)

        salvarComoAct = QAction('Guardar como...', self)
        salvarComoAct.setStatusTip('Guardar el documento con un nuevo nombre')
        salvarComoAct.triggered.connect(self.salvar_como)

        # 4. Creación del Menú
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Archivo')
        fileMenu.addAction(abrirAct)
        fileMenu.addAction(salvarAct)
        fileMenu.addAction(salvarComoAct)

        # 5. Creación de la Barra de Herramientas
        toolbar = self.addToolBar('Archivo')
        toolbar.addAction(abrirAct)
        toolbar.addAction(salvarAct)

        # 6. Configuración de la Ventana Principal
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Editor de Textos ISBC')
        self.show()

    # --- FUNCIONES DE GESTIÓN DE ARCHIVOS (SLOTS) ---

    def abrir_fichero(self):
        # Abre el explorador de archivos para elegir qué abrir
        opciones = QFileDialog.Options()
        ruta, _ = QFileDialog.getOpenFileName(self, "Abrir Fichero", "", "Archivos de texto (*.txt);;Todos los archivos (*)", options=opciones)
        
        if ruta:
            try:
                with open(ruta, 'r', encoding='utf-8') as f:
                    contenido = f.read()
                    self.textEdit.setText(contenido) # Pone el texto en el editor
                    self.ruta_archivo = ruta # Guarda la ruta en memoria
                    self.setWindowTitle(f'Editor de Textos ISBC - {ruta}')
                    self.statusBar().showMessage('Archivo cargado correctamente')
            except Exception as e:
                QMessageBox.warning(self, "Error", f"No se pudo abrir el archivo:\n{e}")

    def salvar_fichero(self):
        # Si el archivo es nuevo y no tiene ruta, actúa como "Salvar como"
        if self.ruta_archivo is None:
            self.salvar_como()
        else:
            # Si ya tiene ruta, simplemente sobreescribe el archivo con el nuevo texto
            try:
                with open(self.ruta_archivo, 'w', encoding='utf-8') as f:
                    f.write(self.textEdit.toPlainText())
                    self.statusBar().showMessage('Archivo guardado')
            except Exception as e:
                QMessageBox.warning(self, "Error", f"No se pudo guardar el archivo:\n{e}")

    def salvar_como(self):
        # Abre el explorador de archivos para elegir dónde y con qué nombre guardar
        opciones = QFileDialog.Options()
        ruta, _ = QFileDialog.getSaveFileName(self, "Guardar Como", "", "Archivos de texto (*.txt);;Todos los archivos (*)", options=opciones)
        
        if ruta:
            try:
                with open(ruta, 'w', encoding='utf-8') as f:
                    f.write(self.textEdit.toPlainText()) # Guarda el texto actual
                    self.ruta_archivo = ruta # Actualiza la ruta en memoria
                    self.setWindowTitle(f'Editor de Textos ISBC - {ruta}')
                    self.statusBar().showMessage('Archivo guardado exitosamente')
            except Exception as e:
                QMessageBox.warning(self, "Error", f"No se pudo guardar el archivo:\n{e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = EditorTexto()
    sys.exit(app.exec_())