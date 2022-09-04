from io import open
import os

class Document:
    def __init__(self):
        self.id_line: IdentificationLine = None
        self.header_line: Line = None
        self.detail_lines: [Line] = []
        self.other_lines: [Line] = []

    def read_header_line(self, line: str) -> Line:
        raise NotImplementedError("Depends on document type. Implement in subclasses")

    def read_detail_line(self, line: str) -> Line:
        raise NotImplementedError("Depends on document type. Implement in subclasses")

    def read_other_line(self, line: str) -> Line:
        raise NotImplementedError("Depends on document type. Implement in subclasses")

    class Type(Enum):
        ABONO  = "Albarán o Factura de Abono"
        CAMPRE = "Cambios de precio"
        ESTADO = "Cambios de estado"
        LIBROS = "Ficha del Libro"
        MENSAJ = "Mensaje"

    def process_line(self, line: str):
        l = LineReader(line)
        tdoc = l.read(1)
        if tdoc == "I": # Identification
            self.id_line = IdentificationLine(line)
        elif tdoc == "C": # header (Cabecera)
            self.header_line = self.read_header_line(line)
        elif tdoc == "D": # Detail
            self.detail_lines.append(self.read_detail_line(line))
        # other #
        elif (
            tdoc == "T" or   # Totals
            tdoc == "V" or   # tax (IVA)
            tdoc == "R" or   # Refusal (Rechazo)
            tdoc == "M" or   # Message
            tdoc == "E" or   # status (Estado)
            tdoc == "P" or   # Payment time (vencimiento)
            tdoc == "H"      # dropsHiping (entregas directas de distribuidoras a cliente final en nombre de la librería que recibe el pedido)
        ):
            self.other_lines.append(self.read_other_line(line))
        else: # error
            raise SyntaxError("SINLI syntax error", f"El codi de registre {tdoc} no es reconeix")


    def from_str(s: str) -> Document :
        for line in s.split_lines():
            self.process_line(line)


    def from_filename(filename: str) -> Document:
        """
        El juego de caracteres recomendado es el 850 OEM – Multilingual Latín I // (DOS Latin 1 = CP 850)
        https://docs.python.org/3/library/codecs.html#module-codecs
        """
        with open(filename, encoding="cp850") as f:
            for line in f:
                self.process_line(line)

    def __str__(self) -> str:
        slines = []
        slines.append(str(self.id_line))
        slines.append(str(self.header_line))
        if len(self.detail_lines > 0): slines.append(os.linesep.join([str(line) for line in self.detail_lines]))
        if len(self.other_lines > 0):  slines.append(os.linesep.join([str(line) for line in self.other_lines]))
        return os.linesep.join(slines)


