# geo_work — Trabajo geo

## Propósito

Ejecutar el procesamiento territorial de las bases nominales.

Este esquema contiene todas las tablas derivadas.

---

## Estructura

Para cada base:

* *_base → extracto mínimo
* *_join → resultado del cruce territorial
* *_agg_depto → agregado final

---

## Flujo

1. cargar datos desde esquema fuente
2. normalizar provincia
3. normalizar CP
4. join con geo_ref.codigos_postales
5. asignar departamento
6. generar agregados

---

## Características

* tablas recalculables
* no modifica fuentes
* permite auditoría de resultados

---

## Resultado esperado

* asignación territorial a nivel departamento
* tabla lista para análisis o visualización

---

## Regla

Todo procesamiento geo ocurre en este esquema.

Las tablas originales no se modifican.
