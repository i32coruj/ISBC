# ============================================================================
# vista.py — VISTA (View)
# ============================================================================
# Responsabilidad: Construir toda la interfaz gráfica de usuario con PyQt5.
# Incluye gestión de errores visual (QMessageBox), atajos de teclado,
# barra de estado dinámica, indicador de cambios, búsqueda de texto
# y alternancia de tema oscuro/claro.
#
# NO contiene lógica de lectura/escritura de archivos. Todas las peticiones
# pasan por el Controlador.
# ============================================================================

import os

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import (
    QTextCharFormat,
    QColor,
    QFont,
    QKeySequence,
    QTextCursor,
    QIcon,
)
from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QSplitter,
    QTextEdit,
    QListWidget,
    QLineEdit,
    QPushButton,
    QLabel,
    QStatusBar,
    QMessageBox,
    QFileDialog,
    QShortcut,
    QFrame,
    QToolBar,
    QAction,
    QSizePolicy,
)


# ============================================================================
#  Hojas de estilo para los temas claro y oscuro
# ============================================================================

ESTILO_CLARO = """
QMainWindow {
    background-color: #f5f5f5;
}
QTextEdit {
    background-color: #ffffff;
    color: #1e1e1e;
    border: 1px solid #cccccc;
    border-radius: 4px;
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 13px;
    padding: 6px;
    selection-background-color: #add6ff;
}
QListWidget {
    background-color: #ffffff;
    color: #1e1e1e;
    border: 1px solid #cccccc;
    border-radius: 4px;
    font-size: 13px;
    padding: 2px;
}
QListWidget::item:selected {
    background-color: #0078d4;
    color: #ffffff;
}
QListWidget::item:hover {
    background-color: #e8e8e8;
}
QLineEdit {
    background-color: #ffffff;
    color: #1e1e1e;
    border: 1px solid #cccccc;
    border-radius: 4px;
    padding: 4px 8px;
    font-size: 13px;
}
QPushButton {
    background-color: #0078d4;
    color: #ffffff;
    border: none;
    border-radius: 4px;
    padding: 6px 16px;
    font-size: 13px;
    font-weight: bold;
}
QPushButton:hover {
    background-color: #106ebe;
}
QPushButton:pressed {
    background-color: #005a9e;
}
QPushButton#btnTema {
    background-color: #6c757d;
}
QPushButton#btnTema:hover {
    background-color: #5a6268;
}
QLabel {
    color: #1e1e1e;
    font-size: 13px;
}
QStatusBar {
    background-color: #007acc;
    color: #ffffff;
    font-size: 12px;
    padding: 2px 8px;
}
QToolBar {
    background-color: #e8e8e8;
    border-bottom: 1px solid #cccccc;
    spacing: 4px;
    padding: 2px;
}
QFrame#panelBusqueda {
    background-color: #f0f0f0;
    border: 1px solid #cccccc;
    border-radius: 4px;
    padding: 4px;
}
QSplitter::handle {
    background-color: #cccccc;
}
"""

ESTILO_OSCURO = """
QMainWindow {
    background-color: #1e1e1e;
}
QTextEdit {
    background-color: #1e1e1e;
    color: #d4d4d4;
    border: 1px solid #3c3c3c;
    border-radius: 4px;
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 13px;
    padding: 6px;
    selection-background-color: #264f78;
}
QListWidget {
    background-color: #252526;
    color: #d4d4d4;
    border: 1px solid #3c3c3c;
    border-radius: 4px;
    font-size: 13px;
    padding: 2px;
}
QListWidget::item:selected {
    background-color: #094771;
    color: #ffffff;
}
QListWidget::item:hover {
    background-color: #2a2d2e;
}
QLineEdit {
    background-color: #3c3c3c;
    color: #d4d4d4;
    border: 1px solid #555555;
    border-radius: 4px;
    padding: 4px 8px;
    font-size: 13px;
}
QPushButton {
    background-color: #0e639c;
    color: #ffffff;
    border: none;
    border-radius: 4px;
    padding: 6px 16px;
    font-size: 13px;
    font-weight: bold;
}
QPushButton:hover {
    background-color: #1177bb;
}
QPushButton:pressed {
    background-color: #094771;
}
QPushButton#btnTema {
    background-color: #555555;
}
QPushButton#btnTema:hover {
    background-color: #666666;
}
QLabel {
    color: #d4d4d4;
    font-size: 13px;
}
QStatusBar {
    background-color: #007acc;
    color: #ffffff;
    font-size: 12px;
    padding: 2px 8px;
}
QToolBar {
    background-color: #2d2d2d;
    border-bottom: 1px solid #3c3c3c;
    spacing: 4px;
    padding: 2px;
}
QFrame#panelBusqueda {
    background-color: #2d2d2d;
    border: 1px solid #3c3c3c;
    border-radius: 4px;
    padding: 4px;
}
QSplitter::handle {
    background-color: #3c3c3c;
}
"""


