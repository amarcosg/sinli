#from .document import Document
#from .doctype import DocumentType
from .line import Line
from .common.encoded_values import SinliCode as c, BasicType as t
from .doctype import DocumentType

from enum import Enum
from dataclasses import dataclass, field

@dataclass
class Subject(Line):
    """
    El asunto o subject del mensaje contendrá:
    ESFANDE 7A, Identificador emisor 8A, ESFANDE 7A, Identificador destino 8A,
    Documento 6A, Versión Identificador 2N, FANDE 5A

    Ejemplo:
    ESFANDELIBXXXXXESFANDELIBXXXXXENVIO NNFANDE
    0123456789012345678901234567890123456789012
    0        10        20        30        40
    """
    doctype_desc = ""
    doctype_class = None

    class Field(Enum):
        FILLING1 = (0, 7, t.STR, "ESFANDE")
        FROM     = (7, 8, t.STR, "Sinli From Id")
        FILLING2 = (15, 7, t.STR, "ESFANDE")
        TO       = (22, 8, t.STR, "Sinli To Id")
        DOCTYPE  = (30, 6, t.STR, "Tipo de Fichero")
        VERSION  = (36, 2, t.INT, "Versión fichero")
        FILLING3 = (38, 5, t.STR, "FANDE")

    def __post_init__(self):
        super().__post_init__()
        self.FILLING1 = "ESFANDE"
        self.FILLING2 = "ESFANDE"
        self.FILLING3 = "FANDE"

    def get_doctype_desc(self) -> str:
        if self.doctype_desc == "":
            self.doctype_desc = getattr(DocumentType, self.DOCTYPE).value[0]

        return self.doctype_desc

    def get_doctype_class(self) -> str:
        if self.doctype_class == None:
            val = getattr(DocumentType, self.DOCTYPE).value
            self.doctype_class = val[1].get(self.VERSION) or val[1].get('??')

        return self.doctype_class

