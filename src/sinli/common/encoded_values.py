from pycountry import countries, languages
from enum import Enum, auto
from dataclasses import dataclass, fields

class BasicType(Enum):
    MONTH_YEAR=auto(), # MMAAAA
    DATE=auto(), # AAAAMMDD
    STR=auto(),
    INT=auto(),
    FLOAT=auto(),
    BOOL=auto(),
    LANG=auto(),
    COUNTRY=auto(),
    CURRENCY1=auto(), # "P"|"E"
    CURRENCY3=auto(), # ISO-4217. ex: EUR
    #LIST_SEMICOLON
    #LIST_SLASH

@dataclass(frozen = True)
class EncodedField:

    _decoder = {}
    _describer = {}

    def decode(self, code: str):
        return self._decoder.get(code)

    def describe(self, key: str):
        return self._describer.get(key)

    def __post_init__(self):
        for field in fields(self):
            self._decoder[field.default[0]] = field.default
            self._describer[field.default[0]] = field.default[1]
            self._describer[field.name] = field.default[1]

# ↓  Definition of SINLI Encoded Fields ↓ #

@dataclass(frozen = True)
class Binding(EncodedField):
    TELA: () = ("01", "Tela")
    CARTONE: () = ("02", "Cartoné")
    RUSTICA: () = ("03", "Rústica")
    BOLSILLO: () = ("04", "Bolsillo")
    TROQUELADO: () = ("05", "Troquelado")
    ESPIRAL: () = ("06", "Espiral")
    ANILLAS: () = ("07", "Anillas")
    GRAPADO: () = ("08", "Grapado")
    FASCICULO: () = ("09", "Fascículo encuadernable")
    OTROS: () = ("10", "Otros")

@dataclass(frozen = True)
class TBRegion(EncodedField):
    NONE: () = ("00", "Sin asignación a Comunidad Autónoma concreta")
    AN: () = ("01", "ANDALUCÍA")
    AR: () = ("02", "ARAGÓN")
    AS: () = ("03", "PRINCIPADO DE ASTURIAS")
    IB: () = ("04", "ISLAS BALEARES")
    CN: () = ("05", "CANARIAS")
    CB: () = ("06", "CANTABRIA")
    CM: () = ("07", "CASTILLA-LA MANCHA")
    CL: () = ("08", "CASTILLA y LEÓN")
    CT: () = ("09", "CATALUÑA")
    EX: () = ("10", "EXTREMADURA")
    GA: () = ("11", "GALICIA")
    MD: () = ("12", "MADRID")
    MC: () = ("13", "REGIÓN DE MURCIA")
    NC: () = ("14", "NAVARRA")
    PV: () = ("15", "PAÍS VASCO")
    RI: () = ("16", "LA RIOJA")
    VC: () = ("17", "COMUNIDAD VALENCIANA")
    CE: () = ("18", "CIUDAD DE CEUTA")
    ML: () = ("19", "CIUDAD DE MELILLA")
    ALL: () = ("99", "Asignado a todas las Comunidades Autónomas")

@dataclass(frozen = True)
class Status(EncodedField):
    AVAILABLE: () = ("0", "Disponible")
    SOON: () = ("1", "Sin existencias pero disponible a corto plazo")
    EXHAUSTED: () = ("2", "Sin existencias indefinidamente")
    REPRINTING: () = ("3", "En reimpresión")
    NEW: () = ("4", "Novedad. Próxima publicación")
    REEDITION: () = ("5", "Sustituye edición antigua")
    ON_DEMAND: () = ("6", "Impresión bajo demanda 1x1")
    ALIEN: () = ("7", "No pertenece a nuestro fondo o no identificado")
    EXHAUSTED_TMP: () = ("8", "Agotado")
    DISCONTINUED: () = ("9", "Descatalogado")

