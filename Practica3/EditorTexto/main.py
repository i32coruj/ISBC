# ============================================================================
# main.py — MAIN (Punto de entrada)
# ============================================================================
# Responsabilidad: Inicializar la aplicación de forma limpia,
# crear las instancias del Controlador y la Vista, y ejecutar
# el bucle principal de eventos de PyQt5.
# ============================================================================

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFont

from controlador import ControladorEditor
from vista import VistaEditor


def principal():
    """Punto de entrada principal de la aplicación."""
    aplicacion = QApplication(sys.argv)

    # Fuente global para toda la aplicación
    fuente = QFont("Segoe UI", 10)
    aplicacion.setFont(fuente)

    # Crear controlador (que a su vez crea el modelo internamente)
    controlador = ControladorEditor()

    # Crear la vista, pasándole el controlador como dependencia
    vista = VistaEditor(controlador)
    vista.show()

    # Ejecutar el bucle de eventos
    sys.exit(aplicacion.exec_())


if __name__ == "__main__":
    principal()
