# bbdd_anses — pipeline

## Objetivo

Asignar **departamento** a los CUIL de ANSES usando:

* provincia ANSES normalizada
* código postal
* tabla de códigos postales de referencia

Resultado final:

* **cantidad de CUIL por departamento**

---

## Fuente nominal

Tabla origen:

* `ddbb_anses.anses`

Campos mínimos a extraer:

* `cuil_cuit_nu` → `cuil`
* `provincia_cd` → `codprov_fuente`
* `codigo_postal_nu` → `cp_fuente`

---

## Referencia geo

Tablas de referencia:

* `geo_ref.codigos_postales`
* `geo_ref.alias_provincias_anses`

Uso:

* traducir provincia ANSES a provincia de referencia
* asignar departamento por `cp + codprov_ref`

---

## Tablas de trabajo

### 1. `geo_work.anses_base`

Extracto mínimo desde ANSES.

Campos esperados:

* `cuil`
* `codprov_fuente`
* `cp_fuente`
* `codprov_ref`
* `created_at`
* `updated_at`

---

### 2. `geo_work.anses_join`

Resultado del cruce territorial.

Campos esperados:

* `cuil`
* `codprov_fuente`
* `codprov_ref`
* `cp_fuente`
* `coddepto_ref`
* `cp_match`
* `fl_match_cp`
* `fl_match_validado`
* `created_at`
* `updated_at`

---

### 3. `geo_work.anses_agg_depto`

Agregado final por departamento.

Campos esperados:

* `coddepto_ref`
* `total_cuiles`

---

## Secuencia

### Paso 1

Crear `geo_work.anses_base`

### Paso 2

Cargar extracto mínimo desde `ddbb_anses.anses`

### Paso 3

Asignar `codprov_ref` usando `geo_ref.alias_provincias_anses`

### Paso 4

Crear `geo_work.anses_join`

### Paso 5

Cruzar contra `geo_ref.codigos_postales` por:

* `cp_fuente = cp`
* `codprov_ref = codprov_ref`

### Paso 6

Medir cobertura del join

### Paso 7

Crear `geo_work.anses_agg_depto`

### Paso 8

Agregar:

* `COUNT(DISTINCT cuil)` por `coddepto_ref`

---

## Regla de validación

Se considera válido un caso cuando:

* existe match por CP
* existe correspondencia entre provincia fuente normalizada y provincia de referencia

---

## Producto final

Tabla agregada:

* cantidad de CUIL por departamento

Lista para:

* exportación
* análisis territorial
* unión posterior con geometrías fuera del servicio si hiciera falta

---

## Estado esperado

Pipeline repetible, sin tocar esquemas fuente, usando:

* `geo_ref` como referencia
* `geo_work` como staging y salida
