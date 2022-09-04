class Line:
    def __init__(self):
        pass

    class Field(Enum):
        EXAMPLE: (1, 7, "Example field located in 1st position with length 7")

    def load_from_dict(self, fields: {}) -> self:
        raise NotImplementedError("Depends on line type. Implement in subclasses")

    def __str__(self) -> str:
        raise NotImplementedError("Depends on line type. Implement in subclasses")

    def from_str(self, line: str, field_enum: Enum):
        line_dict = {}
        for field in field_enum:
            line_dict[field] = line[field.value[0], field.value[0]+field.value[1]].strip()
        return self.from_dict()

# TODO consider converting to a @dataclass
class IdentificationLine(Line):
    def __init__(self):
        self.from_email = ""
        self.to_email = ""
        self.version = 0

    #TODO def load_from_dict / either method or from_dict as a @classmethod

    class Field(Enum):
        FROM =    (1, 50, "E-mail origen")
        TO =      (51, 50, "E-mail destino")
        DOCTYPE = (101, 6, "Tipo de Fichero")
        VERSION = (107, 2, "Versión fichero")


