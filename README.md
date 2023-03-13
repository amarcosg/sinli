# SINLI

## Introduction and purpose

This package is a libre-free implementation of the [SINLI standard](http://www.fande.es/normalizacion/sinli_indicedocumentos.html).
It builds on top of email to allow applications to communicate all sort of operations of the book sector in Spain.

There are 3 main roles in this sector:
- bookshops
- distributors
- editors

There are some other implementations of this standard, but all of those we know about are closed-source, sell for an expensive yearly license, and work only in Window$ Opressing System.
Thus, small bookshops, independent editors and distributors get tied to these disrespectful technologies, and represent a huge economic drag for them.

At [Devcontrol](https://framagit.org/devcontrol/) we are coding for an initiative supported by a union of these independent entities and led by [Descontrol](https://descontrol.cat).
This initiative is sharing the solution to a shared problem, and is adapting the Odoo ERP (business managing software) to be used for both distributors and bookshops. In order to be a complete replacement of those closed-source apps, we are trying to make Odoo speak SINLI ;)

## Organisation and code paradigm

This repository is organized following the [guidelines for python packages](https://packaging.python.org/en/latest/tutorials/packaging-projects/#creating-the-package-files). The actual code source is inside `src/sinli/`.

This project is object oriented, and makes use of python [@dataclass](https://docs.python.org/3/library/dataclasses.html) decorator and [Enum](https://docs.python.org/3/howto/enum.html) class.
Namely, the main classes are `Document` and `Line`. Each SINLI message is a `Document`, and each one has many `Line`s. These two classes must be subclassed for each different document type in a separate file, located inside `src/sinli/doctype`.
Additionaly, `Line` has 2 subclasses, `SubjectLine` and `IdentificationLine` that share a common format for all document types.

## SINLI details

### Transport

SINLI uses the email as a common transport, but can be also fetched via FTP or other means if the parties agree to do so.

### Structure

SINLI documents or messages are text-based, one file each, and line-based. There is no special syntax, instead, each line is to be processed separately,
and the different fields in each line are split by their byte position in the line. Therefore, each field has a fixed lenght. In fields where the data has variable lenght, the data is padded with spaces in case of text, and ascii 0 characters in case of numerical fields.

### SINLI versions

There are no standard-wide versions in SINLI. Instead, each message type has its own version number. New versions are meant to be backwards compatible to older clients. The standaring committee tries to only add fields at the end of the line, not modifying the lengths or meanings of the existing ones. However, they do not commit to it and call for "get what you can" and for a human check before importing to a system. We support implementing different versions of a document type and parsing them accordingly, but will only implement older versions in a case by case basis. SINLI editors do not like developers implementing old versions because in their opinion, it makes users lazier to update. Because of this and other reasons, older versions specifications are not publicly available.

## Goals

### Generic

- [x] Basic architecture for reading documents and lines
- [x] Read LIBRO doctype
- [x] Prepare the repo as an importable python package
- [x] Implement document writing
- [x] Manage different document versions
- [x] Manage table-based fields
- [x] Manage different data types

### For bookshops

- [x] Albarán de pedido del cliente
- [ ] Albarán de devolución
- [x] Mensaje de texto

### For distributors

- [x] Ficha del libro
- [ ] Cambio de precio
- [x] Albarán de envío
- [x] Factura
- [x] Mensaje de texto
