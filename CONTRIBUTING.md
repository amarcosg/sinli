## Adding a new SINLI message

Python allow us for a quasi-config syntax. Once the sinli logic has been implemented, adding more sinli message types requires only a begginer level of python. If you find something confusing, please write to devcontrolATsindominio.net. We really want to make this easy.

1. Create a new directory at `src/sinli/doctype` like `src/sinli/doctype/name`, where `name` must be the message name given at the pdf reference at `/doc/ref-sinli-2020.05.22.pdf`
2. Inside this dir, create a python file named after the version of the sinli message you want to implement. e.g.: `v3.py`. The latest version appears at the pdf also.
3. Sibling to this python file, create an `__init__.py` file with a line such as `from . import v8`. Please change this `v8` to the name of the python file you just created. This is for cohesion of the python package and to enable an easier usage of the library.
4. Once again in the version python file e.g. `v3.py`, we create as many `Line` as the reference tells us. Usualy, there is at least one "Cabecera" (header) line type, and one "Detalle" (payload, body, detail) type. But there can be more. Also, add the line code at `linemap` at the end of the class. Please, take an existing message type file as reference.
5. Do the repetitive job of transcripting the fields from the pdf to your file. Check the notes for how to construct the field's tuple. Please note that the sinli pdf states only length. We code start and length. Please double check for your sums, and test your implementation at the end for all the fields with an export → import cycle.
6. In order to make the library aware of this new message type implementation (congrats!), you need to "register" it at `src/sinli/doctype/__init__.py`. The version value `??` means "all other versions not specified".
7. Finally, push your changes to this repo into a new branch an open a merge request, tagging @raneq for revision ;)

### Notes

* We only implement the most recent versions of the messages. Mr. Sinli told us to do it this way. Messages are "mostly" backwards compatible and they provide no real changelog.
* Sinli versions message tipes, not the whole standard. Thus, there is no such thing as Sinli v3.2, but sinli-libros v8, v9 and sinli-pedido v7, for instance.
* Our implementation of a sinli message's line field looks like:  
```py
# Translation                                   description and comment 
# to English            start  length    type   copied from the pdf
DATE               =  (    91,      8, t.DATE,  "Fecha del documento")
```
* Sinli assumes 8-bit character encodings. In the wild, we found out that Latin-1 is the most common. That is why "byte-length", "character-position" and alike are used interchangeably.
* We use some enums to mark the data type of each field. We have some standard ones: (string, date, currency, country, decimal number, integer number) and some other that the standard encodes with special meanings . For instance, the field "tipo de precio"/"price type" can take `L` or `F` values. However, instead of marking it as an string, we create a field type named PRICE_TYPE:  
```py
@dataclass(frozen = True)
class PriceType(EncodedField):
    FIXED: () = ("F", "Precio final fijo")
    FREE: () = ("L", "Precio final libre")
```
These types are defined at `sinli/common/encoded_values.py`. Please double check that your new encoded type isn't already present with another name, and that the name you chose, isn't already taken by another type.