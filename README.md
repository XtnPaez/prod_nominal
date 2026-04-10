# GEO — Asignación territorial de bases nominales

![Estado](https://img.shields.io/badge/estado-activo-brightgreen)
![Enfoque](https://img.shields.io/badge/enfoque-geolocalización-blue)
![Etapa](https://img.shields.io/badge/etapa-departamento-orange)
![ANSES](https://img.shields.io/badge/ANSES-resuelto-success)
![Alimentar](https://img.shields.io/badge/Alimentar-operativo-yellow)
![Educación](https://img.shields.io/badge/Educación-operativo-yellow)
![STESS](https://img.shields.io/badge/STESS-postergado-lightgrey)

---

## Propósito

Construir una infraestructura simple y robusta para asignar ubicación territorial a personas a partir de bases nominales.

Objetivo operativo:

> **obtener la cantidad de CUIL por departamento**

---

## Alcance

El proyecto se enfoca exclusivamente en geolocalización:

* normalización de provincia
* uso de estructuras administrativas
* asignación de departamento
* generación de indicadores territoriales

No se evalúan aspectos de negocio ni consistencia general de datos.

---

## Arquitectura

### `geo_ref`

Tablas de referencia geográfica sin geometrías:

* provincias
* departamentos
* localidades
* códigos postales
* alias

Estado: **cargado y operativo**

---

### `geo_work`

Tablas de trabajo:

* staging de bases nominales
* joins territoriales
* agregados por departamento

Estado: **operativo**

---

### `ddbb_analisis`

Esquema reservado para análisis de consistencia por otros equipos.

---

## Metodología

1. extraer datos mínimos (CUIL, provincia, variables geo)
2. normalizar provincia
3. seleccionar estrategia de asignación (CP / partido / localidad)
4. asignar departamento
5. medir cobertura

---

## Estrategia

### Etapa 1 — Departamento

Asignación territorial usando:

* código postal
* partido/departamento
* localidad (fallback)

### Etapa 2 — Localidad

Descenso a localidad en las bases que lo permitan

### Etapa 3 — Dirección

Descenso a dirección en las bases que lo permitan

---

## Proceso transversal

Construcción continua de tablas de alias:

* provincias
* departamentos
* localidades

Permiten:

* mejorar cobertura
* normalizar nuevas bases
* evitar reprocesos

---

## Esquemas trabajados

| esquema   | nivel actual | estado     |
| --------- | ------------ | ---------- |
| ANSES     | departamento | resuelto   |
| Alimentar | departamento | operativo  |
| Educación | departamento | operativo  |
| Niñez     | departamento | pendiente  |
| STESS     | —            | postergado |

---

## Estado actual

* `geo_ref` cargado y validado
* pipeline ANSES resuelto
* pipeline Alimentar operativo
* pipeline Educación operativo (en mejora)
* STESS descartado para etapa actual
* metodología definida y replicable

---

## Regla del proyecto

Si no ayuda a ubicar a una persona en el territorio, no importa.
