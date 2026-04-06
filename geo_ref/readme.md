# geo_ref — Referencia geográfica

## Propósito

Centralizar las tablas de referencia utilizadas para la asignación territorial.

Este esquema funciona como catálogo maestro del proyecto geo.

## Contenido

* provincias
* departamentos
* localidades
* códigos postales
* tablas de alias

## Uso

Se utiliza para:

* normalizar provincias
* asignar departamentos a partir de CP
* servir como base común para todos los esquemas nominales

## Características

* sin geometrías
* codificación estable
* independiente de las bases nominales

## Estado

Tablas cargadas y operativas:

* provincias
* departamentos
* localidades
* códigos postales

Observaciones:

* localidades normalizadas para permitir múltiples departamentos cuando corresponde
* códigos postales complementados con CABA

## Regla

No utilizar para:

* staging
* resultados de joins
* experimentación

## Rol en el pipeline

`geo_ref` es la base sobre la cual `geo_work` ejecuta joins territoriales.
