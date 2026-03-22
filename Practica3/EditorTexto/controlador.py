# ============================================================================
# controlador.py — CONTROLADOR (Controller)
# ============================================================================
# Responsabilidad: Intermediario puro entre la Vista y el Modelo.
# Recibe peticiones de la vista, las delega al modelo y devuelve los
# resultados. NO contiene lógica de negocio ni de interfaz gráfica.
# ============================================================================

from modelo import ModeloEditor


class ControladorEditor:
    """Controlador del Editor de Archivos Avanzado.

    Actúa como intermediario puro: recibe peticiones de la vista,
    las delega al modelo y retorna los resultados sin modificarlos.
    """

    def __init__(self):
        self.modelo = ModeloEditor()

    # ------------------------------------------------------------------ #
    #  Delegación — Exploración de directorios
    # ------------------------------------------------------------------ #

    def listar_directorio(self, ruta: str):
        """Solicita al modelo la lista de elementos de un directorio."""
        return self.modelo.listar_directorio(ruta)

    def es_directorio(self, ruta: str) -> bool:
        """Consulta al modelo si la ruta es un directorio."""
        return self.modelo.es_directorio(ruta)

    def es_archivo(self, ruta: str) -> bool:
        """Consulta al modelo si la ruta es un archivo."""
        return self.modelo.es_archivo(ruta)

    def ruta_absoluta(self, base: str, nombre: str) -> str:
        """Solicita al modelo la ruta absoluta."""
        return self.modelo.ruta_absoluta(base, nombre)

    def directorio_padre(self, ruta: str) -> str:
        """Solicita al modelo el directorio padre."""
        return self.modelo.directorio_padre(ruta)

    # ------------------------------------------------------------------ #
    #  Delegación — Lectura / escritura de archivos
    # ------------------------------------------------------------------ #

    def leer_archivo(self, ruta: str):
        """Solicita al modelo la lectura de un archivo."""
        return self.modelo.leer_archivo(ruta)

    def guardar_archivo(self, ruta: str, contenido: str):
        """Solicita al modelo el guardado de un archivo."""
        return self.modelo.guardar_archivo(ruta, contenido)

    def crear_archivo(self, ruta: str):
        """Solicita al modelo la creación de un archivo vacío."""
        return self.modelo.crear_archivo(ruta)

    # ------------------------------------------------------------------ #
    #  Delegación — Utilidades de texto
    # ------------------------------------------------------------------ #

    def contar_estadisticas(self, texto: str) -> dict:
        """Solicita al modelo las estadísticas del texto."""
        return self.modelo.contar_estadisticas(texto)

    def buscar_texto(self, contenido: str, termino: str) -> list[int]:
        """Solicita al modelo la búsqueda de texto."""
        return self.modelo.buscar_texto(contenido, termino)
