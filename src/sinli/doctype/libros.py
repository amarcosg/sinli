from ..document import Document
from ..line import Line
from enum import Enum


class LibrosDoc(Document):
    class Header(Line):
        class Field(Enum):
            TYPE = (0, 1, "Tipo de Registro")
            PROVIDER = (1, 40, "Nombre del proveedor")
            CURRENCY = (41, 42, "Moneda")

    class Body(Line):
        class Field(Enum):
            EAN = (1, 18, "EAN")
            ISBN_INVOICE = (19, 17, "ISBN (Con guiones) Facturación")
            ISBN_COMPLETE = (36, 17, "ISBN (Con guiones) Obra completa")
            ISBN_VOLUME = (53, 17, "ISBN (Con guiones) Tomo")
            ISBN_ISSUE = (70, 17, "ISBN (Con guiones) Fascículo")
            REFERENCE = (87, 15, "Referencia")
            TITLE_FULL = (102, 80, "Título completo")
            SUBTITLE = (182, 80, "Subtítulo")
            AUTHORS = (262, 150, "Autor/es (Apellidos, Nombre)")
            PUB_COUNTRY = (412, 2, "País de publicación")
            """
            EDITOR       = (    ,     , "")
            BINDING= (    ,     , "")
            LANGUAGE= (    ,     , "")
            EDITION= (    ,     , "")
            PUB_DATE= (    ,     , "")
            PAGE_NUM= (    ,     , "")
            WIDTH_MM= (    ,     , "")
            HEIGH_MM= (    ,     , "")
            TOPICS= (    ,     , "")
            KEYWORDS= (    ,     , "")
            STATUS= (    ,     , "")
            TYPE= (    ,     , "")
            PRICE_PVP= (    ,     , "")
            PRICE_PV= (    ,     , "")
            TAX_IVA= (    ,     , "")
            PRICE_TYPE= (    ,     , "")
            COLLECTION= (    ,     , "")
            COL_NUM= (    ,     , "")
            VOL_NUM= (    ,     , "")
            COVER_IMAGE= (    ,     , "")
            COVER_ILLUSTRATOR= (    ,     , "")
            INNER_ILLUSTRATOR= (    ,     , "")
            COLOR_ILL_NUM= (    ,     , "")
            TRANSLATORS= (    ,     , "")
            LANG_ORIG= (    ,     , "")
            THICK_MM= (    ,     , "")
            WEIGHT_G= (    ,     , "")
            AUDIENCE= (    ,     , "")
            READ_LEVEL= (    ,     , "")
            TB_LEVEL= (    ,     , "")
            TB_COURSE= (    ,     , "")
            TB_SUBJECT= (    ,     , "")
            TB_REGION= (    ,     , "")
            IBIC_VERSION= (    ,     , "")
            IBIC_TOPICS= (    ,     , "")
            IBIC_REL= (    ,     , "")
            THEMA_VERSION= (    ,     , "")
            THEMA_TOPICS= (    ,     , "")
            THEMA_REL= (    ,     , "")
            DATE_LAUNCH= (    ,     , "")
            DATE_AVAILABLE= (    ,     , "")
            URL= (    ,     , "")
            SUMMARY= (    ,     , "")
            """
