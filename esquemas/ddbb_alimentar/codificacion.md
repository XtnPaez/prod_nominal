# ddbb_alimentar — CODIFICACIÓN GEO

## Estado general

Tipo: no codificado

Descripción:
El esquema no utiliza claves oficiales para provincias, departamentos o localidades.
Toda la información geográfica está en texto libre.

---

## Evaluación por nivel

### Provincias

Campos:

* titulares.provincia
* unidades_convivencia.provincia
* titulares_serie.provincia_titular

Tipo:
no codificado

Problema:

* nombres inconsistentes
* posibles variantes ("Bs As", "Buenos Aires", etc.)

---

### Localidades / Municipios

Campos:

* titulares.localidad
* unidades_convivencia.localidad
* titulares_serie.municipio_titular

Tipo:
no codificado

Problemas:

* mezcla de conceptos (localidad vs municipio)
* ambigüedad (nombres repetidos en distintas provincias)
* falta de jerarquía geográfica

---

### Dirección

Campos:

* calle
* numero
* piso
* depto
* cod_postal

Tipo:
no codificado

Problemas:

* calle en texto libre
* numero como varchar
* posible ruido ("S/N", rangos, etc.)
* código postal no validado

---

## Comparación con fuentes oficiales

Referencias esperadas:

* provincias (código INDEC)
* departamentos (código jerárquico)
* localidades (nomenclador oficial)

Estado:

* no hay correspondencia directa
* no existen claves de enlace

---

## Impacto en geocodificación

* requiere normalización previa obligatoria
* alto riesgo de ambigüedad
* posible pérdida de precisión si no se corrige

---

## Nivel de esfuerzo requerido

alto

Motivo:

* limpieza de texto
* estandarización de provincias
* desambiguación de localidades
* parsing de direcciones

---

## Conclusión

El esquema tiene buena disponibilidad de datos geográficos,
pero sin codificación.

Toda explotación geográfica depende de un proceso ETL previo.
