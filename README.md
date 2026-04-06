# GEO — Asignación territorial de bases nominales

![Estado](https://img.shields.io/badge/estado-activo-brightgreen)
![Enfoque](https://img.shields.io/badge/enfoque-geolocalización-blue)

## Propósito

Construir una infraestructura simple y robusta para asignar ubicación territorial a personas a partir de bases nominales.

Objetivo operativo actual:

> **obtener la cantidad de CUIL por departamento**

## Alcance

El proyecto se enfoca exclusivamente en geolocalización:

* normalización de provincia
* uso de código postal como ancla territorial
* asignación de departamento
* generación de indicadores territoriales

No se evalúan aspectos de negocio ni consistencia general de datos.

## Arquitectura

### `geo_ref`

Tablas de referencia geográfica sin geometrías:

* provincias
* departamentos
* localidades
* códigos postales
* alias

### `geo_work`

Tablas de trabajo:

* staging de bases nominales
* joins territoriales
* agregados por departamento

### `ddbb_analisis`

Esquema reservado para análisis de consistencia por otros equipos.

## Metodología

1. extraer datos mínimos (CUIL, provincia, CP)
2. normalizar provincia
3. normalizar código postal
4. cruzar con tabla de códigos postales
5. asignar departamento
6. medir cobertura

## Estrategia

### Etapa 1

Asignación territorial por código postal.
Nivel objetivo: **departamento**

### Etapa 2

Descenso a localidad en las bases que lo permitan.

### Etapa 3

Descenso a dirección en las bases que lo permitan.

## Proceso transversal

Construcción continua de tablas de alias:

* provincias
* departamentos
* localidades

Permiten acelerar la incorporación de nuevas bases y mejorar calidad progresivamente.

## Esquemas trabajados

| esquema   | nivel actual | estado    |
| --------- | ------------ | --------- |
| ANSES     | departamento | resuelto  |
| Alimentar | departamento | pendiente |
| Educación | dirección    | pendiente |
| Niñez     | departamento | pendiente |
| STESS     | dirección    | pendiente |

## Estado actual

* `geo_ref` cargado y operativo
* `geo_work` definido
* pipeline de ANSES resuelto en el nuevo modelo
* resto de los esquemas pendientes de implementación

## Regla del proyecto

Si no ayuda a ubicar a una persona en el territorio, no importa.
