from enum import Enum
from . import libros
from . import envio
#from .mensaje import MensajeDoc

class DocumentType(Enum):
    ABONO = ("Albarán o Factura de Abono", None)
    CAMPRE = ("Cambios de precio", None)
    ESTADO = ("Cambios de estado", None)  # noqa: F405
    LIBROS = ("Ficha del Libro", {
        "08": libros.v8.LibrosDoc,
        "09": libros.v9.LibrosDoc,
        "??": libros.v9.LibrosDoc
    })  # noqa: F405
    ENVIO = ("Albarán de envío de distribuidora", {
        "08": envio.v8.EnvioDoc,
        "??": envio.v8.EnvioDoc,
    })
    MENSAJ = ("Mensaje", None)
