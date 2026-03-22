# ============================================================================
# modelo.py — MODELO (Model)
# ============================================================================
# Responsabilidad: Toda la lógica de negocio y de E/S de archivos.
# NO tiene dependencias de PyQt5. Devuelve tuplas (éxito, resultado_o_mensaje).
# ============================================================================

import os


class ModeloEditor:
    """Modelo del Editor de Archivos Avanzado.

    Gestiona la lectura/escritura de archivos en disco usando codificación
    UTF-8 y proporciona utilidades de exploración de directorios.
    """

    # ------------------------------------------------------------------ #
    #  Exploración de directorios
    # ------------------------------------------------------------------ #

    def listar_directorio(self, ruta: str) -> tuple[bool, list[str] | str]:
        """Devuelve la lista de elementos (archivos y carpetas) de *ruta*.

        Devuelve:
            (True, lista_de_nombres)  si la operación fue exitosa.
            (False, mensaje_de_error) si hubo un problema.
        """
        try:
            if not os.path.isdir(ruta):
                return False, f"La ruta no es un directorio válido: {ruta}"
            elementos = sorted(os.listdir(ruta))
            return True, elementos
        except PermissionError:
            return False, f"Sin permisos para acceder a: {ruta}"
        except Exception as e:
            return False, f"Error al listar directorio: {e}"

    def es_directorio(self, ruta: str) -> bool:
        """Indica si *ruta* es un directorio."""
        return os.path.isdir(ruta)

    def es_archivo(self, ruta: str) -> bool:
        """Indica si *ruta* es un archivo regular."""
        return os.path.isfile(ruta)

    def ruta_absoluta(self, base: str, nombre: str) -> str:
        """Construye la ruta absoluta uniendo *base* y *nombre*."""
        return os.path.join(base, nombre)

    def directorio_padre(self, ruta: str) -> str:
        """Devuelve el directorio padre de *ruta*."""
        return os.path.dirname(ruta)

    # ------------------------------------------------------------------ #
    #  Lectura de archivos
    # ------------------------------------------------------------------ #

    def leer_archivo(self, ruta: str) -> tuple[bool, str]:
        """Lee el contenido completo de un archivo en UTF-8.

        Devuelve:
            (True, contenido)         si se leyó correctamente.
            (False, mensaje_de_error) si hubo algún problema.
        """
        try:
            if not os.path.isfile(ruta):
                return False, f"El archivo no existe: {ruta}"
            with open(ruta, "r", encoding="utf-8") as f:
                contenido = f.read()
            return True, contenido
        except PermissionError:
            return False, f"Sin permisos para leer: {ruta}"
        except UnicodeDecodeError:
            return False, f"El archivo no es texto válido UTF-8: {ruta}"
        except Exception as e:
            return False, f"Error al leer archivo: {e}"

    # ------------------------------------------------------------------ #
    #  Escritura / guardado de archivos
    # ------------------------------------------------------------------ #

    def guardar_archivo(self, ruta: str, contenido: str) -> tuple[bool, str]:
        """Escribe *contenido* en *ruta* usando codificación UTF-8.

        Devuelve:
            (True, ruta)              si se guardó correctamente.
            (False, mensaje_de_error) si hubo algún problema.
        """
        try:
            directorio = os.path.dirname(ruta)
            if directorio and not os.path.exists(directorio):
                os.makedirs(directorio, exist_ok=True)
            with open(ruta, "w", encoding="utf-8") as f:
                f.write(contenido)
            return True, ruta
        except PermissionError:
            return False, f"Sin permisos para escribir en: {ruta}"
        except Exception as e:
            return False, f"Error al guardar archivo: {e}"

    # ------------------------------------------------------------------ #
    #  Crear archivo nuevo
    # ------------------------------------------------------------------ #

    def crear_archivo(self, ruta: str) -> tuple[bool, str]:
        """Crea un archivo vacío en *ruta*.

        Devuelve:
            (True, ruta)              si se creó correctamente.
            (False, mensaje_de_error) si hubo algún problema.
        """
        try:
            if os.path.exists(ruta):
                return False, f"El archivo ya existe: {ruta}"
            directorio = os.path.dirname(ruta)
            if directorio and not os.path.exists(directorio):
                os.makedirs(directorio, exist_ok=True)
            with open(ruta, "w", encoding="utf-8") as f:
                f.write("")
            return True, ruta
        except PermissionError:
            return False, f"Sin permisos para crear: {ruta}"
        except Exception as e:
            return False, f"Error al crear archivo: {e}"

    # ------------------------------------------------------------------ #
    #  Utilidades de texto (sin PyQt)
    # ------------------------------------------------------------------ #

    def contar_estadisticas(self, texto: str) -> dict:
        """Devuelve un diccionario con estadísticas del texto.

        Keys: 'caracteres', 'lineas', 'palabras'.
        """
        return {
            "caracteres": len(texto),
            "lineas": texto.count("\n") + 1 if texto else 0,
            "palabras": len(texto.split()) if texto else 0,
        }

    def buscar_texto(self, contenido: str, termino: str) -> list[int]:
        """Busca *termino* en *contenido* y devuelve las posiciones de inicio.

        La búsqueda no distingue mayúsculas de minúsculas.

        Devuelve:
            Lista de índices donde se encontró *termino*.
        """
        if not termino:
            return []
        posiciones = []
        contenido_min = contenido.lower()
        termino_min = termino.lower()
        inicio = 0
        while True:
            idx = contenido_min.find(termino_min, inicio)
            if idx == -1:
                break
            posiciones.append(idx)
            inicio = idx + 1
        return posiciones
