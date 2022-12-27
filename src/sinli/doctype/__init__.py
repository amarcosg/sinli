from enum import Enum
from .libros import LibrosDoc
#from .mensaje import MensajeDoc

class DocumentType(Enum):
    ABONO = ("Albarán o Factura de Abono", None)
    CAMPRE = ("Cambios de precio", None)
    ESTADO = ("Cambios de estado", None)  # noqa: F405
    LIBROS = ("Ficha del Libro", LibrosDoc)  # noqa: F405
    MENSAJ = ("Mensaje", None)