@dataclass(frozen = True)
class ReadLevel(EncodedField):
    NONE: () = ("0", "Sin calificar")
    AGE_0: () = ("1", "De 0 a 4 años")
    AGE_5: () = ("2", "De 5 a 6 años")
    AGE_7: () = ("3", "De 7 a 8 años")
    AGE_9: () = ("4", "De 9 a 10 años")
    AGE_11: () = ("5", "De 11 a 12 años")

@dataclass(frozen = True)
class Audience(EncodedField):
    NONE: () = ("000", "Sin calificar")
    KIDS: () = ("100", "Infantil hasta 12 años")
    TEEN: () = ("200", "Juvenil de 13 a 15 años")
    TEXT: () = ("300", "Textos")
    GENERIC: () = ("400", "General")

@dataclass(frozen = True)
class ProductType(EncodedField):
    NONE: () = ("00", "sin calificar")
    BOOK: () = ("10", "libro")
    AUDIO: () = ("20", "audio")
    VIDEO: () = ("30", "video")
    CD: () = ("40", "cd-rom")
    DVD: () = ("50", "dvd")
    OTHER: () = ("60", "otros")

@dataclass(frozen = True)
class InvoiceOrNote(EncodedField):
    NOTE: () = ("A", "Albarán")
    INVOICE: () = ("F", "Factura")

@dataclass(frozen = True)
class ConsignmentType(EncodedField):
    FIRM: () = ("F", "Firme")
    DEPOSIT: () = ("D", "Depósito")
    DEPOSIT_FEE: () = ("C", "Cargo al depósito")
    GIFT: () = ("P", "Promoción, obsequio")

@dataclass(frozen = True)
class PriceType(EncodedField):
    FIXED: () = ("F", "Precio final fijo")
    FREE: () = ("L", "Precio final libre")

@dataclass(frozen = True)
class FreePriceType(EncodedField):
    COST: () = ("C", "Coste")
    RECOMMENDED: () = ("R", "Precio recomendado")

@dataclass(frozen = True)
class PaymentType(EncodedField):
    CASH: () = ("1", "Al contado")
    DAYS_30: () = ("2", "A 30 días")
    DAYS_60: () = ("3", "A 60 días")
    DAYS_90: () = ("4", "A 90 días")
    DAYS_120: () = ("5", "A 120 días")
    OTHER: () = ("6", "Otras")

@dataclass(frozen = True)
class OrderType(EncodedField):
    FIRM: () = ("N", "Normal")
    FAIRE: () = ("F", "Sant Jordi / Feria del libro")
    DEPOSIT: () = ("D", "Pedido en depósito")
    OTHER: () = ("O", "Otros")

@dataclass(frozen = True)
class OrderSource(EncodedField):
    STORE: () = ("N", "Normal")
    CLIENT: () = ("C", "Cliente")

@dataclass(frozen = True)
class DevolutionCause(EncodedField):
    DAMAGED: () = ("0", "Estropeados")
    OLD: () = ("1", "Edición desfasada")
    BAD_DELIVERY: () = ("2", "Incidencia en la entrega")

@dataclass(frozen = True)
class SinliCode:
    """Wrapping class that instantiates all codes"""

    @classmethod
    def get(cls, name: str):
        try:
            return cls.__getattr__(name)
        except:
            return None

    BINDING = Binding()
    TB_REGION = TBRegion()
    STATUS = Status()
    READ_LEVEL = ReadLevel()
    AUDIENCE = Audience()
    PRODUCT_TYPE = ProductType()
    INVOICE_OR_NOTE = InvoiceOrNote()
    CONSIGNMENT_TYPE = ConsignmentType()
    PRICE_TYPE = PriceType()
    FREE_PRICE_TYPE = FreePriceType()
    PAYMENT_TYPE = PaymentType()
    ORDER_TYPE = OrderType()
    ORDER_SOURCE = OrderSource()
    DEVOLUTION_CAUSE = DevolutionCause()
