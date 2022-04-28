## Documentos contemplados por QFACWIN

### Documentos recibidos del proveedor:

- **ENVIO** versión 06 y 08 - Albarán del proveedor o factura directa del proveedor (factura sin albaranes). Al incorporar el documento se añaden los libros nuevos y se asignan a la categoría indicada en la configuración con el código de artículo igual al ISBN.
- **FACTUL** versión 01 - Factura por albaranes del proveedor (incluye albaranes enviados previamente).
- **ENTPAP** versión 01 - Albarán del proveedor o factura directa del proveedor de artículos de papelería (factura sin albaranes). Si el artículo no existe en el programa (el proceso busca por EAN) lo añade con el código P seguido del EAN.
- **ABONO** - Abono de albarán (A) o factura (F).
- **LIBROS** versión 08 - Fichas de libro. Debe incorporarse después de las compras: actualiza y completa la información de los libros que están dados de alta en el programa. Si en la pestaña Configuración marca la casilla Sólo añadir artículos de albaranes y facturas, añadirá o modificará los datos de artículos que ya están dados de alta en el programa sin añadirlos todos.
- **CAMPRE** versión 03 - Cambios de precio.
- **MENSAJ** versión 01 - Mensajes del proveedor.

### Documentos a enviar al proveedor:

- **PEDIDO** versión 06 - Pedido.
- **DEVOLU** versión 02 - Albarán de devolución (importe total negativo).
- **MENSAJ** versión 01 - Mensajes al proveedor.

Los documentos de SINLI (adjuntos a los emails de SINLI) son documentos de texto y pueden visualizarse abriéndolos con el Bloc de notas de Windows o cualquier editor de texto.
*ATENCIÓN*: no editarlos y guardarlos ya que podrían perder el formato.

## Cómo identificar el contenido de los mensajes de SINLI

El asunto de los mensajes con un documento SINLI puede resultar extraño pero se trata una codificación que nos permite identificar el contenido y el tipo de documento SINLI que se adjunta.
La codificación del asunto incluye la identificación FANDE (buzón) del proveedor (emisor) y la propia (receptor) así como el tipo de documento adjunto y su versión. FANDE y ESFANDE son textos fijos que se repiten siempre en las mismas posiciones del asunto de los mensajes de SINLI.
La estructura del contenido de los mensajes de SINLI es la siguiente:
`ESFANDE + Id SINLI del proveedor + ESFANDE + Id SINLI propio + Tipo Documento + Versión del documento + FANDE`

Lo veremos más claro con algunos ejemplos:

### Ejemplo 1:
Asunto: `ESFANDE LIB00363 ESFANDE L0003321 LIBROS 07 FANDE`

id SINLI proveedor: LIB00363 en este caso
id SINLI propio (Librería Q): L0003321
Tipo documento: LIBROS en este caso se trata de Fichas de libro
Versión del documento: 07 en este caso

### Ejemplo 2:
Asunto: `ESFANDE LIB00363 ESFANDE L0003321 FACTUL 01 FANDE`

id SINLI proveedor: LIB00363 en este caso
id SINLI Librería Q: L0003321
Tipo documento: FACTUL en este caso se trata de facturas correspondientes a albaranes ya enviados.
Versión del documento: 01 en este caso