# ============================================================================
#  Clase principal — VistaEditor
# ============================================================================


class VistaEditor(QMainWindow):
    """Vista principal del Editor de Archivos Avanzado.

    Construye la interfaz gráfica completa, gestiona atajos de teclado,
    barra de estado dinámica, indicador de cambios sin guardar,
    búsqueda de texto y alternancia de tema oscuro / claro.
    """

    TITULO_BASE = "Editor de Archivos Avanzado"

    def __init__(self, controlador):
        super().__init__()
        self.controlador = controlador

        # Estado interno de la vista
        self._archivo_actual: str | None = None
        self._directorio_actual: str = os.path.expanduser("~")
        self._cambios_pendientes: bool = False
        self._tema_oscuro: bool = False
        self._posiciones_busqueda: list[int] = []
        self._indice_busqueda: int = -1

        # Construir interfaz
        self._crear_interfaz()
        self._crear_atajos()
        self._conectar_senales()

        # Estado inicial
        self._aplicar_tema()
        self._navegar_directorio(self._directorio_actual)
        self._actualizar_titulo()
        self._actualizar_estado()

    # ================================================================== #
    #  CONSTRUCCIÓN DE LA INTERFAZ
    # ================================================================== #

    def _crear_interfaz(self):
        """Construye todos los widgets y los organiza con layouts."""
        self.setWindowTitle(self.TITULO_BASE)
        self.setMinimumSize(960, 640)
        self.resize(1200, 750)

        # ----- Widget central -----
        widget_central = QWidget()
        self.setCentralWidget(widget_central)
        layout_principal = QVBoxLayout(widget_central)
        layout_principal.setContentsMargins(6, 6, 6, 6)
        layout_principal.setSpacing(6)

        # ----- Barra de navegación de directorio -----
        layout_nav = QHBoxLayout()
        self.btn_seleccionar_dir = QPushButton("📂 Seleccionar directorio")
        self.btn_seleccionar_dir.setToolTip("Abrir un directorio con el explorador del sistema")
        self.lbl_directorio_actual = QLabel(self._directorio_actual)
        self.lbl_directorio_actual.setStyleSheet("padding: 4px 8px;")
        layout_nav.addWidget(self.btn_seleccionar_dir)
        layout_nav.addWidget(self.lbl_directorio_actual, 1)
        layout_principal.addLayout(layout_nav)

        # ----- Panel de búsqueda -----
        self.panel_busqueda = QFrame()
        self.panel_busqueda.setObjectName("panelBusqueda")
        layout_busqueda = QHBoxLayout(self.panel_busqueda)
        layout_busqueda.setContentsMargins(6, 4, 6, 4)
        self.lbl_buscar = QLabel("🔍 Buscar:")
        self.txt_buscar = QLineEdit()
        self.txt_buscar.setPlaceholderText("Escriba el texto a buscar…")
        self.btn_buscar = QPushButton("Buscar")
        self.btn_buscar.setFixedWidth(80)
        self.btn_buscar_sig = QPushButton("▼")
        self.btn_buscar_sig.setToolTip("Siguiente coincidencia")
        self.btn_buscar_sig.setFixedWidth(36)
        self.btn_buscar_ant = QPushButton("▲")
        self.btn_buscar_ant.setToolTip("Anterior coincidencia")
        self.btn_buscar_ant.setFixedWidth(36)
        self.btn_cerrar_busqueda = QPushButton("✕")
        self.btn_cerrar_busqueda.setToolTip("Cerrar panel de búsqueda")
        self.btn_cerrar_busqueda.setFixedWidth(36)
        self.lbl_resultados = QLabel("")
        layout_busqueda.addWidget(self.lbl_buscar)
        layout_busqueda.addWidget(self.txt_buscar, 1)
        layout_busqueda.addWidget(self.btn_buscar)
        layout_busqueda.addWidget(self.btn_buscar_ant)
        layout_busqueda.addWidget(self.btn_buscar_sig)
        layout_busqueda.addWidget(self.lbl_resultados)
        layout_busqueda.addWidget(self.btn_cerrar_busqueda)
        self.panel_busqueda.setVisible(False)
        layout_principal.addWidget(self.panel_busqueda)

        # ----- Splitter: lista de archivos | editor de texto -----
        self.divisor = QSplitter(Qt.Horizontal)

        # Panel izquierdo — explorador de archivos
        panel_izquierdo = QWidget()
        layout_izq = QVBoxLayout(panel_izquierdo)
        layout_izq.setContentsMargins(0, 0, 0, 0)
        self.lbl_explorador = QLabel("Archivos")
        self.lbl_explorador.setStyleSheet("font-weight: bold; padding: 2px 4px;")
        self.lista_archivos = QListWidget()
        layout_izq.addWidget(self.lbl_explorador)
        layout_izq.addWidget(self.lista_archivos)

        # Panel derecho — editor de texto
        panel_derecho = QWidget()
        layout_der = QVBoxLayout(panel_derecho)
        layout_der.setContentsMargins(0, 0, 0, 0)
        self.lbl_editor = QLabel("Editor")
        self.lbl_editor.setStyleSheet("font-weight: bold; padding: 2px 4px;")
        self.editor = QTextEdit()
        self.editor.setAcceptRichText(False)
        layout_der.addWidget(self.lbl_editor)
        layout_der.addWidget(self.editor)

        self.divisor.addWidget(panel_izquierdo)
        self.divisor.addWidget(panel_derecho)
        self.divisor.setStretchFactor(0, 1)
        self.divisor.setStretchFactor(1, 3)
        self.divisor.setSizes([280, 800])
        layout_principal.addWidget(self.divisor, 1)

        # ----- Barra de botones de acción -----
        layout_acciones = QHBoxLayout()
        self.btn_nuevo = QPushButton("📄 Nuevo (Ctrl+N)")
        self.btn_guardar = QPushButton("💾 Guardar (Ctrl+S)")
        self.btn_guardar_como = QPushButton("📁 Guardar como… (Ctrl+Shift+S)")
        self.btn_tema = QPushButton("🌙 Modo Oscuro")
        self.btn_tema.setObjectName("btnTema")
        self.btn_alternar_busqueda = QPushButton("🔍 Buscar (Ctrl+F)")

        layout_acciones.addWidget(self.btn_nuevo)
        layout_acciones.addWidget(self.btn_guardar)
        layout_acciones.addWidget(self.btn_guardar_como)
        layout_acciones.addStretch()
        layout_acciones.addWidget(self.btn_alternar_busqueda)
        layout_acciones.addWidget(self.btn_tema)
        layout_principal.addLayout(layout_acciones)

        # ----- Barra de estado -----
        self.barra_estado = QStatusBar()
        self.setStatusBar(self.barra_estado)
        self.lbl_ruta_estado = QLabel("Sin archivo abierto")
        self.lbl_estadisticas = QLabel("Caracteres: 0 | Líneas: 0 | Palabras: 0")
        self.lbl_cambios = QLabel("")
        self.barra_estado.addWidget(self.lbl_ruta_estado, 2)
        self.barra_estado.addWidget(self.lbl_cambios, 0)
        self.barra_estado.addPermanentWidget(self.lbl_estadisticas)

    # ================================================================== #
    #  ATAJOS DE TECLADO
    # ================================================================== #

    def _crear_atajos(self):
        """Registra los atajos de teclado globales."""
        QShortcut(QKeySequence("Ctrl+S"), self, activated=self._accion_guardar)
        QShortcut(QKeySequence("Ctrl+Shift+S"), self, activated=self._accion_guardar_como)
        QShortcut(QKeySequence("Ctrl+N"), self, activated=self._accion_nuevo)
        QShortcut(QKeySequence("Ctrl+F"), self, activated=self._alternar_panel_busqueda)

    # ================================================================== #
    #  CONEXIÓN DE SEÑALES
    # ================================================================== #

    def _conectar_senales(self):
        """Conecta las señales de los widgets a sus slots."""
        # Navegación
        self.btn_seleccionar_dir.clicked.connect(self._seleccionar_directorio)
        self.lista_archivos.itemDoubleClicked.connect(self._abrir_elemento)

        # Acciones de archivo
        self.btn_nuevo.clicked.connect(self._accion_nuevo)
        self.btn_guardar.clicked.connect(self._accion_guardar)
        self.btn_guardar_como.clicked.connect(self._accion_guardar_como)

        # Tema
        self.btn_tema.clicked.connect(self._alternar_tema)

        # Búsqueda
        self.btn_alternar_busqueda.clicked.connect(self._alternar_panel_busqueda)
        self.btn_buscar.clicked.connect(self._ejecutar_busqueda)
        self.txt_buscar.returnPressed.connect(self._ejecutar_busqueda)
        self.btn_buscar_sig.clicked.connect(self._buscar_siguiente)
        self.btn_buscar_ant.clicked.connect(self._buscar_anterior)
        self.btn_cerrar_busqueda.clicked.connect(self._cerrar_busqueda)

        # Detección de cambios en el editor
        self.editor.textChanged.connect(self._al_cambiar_texto)

    # ================================================================== #
    #  NAVEGACIÓN DE DIRECTORIOS
    # ================================================================== #

    def _seleccionar_directorio(self):
        """Abre un diálogo nativo para seleccionar un directorio."""
        ruta = QFileDialog.getExistingDirectory(
            self,
            "Seleccionar directorio",
            self._directorio_actual,
            QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks,
        )
        if ruta:
            self._navegar_directorio(ruta)

    def _navegar_directorio(self, ruta: str):
        """Carga el contenido de *ruta* en la lista de archivos."""
        exito, resultado = self.controlador.listar_directorio(ruta)
        if not exito:
            QMessageBox.warning(self, "Error de navegación", resultado)
            return
        self._directorio_actual = os.path.abspath(ruta)
        self.lbl_directorio_actual.setText(self._directorio_actual)
        self.lista_archivos.clear()
        for nombre in resultado:
            ruta_completa = self.controlador.ruta_absoluta(
                self._directorio_actual, nombre
            )
            if self.controlador.es_directorio(ruta_completa):
                self.lista_archivos.addItem(f"📁 {nombre}")
            else:
                self.lista_archivos.addItem(f"📄 {nombre}")
        self.lbl_explorador.setText(f"Archivos — {os.path.basename(self._directorio_actual)}")

    def _abrir_elemento(self, elemento):
        """Abre un archivo o navega a un directorio al hacer doble clic."""
        texto = elemento.text()
        # Quitar el ícono de prefijo
        nombre = texto.split(" ", 1)[-1].strip()

        ruta_completa = self.controlador.ruta_absoluta(
            self._directorio_actual, nombre
        )

        if self.controlador.es_directorio(ruta_completa):
            self._navegar_directorio(ruta_completa)
        elif self.controlador.es_archivo(ruta_completa):
            self._abrir_archivo(ruta_completa)

    def _abrir_archivo(self, ruta: str):
        """Solicita al controlador la lectura de un archivo y lo muestra."""
        # Comprobar cambios pendientes antes de abrir otro archivo
        if self._cambios_pendientes:
            resp = QMessageBox.question(
                self,
                "Cambios sin guardar",
                "Hay cambios sin guardar. ¿Desea descartarlos y abrir otro archivo?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No,
            )
            if resp == QMessageBox.No:
                return

        exito, resultado = self.controlador.leer_archivo(ruta)
        if not exito:
            QMessageBox.warning(self, "Error al abrir archivo", resultado)
            return

        self._archivo_actual = ruta
        self.editor.blockSignals(True)  # Evitar que textChanged dispare
        self.editor.setPlainText(resultado)
        self.editor.blockSignals(False)
        self._cambios_pendientes = False
        self._actualizar_titulo()
        self._actualizar_estado()
        self._limpiar_busqueda()

    # ================================================================== #
    #  ACCIONES DE ARCHIVO
    # ================================================================== #

    def _accion_nuevo(self):
        """Crea un nuevo archivo vacío (Ctrl+N)."""
        if self._cambios_pendientes:
            resp = QMessageBox.question(
                self,
                "Cambios sin guardar",
                "Hay cambios sin guardar. ¿Desea descartarlos?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No,
            )
            if resp == QMessageBox.No:
                return

        self._archivo_actual = None
        self.editor.blockSignals(True)
        self.editor.clear()
        self.editor.blockSignals(False)
        self._cambios_pendientes = False
        self._actualizar_titulo()
        self._actualizar_estado()
        self._limpiar_busqueda()

    def _accion_guardar(self):
        """Guarda el archivo actual (Ctrl+S)."""
        if self._archivo_actual is None:
            # Si no hay archivo, redirigir a "Guardar como"
            self._accion_guardar_como()
            return
        contenido = self.editor.toPlainText()
        exito, resultado = self.controlador.guardar_archivo(
            self._archivo_actual, contenido
        )
        if exito:
            self._cambios_pendientes = False
            self._actualizar_titulo()
            self._actualizar_estado()
            self.barra_estado.showMessage("Archivo guardado correctamente.", 3000)
        else:
            QMessageBox.critical(self, "Error al guardar", resultado)

    def _accion_guardar_como(self):
        """Guarda con un nombre nuevo (Ctrl+Shift+S)."""
        ruta, _ = QFileDialog.getSaveFileName(
            self,
            "Guardar como…",
            self._directorio_actual,
            "Todos los archivos (*);;Archivos de texto (*.txt);;Python (*.py)",
        )
        if not ruta:
            return  # El usuario canceló
        contenido = self.editor.toPlainText()
        exito, resultado = self.controlador.guardar_archivo(ruta, contenido)
        if exito:
            self._archivo_actual = ruta
            self._cambios_pendientes = False
            self._actualizar_titulo()
            self._actualizar_estado()
            # Refrescar la lista de archivos si guardamos en el directorio actual
            dir_guardado = os.path.dirname(ruta)
            if os.path.abspath(dir_guardado) == os.path.abspath(self._directorio_actual):
                self._navegar_directorio(self._directorio_actual)
            self.barra_estado.showMessage("Archivo guardado correctamente.", 3000)
        else:
            QMessageBox.critical(self, "Error al guardar", resultado)

    # ================================================================== #
    #  DETECCIÓN DE CAMBIOS (Indicador de cambios sin guardar)
    # ================================================================== #

    def _al_cambiar_texto(self):
        """Se invoca cada vez que el contenido del editor cambia."""
        if not self._cambios_pendientes:
            self._cambios_pendientes = True
            self._actualizar_titulo()
        self._actualizar_estado()

    def _actualizar_titulo(self):
        """Actualiza el título de la ventana con el indicador de cambios."""
        nombre = (
            os.path.basename(self._archivo_actual)
            if self._archivo_actual
            else "Sin título"
        )
        asterisco = " *" if self._cambios_pendientes else ""
        self.setWindowTitle(f"{nombre}{asterisco} — {self.TITULO_BASE}")

    # ================================================================== #
    #  BARRA DE ESTADO
    # ================================================================== #

    def _actualizar_estado(self):
        """Actualiza la barra de estado con la ruta y las estadísticas."""
        # Ruta del archivo activo
        if self._archivo_actual:
            self.lbl_ruta_estado.setText(f"  {self._archivo_actual}")
        else:
            self.lbl_ruta_estado.setText("  Sin archivo abierto")

        # Estadísticas
        texto = self.editor.toPlainText()
        estadisticas = self.controlador.contar_estadisticas(texto)
        self.lbl_estadisticas.setText(
            f"Caracteres: {estadisticas['caracteres']} | "
            f"Líneas: {estadisticas['lineas']} | "
            f"Palabras: {estadisticas['palabras']}"
        )

        # Indicador de cambios
        if self._cambios_pendientes:
            self.lbl_cambios.setText(" ● Sin guardar ")
            self.lbl_cambios.setStyleSheet(
                "color: #ffcc00; font-weight: bold; font-size: 12px;"
            )
        else:
            self.lbl_cambios.setText("")

    # ================================================================== #
    #  BÚSQUEDA DE TEXTO
    # ================================================================== #

    def _alternar_panel_busqueda(self):
        """Muestra u oculta el panel de búsqueda."""
        visible = not self.panel_busqueda.isVisible()
        self.panel_busqueda.setVisible(visible)
        if visible:
            self.txt_buscar.setFocus()
            self.txt_buscar.selectAll()

    def _cerrar_busqueda(self):
        """Cierra el panel de búsqueda y limpia los resaltados."""
        self.panel_busqueda.setVisible(False)
        self._limpiar_busqueda()

    def _ejecutar_busqueda(self):
        """Busca todas las coincidencias del término en el editor."""
        termino = self.txt_buscar.text()
        if not termino:
            self.lbl_resultados.setText("Ingrese un término.")
            return

        contenido = self.editor.toPlainText()
        self._posiciones_busqueda = self.controlador.buscar_texto(contenido, termino)
        cantidad = len(self._posiciones_busqueda)

        if cantidad == 0:
            self.lbl_resultados.setText("Sin resultados")
            self._limpiar_resaltado()
            self._indice_busqueda = -1
            return

        self.lbl_resultados.setText(f"{cantidad} coincidencia(s)")
        self._indice_busqueda = 0
        self._resaltar_coincidencias(termino)
        self._ir_a_coincidencia(0)

    def _resaltar_coincidencias(self, termino: str):
        """Resalta todas las coincidencias en el editor."""
        self._limpiar_resaltado()
        formato = QTextCharFormat()
        formato.setBackground(QColor("#ffeb3b") if not self._tema_oscuro else QColor("#665c00"))
        formato.setForeground(QColor("#000000") if not self._tema_oscuro else QColor("#ffeb3b"))

        cursor = self.editor.textCursor()
        longitud = len(termino)

        self.editor.blockSignals(True)
        for pos in self._posiciones_busqueda:
            cursor.setPosition(pos)
            cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor, longitud)
            cursor.mergeCharFormat(formato)
        self.editor.blockSignals(False)

    def _limpiar_resaltado(self):
        """Elimina todos los resaltados de búsqueda."""
        cursor = self.editor.textCursor()
        self.editor.blockSignals(True)
        cursor.select(QTextCursor.Document)
        formato = QTextCharFormat()
        formato.clearBackground()
        formato.clearForeground()
        cursor.setCharFormat(formato)
        self.editor.blockSignals(False)

    def _ir_a_coincidencia(self, indice: int):
        """Desplaza el cursor a la coincidencia número *indice*."""
        if not self._posiciones_busqueda:
            return
        indice = indice % len(self._posiciones_busqueda)
        self._indice_busqueda = indice
        pos = self._posiciones_busqueda[indice]
        cursor = self.editor.textCursor()
        cursor.setPosition(pos)
        self.editor.setTextCursor(cursor)
        self.editor.ensureCursorVisible()
        self.lbl_resultados.setText(
            f"{indice + 1}/{len(self._posiciones_busqueda)} coincidencia(s)"
        )

    def _buscar_siguiente(self):
        """Navega a la siguiente coincidencia."""
        if self._posiciones_busqueda:
            self._ir_a_coincidencia(self._indice_busqueda + 1)

    def _buscar_anterior(self):
        """Navega a la coincidencia anterior."""
        if self._posiciones_busqueda:
            self._ir_a_coincidencia(self._indice_busqueda - 1)

    def _limpiar_busqueda(self):
        """Restablece el estado de búsqueda."""
        self._posiciones_busqueda = []
        self._indice_busqueda = -1
        self.lbl_resultados.setText("")
        self._limpiar_resaltado()

    # ================================================================== #
    #  TEMA OSCURO / CLARO
    # ================================================================== #

    def _alternar_tema(self):
        """Alterna entre el tema claro y el tema oscuro."""
        self._tema_oscuro = not self._tema_oscuro
        self._aplicar_tema()

    def _aplicar_tema(self):
        """Aplica la hoja de estilos correspondiente al tema actual."""
        if self._tema_oscuro:
            self.setStyleSheet(ESTILO_OSCURO)
            self.btn_tema.setText("☀️ Modo Claro")
        else:
            self.setStyleSheet(ESTILO_CLARO)
            self.btn_tema.setText("🌙 Modo Oscuro")
