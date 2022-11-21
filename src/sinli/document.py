# external general
from io import open
import os
from enum import Enum

# typing
from typing_extensions import Self
from dataclasses import dataclass, field

# module
from line import IdentificationLine, Line


@dataclass
class Document:
    id_line: IdentificationLine = None
    header_line: Line = None
    detail_lines: [Line] = field(default_factory=list)
    other_lines: [Line] = field(default_factory=list)

    class Header(Line):
        pass

    def read_header_line(self, line: str) -> Line:
        # raise NotImplementedError("Depends on document type. Implement in subclasses")
        return self.Header.from_str(str)

    def read_detail_line(self, line: str) -> Line:
        raise NotImplementedError("Depends on document type. Implement in subclasses")

    def read_other_line(self, line: str) -> Line:
        raise NotImplementedError("Depends on document type. Implement in subclasses")

    def process_line(self, line: str):
        tdoc = line[0:1]
        if tdoc == "I":  # Identification
            self.id_line = IdentificationLine.from_str(line)
        elif tdoc == "C":  # header (Cabecera)
            self.header_line = self.read_header_line(line)
        elif tdoc == "D":  # Detail
            self.detail_lines.append(self.read_detail_line(line))
        # other #
        elif (
            tdoc == "T"  # Totals
            or tdoc == "V"  # tax (IVA)
            or tdoc == "R"  # Refusal (Rechazo)
            or tdoc == "M"  # Message
            or tdoc == "E"  # status (Estado)
            or tdoc == "P"  # Payment time (vencimiento)
            or tdoc
            == "H"  # dropsHiping (entregas directas de distribuidoras a cliente final en nombre de la librería que recibe el pedido)
        ):
            self.other_lines.append(self.read_other_line(line))
        else:  # error
            raise SyntaxError(
                "SINLI syntax error", f"El codi de registre {tdoc} no es reconeix"
            )

    @classmethod
    def from_str(cls, s: str) -> Self:
        doc = Document()
        doctype_s = ""
        for line in s.split_lines():
            doc.process_line(line)
            if doc.DOCTYPE:
                break
        if not doc.DOCTYPE:
            return doc
        doctype_s = doc.DOCTYPE
        doctype_e = DocumentDoctype[doctype_s]
        specific_doc = doctype_e.value[2]()
        # TODO crear mètode per llegir línies de detall, que no comencen per D i que podrien començar per alguna lletra reservada (!)
        # TODO llegir les línies úniques, que porten lletra davant, i un cop això, passar totes les línies restants amb process_detail_line
        return specific_doc

    @classmethod
    def from_filename(cls, filename: str) -> Self:
        """
        El juego de caracteres recomendado es el 850 OEM – Multilingual Latín I // (DOS Latin 1 = CP 850)
        https://docs.python.org/3/library/codecs.html#module-codecs
        """
        doc = Document()
        with open(filename, encoding="cp850") as f:
            for line in f:
                doc.process_line(line)
        return doc

    def __str__(self) -> str:
        slines = []
        slines.append(str(self.id_line))
        slines.append(str(self.header_line))
        if len(self.detail_lines > 0):
            slines.append(os.linesep.join([str(line) for line in self.detail_lines]))
        if len(self.other_lines > 0):
            slines.append(os.linesep.join([str(line) for line in self.other_lines]))
        return os.linesep.join(slines)
