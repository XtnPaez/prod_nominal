# bbdd_anses — pipeline

## Objetivo

Asignar **departamento** a los CUIL de ANSES usando:

* provincia ANSES normalizada
* código postal
* tabla de códigos postales de referencia

Resultado final:

> **cantidad de CUIL por departamento**

## Fuente nominal

Tabla origen:

* `ddbb_anses.anses`

Campos mínimos usados:

* `cuil_cuit_nu` → `cuil`
* `provincia_cd` → `codprov_fuente`
* `codigo_postal_nu` → `cp_fuente`

## Referencia geo

Tablas usadas:

* `geo_ref.codigos_postales`
* `geo_ref.alias_provincias_anses`

## Tablas de trabajo

### `geo_work.anses_base`

Extracto mínimo desde ANSES.

Campos:

* `cuil`
* `codprov_fuente`
* `cp_fuente`
* `codprov_ref`

### `geo_work.anses_join`

Resultado del cruce territorial.

Campos:

* `cuil`
* `codprov_fuente`
* `codprov_ref`
* `cp_fuente`
* `coddepto_ref`
* `cp_match`
* `fl_match_cp`
* `fl_match_validado`

### `geo_work.anses_agg_depto`

Agregado final por departamento.

Campos:

* `coddepto_ref`
* `total_cuiles`

## Secuencia aplicada

1. creación de `geo_work.anses_base`
2. carga de extracto mínimo desde `ddbb_anses.anses`
3. asignación de `codprov_ref` usando `geo_ref.alias_provincias_anses`
4. creación de `geo_work.anses_join`
5. cruce territorial por:

   * `cp_fuente = cp`
   * `codprov_ref = codprov_ref`
6. creación de `geo_work.anses_agg_depto`
7. agregado:

   * `COUNT(DISTINCT cuil)` por `coddepto_ref`

## Resultado

* total base: **11.283.777**
* con departamento asignado: **9.392.161**
* cobertura sobre total: **83,24%**

## Lectura

* el pipeline quedó validado
* el uso de CP como ancla territorial es operativo
* ANSES queda resuelta a nivel departamento en el nuevo modelo

## Producto final

Tabla agregada:

* `geo_work.anses_agg_depto`

Uso:

* análisis territorial
* exportación
* unión posterior con geometrías fuera del servicio si hiciera falta

## Estado

> **Resuelto**
>
> Pipeline implementado y replicable.
