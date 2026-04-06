# geo_ref — Referencia geográfica

## Propósito

Centralizar las tablas de referencia utilizadas para la asignación territorial.

Este esquema funciona como catálogo maestro.

---

## Contenido

* provincias
* departamentos
* localidades
* códigos postales
* tablas de alias

---

## Uso

Se utiliza para:

* normalizar provincias
* asignar departamentos a partir de CP
* servir como base común para todos los esquemas

---

## Características

* sin geometrías
* codificación estable
* independiente de las bases nominales

---

## Regla

No utilizar para:

* staging
* resultados de joins
* experimentación

---

## Rol en el pipeline

geo_ref es la base sobre la cual:

* geo_work ejecuta joins
* las bases nominales se traducen a territorio

---

## Estado

Tablas cargadas y operativas:

- provincias
- departamentos
- localidades (normalizadas a nivel comuna en CABA)
- códigos postales (incluye CABA)

Listas para uso en joins territoriales.
