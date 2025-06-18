from io import open
import os
import json
import unicodedata
import re
from enum import Enum
from typing import List, Dict

# typing
from typing_extensions import Self
from dataclasses import dataclass, field

# module
from .line import LongIdentificationLine, ShortIdentificationLine, Line

@dataclass
class Document:
    long_id_line: LongIdentificationLine = field(default_factory=LongIdentificationLine)
    short_id_line: ShortIdentificationLine = field(default_factory=ShortIdentificationLine)
    doc_lines: List[Line] = field(default_factory=list)
    lines_by_type: Dict[str, Line] = field(default_factory=dict)
    linemap = {}
    doctype_code = ""
    version_code = ""

    def get_doctype_version(self) -> str:
        """
        Produces the sinli version string, like "09"
        from the package of the instance class, such as sinli.libros.v9
        """
        pkg = self.__class__.__module__
        version_code = pkg.split('.')[-1]
        return version_code.replace('v', '').zfill(2)

    def __post_init__(self):
        from .doctype import DocumentType
        for doctype in DocumentType:
            name = doctype.name
            version_map = doctype.value[1]

        self.version_code = self.get_doctype_version()

    @staticmethod
    def normalize_sinli_text(text: str) -> str:
        """
        Normaliza texto para cumplir con estándares SINLI:
        - Remueve acentos y diacríticos
        - Convierte caracteres especiales del español
        - Reemplaza espacios no estándar por espacios normales
        - Maneja caracteres especiales comunes
        """
        if not text:
            return text

        # Reemplazar espacios no estándar (ASCII 160) por espacios normales (ASCII 32)
        text = text.replace('\u00A0', ' ')  # Non-breaking space
        text = text.replace('\u2009', ' ')  # Thin space
        text = text.replace('\u200A', ' ')  # Hair space
        text = text.replace('\u202F', ' ')  # Narrow no-break space

        # Mapeo manual de caracteres especiales comunes en español
        replacements = {
            'ñ': 'n', 'Ñ': 'N',
            'ç': 'c', 'Ç': 'C',
            '¡': '!', '¿': '?',
            'º': 'o', 'ª': 'a',
            'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
            'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
            'ü': 'u', 'Ü': 'U',
            'à': 'a', 'è': 'e', 'ì': 'i', 'ò': 'o', 'ù': 'u',
            'À': 'A', 'È': 'E', 'Ì': 'I', 'Ò': 'O', 'Ù': 'U'
        }

        for old, new in replacements.items():
            text = text.replace(old, new)

        # Normalizar unicode para remover acentos restantes
        text = unicodedata.normalize('NFD', text)
        text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')

        return text

    @classmethod
    def consume_line(cls, line: str, doc: Self) -> Self:
        # files can have empty lines at the end of the document.
        # Just ignore all empty lines without complaining
        if not line:
            return doc  # Retornamos doc en lugar de None

        print(f"\n[DEBUG] line: '{line}'")

        tdoc = line[0:1]
        if tdoc == "I" and not doc.long_id_line.FROM:
            doc.long_id_line = LongIdentificationLine.from_str(line)
            return doc

        elif tdoc == "I" and not doc.short_id_line.FROM:
            doc.short_id_line = ShortIdentificationLine.from_str(line)
            version_str = doc.short_id_line.VERSION if hasattr(doc, "short_id_line") else ""
            doctype_str = doc.short_id_line.DOCTYPE if hasattr(doc, "short_id_line") else ""

            if doctype_str:
                doc.doctype_code = doctype_str
                from .doctype import DocumentType
                doctype_tup = DocumentType[doctype_str]
                doctype_class = doctype_tup.value[1].get(version_str)
                if doctype_class == None:
                    doctype_class = doctype_tup.value[1].get("??")
                    print(f"[WARN] using class {doctype_class} to parse document at version {version_str}. Some fields may be missing or become mixed")
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
        docline = lineclass.from_str(line)
        doc.doc_lines.append(docline)

        # put line in doc dictionary by line type
        if not doc.lines_by_type.get(lineclass.__name__):
            doc.lines_by_type[lineclass.__name__] = []
        doc.lines_by_type[lineclass.__name__].append(docline)

        return doc

    @classmethod
    def consume_lines(cls, lines) -> Self:
        doc = cls()
        for line in lines:
            doc = cls.consume_line(line.strip(), doc)
        return doc

    @classmethod
    def from_str(cls, s: str) -> Self:
        # Normalizar terminadores de línea antes de procesar
        doctype_s = ""
        doc = cls.consume_lines(s.splitlines())
        return doc

    @classmethod
    def from_filename(cls, filename: str, encoding=None, normalize_text=True) -> Self:
        """
        Lee un archivo SINLI con el encoding correcto y normalización opcional.

        Args:
            filename: Ruta del archivo
            encoding: Encoding a usar. Si es None, probará en orden: cp850, windows-1252, iso-8859-15, utf-8
            normalize_text: Si True, normaliza caracteres especiales y espacios
        """
        encodings_to_try = []

        if encoding:
            encodings_to_try = [encoding]
        else:
            # Orden recomendado según documentación SINLI
            encodings_to_try = ['cp850', 'windows-1252', 'iso-8859-15', 'utf-8']

        content = None
        used_encoding = None

        for enc in encodings_to_try:
            try:
                with open(filename, encoding=enc) as f:
                    content = f.read()
                    used_encoding = enc
                    print(f"[INFO] Archivo leído correctamente con encoding: {enc}")
                    break
            except (UnicodeDecodeError, UnicodeError) as e:
                print(f"[WARN] Error con encoding {enc}: {e}")
                continue

        if content is None:
            raise ValueError(f"No se pudo leer el archivo {filename} con ninguno de los encodings probados: {encodings_to_try}")

        # Normalizar texto si se solicita
        if normalize_text:
            content = cls.normalize_sinli_text(content)

        doc = cls()
        for line in content.splitlines():
            line = line.rstrip()  # Solo quitar espacios al final
            if line:  # Ignorar líneas vacías
                doc = cls.consume_line(line, doc)

        return doc

    @classmethod
    def from_document(cls, doc: Self) -> Self:
        new_doc = cls()
        new_doc.long_id_line = doc.long_id_line
        new_doc.short_id_line = doc.short_id_line
        new_doc.doctype_code = doc.doctype_code
        new_doc.doc_lines = doc.doc_lines
        new_doc.lines_by_type = doc.lines_by_type
        return new_doc

    def __str__(self) -> str:
        """
        Exporta el documento con terminadores SINLI correctos (CR+LF)
        """
        slines = []
        slines.append(str(self.long_id_line))
        slines.append(str(self.short_id_line))
        if len(self.doc_lines) > 0:
            slines.append('\r\n'.join([str(line) for line in self.doc_lines]))
        return '\r\n'.join(slines)

    def to_readable(self) -> Self:
        new_doc = self.from_document(self)
        new_doc.long_id_line = self.long_id_line.to_readable()
        new_doc.short_id_line = self.short_id_line.to_readable()
        doc_lines = []
        for line in self.doc_lines:
            doc_lines.append(line.to_readable())
        new_doc.doc_lines = doc_lines

        return new_doc

    def to_json(self) -> str:
        return json.dumps([line.to_readable().to_dict() for line in self.doc_lines])

    def finalize_document(self, doctype_code, version_code):
        """Finalizar documento configurando campos automáticos"""
        # Configurar identificación corta
        self.short_id_line.DOCTYPE = doctype_code
        self.short_id_line.VERSION = version_code

        # Configurar identificación larga
        self.long_id_line.DOCTYPE = doctype_code
        self.long_id_line.VERSION = version_code

        # Calcular LEN
        total_records = len(self.doc_lines) + 2
        self.long_id_line.LEN = total_records

        return self

    def save_to_file(self, filename: str, encoding='cp850', normalize_text=True):
        """
        Guarda el documento en un archivo con formato SINLI correcto

        Args:
            filename: Ruta del archivo de destino
            encoding: Encoding a usar (por defecto cp850 como recomienda SINLI)
            normalize_text: Si True, normaliza el texto antes de guardar
        """
        content = str(self)

        if normalize_text:
            content = self.normalize_sinli_text(content)

        try:
            with open(filename, 'w', encoding=encoding, newline='') as f:
                f.write(content)
            print(f"[INFO] Archivo guardado correctamente en {filename} con encoding {encoding}")
        except UnicodeEncodeError as e:
            print(f"[ERROR] Error de encoding al guardar: {e}")
            # Fallback a windows-1252
            try:
                with open(filename, 'w', encoding='windows-1252', newline='') as f:
                    f.write(content)
                print(f"[INFO] Archivo guardado con encoding fallback windows-1252")
            except Exception as e2:
                raise ValueError(f"No se pudo guardar el archivo: {e2}")
