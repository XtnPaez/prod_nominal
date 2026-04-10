# alimentar — pipeline

## Objetivo

Asignar departamento a titulares de Alimentar usando:

* provincia (texto)
* código postal
* tabla de referencia geo

Resultado:

> cantidad de CUIL por departamento

---

## Fuente

* `ddbb_alimentar.titulares`

Campos:

* `cuiltitular`
* `provincia`
* `cod_postal`

---

## Estrategia

1. extracción mínima
2. normalización de CP
3. alias de provincias (mapping directo)
4. join con códigos postales
5. agregado por departamento

---

## Tablas

### `geo_work.alimentar_base`

Extracto limpio.

### `geo_work.alimentar_join`

Resultado del cruce territorial.

### `geo_work.alimentar_agg_depto`

Agregado final.

---

## Lógica de join

* `cp_fuente = cp`
* `codprov_ref = codprov_ref`
* solo pares únicos de CP + provincia

---

## Resultado

* cobertura: 65,13%

---

## Lectura

* provincia de alta calidad
* CP como limitante principal
* pipeline consistente con ANSES

---

## Estado

> operativo

Pipeline implementado y replicable.
