from .common.encoded_values import SinliCode as c, BasicType as t
from enum import Enum
from dataclasses import dataclass
from pycountry import countries, languages, currencies
import datetime

@dataclass
class Line:
    country_class = countries.get(alpha_2="es").__class__
    lang_class = languages.get(alpha_3="cat").__class__
    currency_class = currencies.get(alpha_3="EUR").__class__

    class Field(Enum):
        EXAMPLE = (1, 7, "Example field located in 1st position with length 7")

    # Export to string

    def __str__(self) -> str:
        field_l = []
        # TODO: check that no fields are missing in the definition
        for field in self.Field:
            deflen = field.value[1]
            val = self.encode(deflen, getattr(self, field.name))
            vallen = len(val)

            if vallen < deflen: # pad with spaces
                val = val + "".join([" " for i in range(0, deflen-vallen)])
            elif vallen > deflen: # truncate
                print(f"[WARN] Unexpected: field {field.name}={val} shouldn't have been longer than {deflen} chars. Truncating to val[0:deflen]")
                val = val[0:deflen]

            field_l.append(val)

        return "".join(field_l)

    def to_csv(self) -> str:
        return ", ".join(vars(self).values())

    def __repr__(self) -> str:
        return repr(vars(self))

    # TODO: converteix a Line de la mateixa classe però valors diferents
    def to_readable(self) -> dict:
        t = self.tables
        ld = vars(self)
        newld = {}
        for k,v in ld.items():
            # resolve tables
            newld[k] = t.get(k).get(v) or t.get(k).get("??") if t and t.get(k) else v
            # trim str blank spaces and left zeroes
            newld[k] = newld[k].strip().lstrip("0")
        return newld

    # Import

    def from_dict(self, fields: {}):
        for (key, value) in fields.items():
            setattr(self, key, value)
        return self

    @classmethod
    def from_str(cls, line_s: str):
        line_dict = {}
        for field in cls.Field:
            start = field.value[0]
            end = start + field.value[1]
            vtype = field.value[2]
            line_dict[field.name] = cls.decode(vtype, line_s[start:end].strip())
            print(f"[DEBUG] {field} → {line_dict[field.name]}")
        line = cls()
        return line.from_dict(line_dict)

    def decode(vtype, value):
        """
        Convert from a sinli field string to a richer type when it applies:
        it returns a str, int, or date.
        """
        #print(f"vtype: {vtype}, value: {value}")
        if vtype == t.STR:
            return value
        elif vtype == t.INT:
            return int(value or '0')
        elif vtype == t.FLOAT:
            return float(value or '0')/100
        elif vtype == t.BOOL:
            return True if "S" else False # "N"
        elif vtype == t.DATE6:
            return datetime.datetime.strptime(value or "011970", "%m%Y")
        elif vtype == t.DATE8:
            return datetime.datetime.strptime(value or "19700101", "%Y%m%d")
        elif vtype == t.LANG:
            return languages.get(alpha_3 = value)
        elif vtype == t.COUNTRY:
            return countries.get(alpha_2 = value)
        elif vtype == t.CURRENCY1:
            return value # FIXME understand meaning of P or E values
        elif vtype == t.CURRENCY3:
            return currencies.get(alpha_3 = value)
        elif vtype in c:
            return value # resolve code only when printing as it's not reversible
        else:
            print(f"[WARN] Unexpected case: var {value} is of type {vtype}")
            return value

    def encode(vlen, value):
        """
        Convert an attribute from an object to a string, appendable to a sinli line
        """
        if type(value) == float:
            return str(int(value * 100))
        elif type(value) == date:
            if vlen == 6: return value.strftime("%m%Y")
            elif vlen == 8: return value.strftime("%Y%m%d")
            else: raise(f"BUG! unexpected situation to SINLI-encode {value} to a length of {vlen} bytes")
        elif type(value) == bool:
            return "S" if value == True else "N" # value == False
        elif type(value) == country_class:
            return value.alpha_2
        elif type(value) == lang_class:
            return value.alpha_3
        elif type(value) == currency_class:
            if vlen == 3:  return value.alpha_3
            #elif vlen == 1: return value # FIXME understand P and E values
        else: # string, integer
            return str(value)

@dataclass
class SubjectLine(Line):

    class Field(Enum):
        TYPE = (0, 1, t.STR, "Tipo de registro (I)")
        FORMAT = (1, 1, t.STR, "Tipo de formato (N=Normalizado ; ?=Libre)")
        DOCTYPE = (2, 6, t.STR, "Nombre del tipo de documento")
        VERSION = (8, 2, t.STR, "Versión del tipo de documento")
        FROM = (10, 8, t.STR, "Identificador ESFANDE del remitente")
        TO = (18, 8, t.STR, "Identificador ESFANDE del destinatario")
        LEN = (26, 5, t.INT, "Cantidad de registros del fichero")
        NUM_TRANS = (31, 7, t.INT, "Número de transmisión s/emisor")
        LOCAL_FROM = (38, 15, t.STR, "Usuario local del emisor")
        LOCAL_TO = (53, 15, t.STR, "Usuario local del destino")
        TEXT = (68, 7, t.STR, "Texto libre")
        FANDE = (75, 5, t.STR, "FANDE")

@dataclass
class IdentificationLine(Line):
    class Field(Enum):
        TYPE = (0, 1, t.STR, "Tipo de registro (I)")
        FROM = (1, 50, t.STR, "E-mail origen")
        TO = (51, 50, t.STR, "E-mail destino")
        DOCTYPE = (101, 6, t.STR, "Tipo de Fichero")
        VERSION = (107, 2, t.STR, "Versión fichero")
        TRANSMISION_NUMBER = (109, 8, t.INT, "Nº de transmisión emisor")
