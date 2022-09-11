from enum import Enum
from dataclasses import dataclass


@dataclass
class Line:

    class Field(Enum):
        EXAMPLE = (1, 7, "Example field located in 1st position with length 7")

    def __str__(self) -> str:
        return str(vars(self))

    def from_dict(self, fields: {}):
        for (key, value) in fields.items():
            setattr(self, key.name, value)
        print(self)
        return self

    @classmethod
    def from_str(cls, line_s: str):
        print(line_s)
        line_dict = {}
        for field in cls.Field:
            start = field.value[0]
            end   = start + field.value[1]
            line_dict[field] = line_s[start:end].strip()
        line = Line()
        return line.from_dict(line_dict)


@dataclass
class IdentificationLine(Line):

    class Field(Enum):
        FROM =    (1, 50, "E-mail origen")
        TO =      (51, 50, "E-mail destino")
        DOCTYPE = (101, 6, "Tipo de Fichero")
        VERSION = (107, 2, "Versión fichero")
