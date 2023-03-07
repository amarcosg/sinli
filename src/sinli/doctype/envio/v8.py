from ...document import Document
from ...line import Line
from ...common import SinliCode as c
from ...common import BasicType as t
from enum import Enum
from dataclasses import dataclass, field

@dataclass
class EnvioDoc(Document):
    class Header(Line):
        class Field(Enum):
            TYPE = (0, 1, t.STR,  'Tipo de Registro “C”')
            PROVIDER = (1, 40, t.STR,  "Nombre del proveedor")
            CLIENT = (41, 40, t.STR,  "Nombre del cliente")
            DELIVERY_NUM = (81, 10, t.STR, "Número de albarán")
            DATE = (91, 8, t.DATE8,  "Fecha del documento")
            INVOICE_OR_NOTE = (99, 1, t.STR,  'Tipo de documento: “A” | ”F”') # FIXME afegeix nou tipus enum
            CONSIGNMENT_TYPE = (100, 1, t.STR,  'Tipo de envío: “F” | “D” | “C”| ”P”') # FIXME afegeix nou tipus enum
            BOOK_FAIRE = (101, 1, t.BOOL, '¿Feria del libro? “S” | “N”')
            SHIPPING_COST = (102, 10, t.INT, 'Importe gastos / portes')
            CURRENCY = (112, 1, t.CURRENCY1, 'Moneda')
            FINAL_USER_MAILBOX = (113, 8, t.STR, 'Buzón usuario final')

    # TODO per ara és una còpia de detalle de libro
    class Book(Line):
        class Field(Enum):
            EAN = (0, 18, t.STR, "EAN")
            ISBN_INVOICE = (18, 17, t.STR, "ISBN (Con guiones) Facturación")
            ISBN_COMPLETE = (35, 17, t.STR, "ISBN (Con guiones) Obra completa")
            ISBN_VOLUME = (52, 17, t.STR, "ISBN (Con guiones) Tomo")

    # TODO per ara és una còpia de detalle de libro
    linemap = {
        "C": Header,
        "": Book
    }

