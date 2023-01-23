from io import open
import os
from enum import Enum

# typing
from typing_extensions import Self
from dataclasses import dataclass, field

# module
from .line import SubjectLine, IdentificationLine, Line

@dataclass
class Document:
    subject_line: SubjectLine = None
    id_line: IdentificationLine = None
    doc_lines: [Line] = field(default_factory=list)
    #linemap: {} = field(default_factory=dict)
    linemap = {}

    def consume_line(line: str, doc: Self) -> Self:
        print(f"[DEBUG] line: {line}")
        #print(f"[DEBUG] sub line: {doc.subject_line}")
        #print(f"[DEBUG] id line: {doc.id_line}")
        #print(f"[DEBUG] doc: {doc}")

        tdoc = line[0:1]
        if tdoc == "I" and not doc.subject_line: # generic processing, we still don't know:  # Subject
            doc.subject_line = SubjectLine.from_str(line)
            #print(f"[DEBUG] doc: {doc}")
            return doc

        elif tdoc == "I" and not doc.id_line: # generic processing, we still don't know:  # Identification
            doc.id_line = IdentificationLine.from_str(line)
            version_str = doc.id_line.VERSION if hasattr(doc, "id_line") else "" # ex: "v9"
            doctype_str = doc.id_line.DOCTYPE if hasattr(doc, "id_line") else ""
            #print(f"[DEBUG] id_line: {doc.id_line}; doctype: {doctype_str}; doc: {doc}")

            if doctype_str: # we just processed the identification line
                from .doctype import DocumentType
                doctype_tup = DocumentType[doctype_str]
                doctype_class = doctype_tup.value[1][version_str]
                newdoc = doctype_class.from_document(doc)
                doc = newdoc
                print(f"[DEBUG] linemap: {doc.linemap.items()}")

            return doc

        lineclass = doc.linemap.get(tdoc)
        if lineclass == None:
            lineclass = doc.linemap.get("")
            print(f"[DEBUG] linemap: {doc.linemap.items()}")
            print(f"[DEBUG] lineclass: {lineclass}")
            if lineclass == None:
                print(f"[DEBUG] linemap: {doc.linemap.items()}")
                raise Exception(
                    "SINLI syntax error", f"El codi de registre {tdoc} no es reconeix i no s'ha definit cap classe sense prefix"
                )
        # we have a valid lineclass already
        doc.doc_lines.append(lineclass.from_str(line))
        return doc

    def consume_lines(lines, doc) -> Self:
        first = True
        for line in lines:
            if first:
                first = False
                continue
            doc = consume_line(line, doc)
        return doc

    @classmethod
    def from_str(cls, s: str) -> Self:
        doc = cls()
        doctype_s = ""
        cls.consume_lines(s.split_lines(), doc)
        return doc

    @classmethod
    def from_filename(cls, filename: str) -> Self:
        """
        El juego de caracteres recomendado es el 850 OEM – Multilingual Latín I // (DOS Latin 1 = CP 850)
        https://docs.python.org/3/library/codecs.html#module-codecs
        """
        doc = cls()
        with open(filename, encoding="cp850") as f:
            for line in f:
                line = line.strip()
                doc = cls.consume_line(line, doc)
        return doc

    @classmethod
    def from_document(cls, doc: Self) -> Self:
        new_doc = cls()
        new_doc.subject_line = doc.subject_line
        new_doc.id_line = doc.id_line
        new_doc.doc_lines = doc.doc_lines
        return new_doc

    def __str__(self) -> str:
        slines = []
        slines.append(str(self.subject_line))
        slines.append(str(self.id_line))
        if len(self.doc_lines) > 0:
            slines.append(os.linesep.join([str(line) for line in self.doc_lines]))
        return os.linesep.join(slines)
