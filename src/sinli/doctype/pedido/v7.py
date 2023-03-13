from ...document import Document
from ...line import Line
from enum import Enum
from dataclasses import dataclass, field

@dataclass
class PedidoDoc(Document):
    class Header(Line):
        class Field(Enum):
            TYPE = (0, 1, "Tipo de registro")
            CUSTOMER = (1, 40, "Nombre del cliente")
            PROVIDER = (41, 40, "Nombre del proveedor")
            ORDER_DATE = (81, 8, "Fecha del pedido")
            ORDER_CODE = (89, 10, "Código del pedido")
            ORDER_TYPE = (99, 1, "Tipo del pedido. Valores: N (normal) F (feria/sant jordi) D (depósito) O (otros)")
            CURRENCY = ( 100, 1, "Moneda")
            PRINT_ON_DEMAND = (101, 1, "Impresión bajo demanda: S/N")
            ASKED_DELIVERY_DATE = (102, 8, "Fecha de entrega solicidtada")
            MAX_DELIVERY_DATE = (110, 8, "Última fecha de entrega admitida")
            STRICT_MAX_DELIVERY_DATE = (118, 1, "Caducidad última fecha entrega: S/N. Si se entrega después del límnite, será rechazada?")

    class DeliveryPlace(Line):
        class Field(Enum):
            TYPE = (0, 1, "Tipo de registro")
            NAME = (1, 50, "Nombre del punto de entrega")
            ADDRESS = (51, 80, "Dirección")
            POSTAL_CODE = (131, 5, "Código postal")
            MUNICIPALITY = (136, 50, "Municipio")
            PROVINCE = (186, 40, "Provincia")

    class Detail(Line):
        class Field(Enum):
            TYPE = (0, 1, "Tipo de registro")
            ISBN = (1, 17, "ISBN")
            EAN = (18, 18, "EAN")
            REFERENCE = (36, 15, "Reference")
            TITLE = (51, 50, "Título")
            QUANTITY = (101, 6, "Cantidad")
            PRICE = (107, 10, "Precio")
            INCLUDE_PENDING = (117, 1, "¿Quiere pendientes? S/N")
            ORDER_SOURCE = (118, 1, "Origen del pedido: N (normal), C (cliente)")
            EXPRESS = (119, 1, "Envío en menos de 24h con gastos de envío especiales S/N")
            ORDER_CODE = (120, 10, "Código de pedido")

    class SimpleDetail(Line):
        class Field(Enum):
            TYPE = (0, 1, "Tipo de registro")
            TEXT = (1, 80, "Texto libre. En caso de desconocer los identificadores de los libros")

    class Dropshipping(Line):
        class Field(Enum):
            TYPE = (0, 1, "Tipo de registro")
            FINAL_CLIENT = (1, 50, "Destino (particular, colegio, otros)")
            RECEIVER_NAME = (51, 50, "Nombre receptor entrega")
            PREFIX = (101, 4, "Prefijo. En formato +AAA")
            PHONE = (105, 9, "Teléfono, sin puntos ni guiones")
            ADDRESS = (114, 80, "Dirección")
            EMAIL = (194, 40, "Correo electrónico")
            POSTAL_CODE = (234, 11, "Código postal")
            MUNICIPALITY = (244, 50, "Localidad")
            PROVINCE = (294, 40, "Provincia")
            COUNTRY = (334, 40, "País")
            CC = (374, 2, "Código ISO de país")
            OBSERVATIONS = (376, 38, "Observaciones")

    linemap = {
        "C": Header,
        "E": DeliveryPlace,
        "D": Detail,
        "M": SimpleDetail,
        "H": Dropshipping,
    }
