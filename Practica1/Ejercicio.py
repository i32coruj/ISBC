#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 16:58:55 2026

@author: Javier Jesús Costa Ruiz-canela
"""
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit, QAction, 
                             QMenu, QMessageBox, QDesktopWidget)
from PyQt5.QtCore import Qt

class EditorISBC(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 1. Configuración Central y Geometría
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.resize(600, 400)
        self.centrar_ventana()
        self.setWindowTitle('Editor ISBC - Presiona una tecla')

        # 2. Barra de Estado
        self.status = self.statusBar()
        self.status.showMessage('Listo')

        # 3. Creación de Acciones
        exitAction = QAction('Salir', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Finalizar la aplicación')
        exitAction.triggered.connect(self.close)

        clearAction = QAction('Limpiar texto', self)
        clearAction.setStatusTip('Borrar todo el contenido del editor')
        clearAction.triggered.connect(lambda: self.textEdit.clear())

        viewStatusAction = QAction('Ver Barra de Estado', self, checkable=True)
        viewStatusAction.setChecked(True)
        viewStatusAction.triggered.connect(self.toggle_status_bar)

        # 4. Barra de Menús
        menubar = self.menuBar()
        
        fileMenu = menubar.addMenu('&Archivo')
        fileMenu.addAction(exitAction)

        viewMenu = menubar.addMenu('&Ver')
        viewMenu.addAction(viewStatusAction)

        accMenu = menubar.addMenu('&Acciones')
        subMenuEdicion = QMenu('Edición', self)
        subMenuEdicion.addAction(clearAction)
        accMenu.addMenu(subMenuEdicion)

        # 5. Barra de Herramientas
        toolbar = self.addToolBar('Salir')
        toolbar.addAction(exitAction)

    # Lógica para centrar la ventana
    def centrar_ventana(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # Lógica para mostrar/ocultar barra de estado
    def toggle_status_bar(self, state):
        if state:
            self.status.show()
        else:
            self.status.hide()

    # Gestión de Menú Contextual (Clic derecho)
    def contextMenuEvent(self, event):
        cmenu = QMenu(self)
        clearAct = cmenu.addAction("Limpiar")
        quitAct = cmenu.addAction("Salir")
        
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
        
        if action == quitAct:
            self.close()
        elif action == clearAct:
            self.textEdit.clear()

    # Gestión de Eventos de Teclado con Confirmación
    def keyPressEvent(self, e):
        reply = QMessageBox.question(self, 'Confirmar cambio',
            f"¿Deseas cambiar el título por la tecla '{e.text()}'?", 
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.setWindowTitle(f"Tecla presionada: {e.text()}")

    # Confirmación al cerrar (Evento Close)
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Mensaje de salida',
            "¿Realmente quiere salir?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = EditorISBC()
    ex.show()
    sys.exit(app.exec_())