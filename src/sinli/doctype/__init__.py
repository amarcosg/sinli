from enum import Enum
from .libros import  v8, v9
from .envio import v8
#from .mensaje import MensajeDoc

class DocumentType(Enum):
    ABONO = ("Albarán o Factura de Abono", None)
    CAMPRE = ("Cambios de precio", None)
    ESTADO = ("Cambios de estado", None)  # noqa: F405
    LIBROS = ("Ficha del Libro", {
        "08": v8.LibrosDoc,
        "09": v9.LibrosDoc,
        "??": v9.LibrosDoc
    })  # noqa: F405
    ENVIO = ("Albarán de envío de distribuidora", {
        "08": v8.Enviodoc,
        "??": v8.Enviodoc,
    })
    MENSAJ = ("Mensaje", None)
