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
