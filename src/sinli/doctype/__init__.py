from enum import Enum
import doctype.libros


class DocumentType(Enum):
    ABONO = ("Albarán o Factura de Abono", None)
    CAMPRE = ("Cambios de precio", None)
    ESTADO = ("Cambios de estado", None)  # noqa: F405
    LIBROS = ("Ficha del Libro", doctype.libros.LibrosDoc)  # noqa: F405
    MENSAJ = ("Mensaje", None)
