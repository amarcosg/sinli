from io import open

class Document:
    def __init__(self, id_line: IdentificationLine, header_line: HeaderLine, detail_lines: [DetailLine], other_lines: [GenericLine]):
        self.id_line = id_line
        self.header_line = header_line
        self.detail_lines = detail_lines
        self.other_lines = other_lines

    def process_line(self, line: str):
        l = LineReader(line)
        tdoc = l.read(1)
        if tdoc == "I": # Identification
            pass
        elif tdoc == "C": # header (Cabecera)
            pass
        elif tdoc == "D": # Detail
            pass
        #elif tdoc in ["T", "V", "R", "M", "E", "P", "H"]: # other
        # other #
        elif tdoc == "T": # Totals
            pass
        elif tdoc == "V": # tax (IVA)
            pass
        elif tdoc == "R": # Refusal (Rechazo)
            pass
        elif tdoc == "M": # Message
            pass
        elif tdoc == "E": # status (Estado)
            pass
        elif tdoc == "P": # Payment time (vencimiento)
            pass
        elif tdoc == "H": # dropsHiping (entregas directas de distribuidoras a cliente final en nombre de la librería que recibe el pedido)
            pass
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

