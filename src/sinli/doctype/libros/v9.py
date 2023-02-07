from ...document import Document
from ...line import Line
from enum import Enum
from dataclasses import dataclass, field

@dataclass
class LibrosDoc(Document):
    class Header(Line):
        class Field(Enum):
            TYPE = (0, 1, "Tipo de Registro")
            PROVIDER = (1, 40, "Nombre del proveedor")
            CURRENCY = (41, 42, "Moneda")

    class Book(Line):
        class Field(Enum):
            EAN = (0, 18, "EAN")
            ISBN_INVOICE = (18, 17, "ISBN (Con guiones) Facturación")
            ISBN_COMPLETE = (35, 17, "ISBN (Con guiones) Obra completa")
            ISBN_VOLUME = (52, 17, "ISBN (Con guiones) Tomo")
            ISBN_ISSUE = (69, 17, "ISBN (Con guiones) Fascículo")
            REFERENCE = (86, 15, "Referencia")
            TITLE_FULL = (101, 80, "Título completo")
            SUBTITLE = (181, 80, "Subtítulo")
            AUTHORS = (261, 150, "Autor/es (Apellidos, Nombre)")
            PUB_COUNTRY = (411, 2, "País de publicación")
            EDITOR_ISBN = (413, 8, "Editorial (Código ISBN)")
            EDITOR = (421, 40, "Editorial (Nombre)")
            BINDING = (461, 2, "Código de tipo de encuadernación")
            LANGUAGE = (463, 3, "Lengua de publicación (Código de la tabla ISO 639-2)")
            EDITION = (466, 2, "Número de edición")
            PUB_DATE= (468, 6, "Fecha de publicación en formato mmaaaa")
            PAGE_NUM = (474, 4, "Número de páginas")
            WIDTH_MM = (478, 4, "Ancho en mm.")
            HEIGH_MM = (482, 4, "Alto en mm.")
            TOPICS = (486, 20, "Temas separados por ';' en códigos CDU o ISBN")
            KEYWORDS = (506, 80, "Palabras clave o descriptores, separadas por '/'")
            STATUS = (586, 1, "Código de situación en catálogo")
            TYPE = (587, 2, "Código de tipo de producto")
            PRICE_PVP = (589, 10, "PVP sin IVA en EUR (sin puntuación)")
            PRICE_PV = (599, 10, "PV con IVA en EUR (sin puntuación)")
            TAX_IVA = (609, 5, "Porcentaje de IVA (ej: 4, 16, ...)")
            PRICE_TYPE = (614, 1, "Tipo de precio. F = Fijo, L = Libre. Si es L, el precio sin IVA será el precio de cesión, y el precio con IVA, el precio de sesión más el IVA correspondiente")
            COLLECTION = (615, 40, "Nombre de la colección")
            COL_NUM = (655, 10, "Número de colección")
            VOL_NUM = (665, 4, "Número de volumen")
            COVER_IMAGE = (669, 1, "Fuente de la imagen de portada y/u otras. N = No; A = Anexada, debe ser en jpg, pesar menos de 500 KB, y el nombre del fichero adjunto con la/las imágenes será el código EAN13; U = URL")
            COVER_ILLUSTRATOR = (670, 150, "Lista de ilustradores de la cubierta en formato 'Apellidos, Nombre' y separados por '/'")
            INNER_ILLUSTRATOR = (820, 150, "Lista de ilustradores del interior en formato 'Apellidos, Nombre' y separados por '/'")
            COLOR_ILL_NUM = (970, 5, "Número de ilustraciones a color")
            TRANSLATORS = (975, 150, "Lista de personas traductoras en formato 'Apellidos, Nombre' y separados por '/'")
            LANG_ORIG = (1125, 3, "Idioma original en código ISO 639-2")
            THICK_MM = (1128, 3, "Grosor en milímetros")
            WEIGHT_G = (1131, 6, "Peso en gramos")
            AUDIENCE = (1137, 3, "Código de audiencia objetivo")
            READ_LEVEL = (1140, 1, "Código de nivel de lectura")
            TB_LEVEL = (1141, 15, "Libro de texto: nivel (infantil, primaria, eso, bachillerato, fp, universitaria)")
            TB_COURSE = (1156, 80, "Libro de texto: Curso")
            TB_SUBJECT = (1236, 80, "Libro de texto: Asignatura")
            TB_REGION = (1316, 53, "Libro de texto: Lista de códigos de comunidades autónoma, separados por '/'.")
            IBIC_VERSION = (1369, 3, "iBIC: Tipo de versión. ej: 2.1")
            IBIC_TOPICS = (1372, 50, "iBIC: Lista de temas (materias) separados por ';'")
            IBIC_REL = (1422, 1, "iBIC: Asignación. 0 = Nativo; 1 = Mapeado")
            THEMA_VERSION = (1423, 3, "THEMA: tipo de versión. ej: 1.3")
            THEMA_TOPICS = (1426, 50, "THEMA: lista de temas (materias) separados por ';'")
            THEMA_REL = (1476, 1, "THEMA: Asignación. 0 = Nativo; 1 = Mapeado")
            DATE_LAUNCH = (1477, 8, "Fecha de puesta en venta o lanzamiento, en formato AAAAMMDD")
            DATE_AVAILABLE = (1485, 8, "Fecha de disponibilidad de existencias, en formato AAAAMMDD")
            URL = (1493, 199, "Dirección URL. Se recomienda nombrar al menos con el EAN en las primeras posiciones")
            SUMMARY = (1692, 1108, "Resumen, sinopsis")

        tables = {
            Field.BINDING: {
                "??": "Sin especificar",
                "01": "Tela",
                "02": "Cartoné",
                "03": "Rústica",
                "04": "Bolsillo",
                "05": "Troquelado",
                "06": "Espiral",
                "07": "Anillas",
                "08": "Grapado",
                "09": "Fascículo encuadernable",
                "10": "Otros",
            }
        }

    linemap = {
        "C": Header,
        "": Book
    }

