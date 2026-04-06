# Convenciones de nombres

## Objetivo

Definir una nomenclatura común para todas las tablas y campos del proyecto geo.

El objetivo es permitir procesamiento homogéneo, reutilización de lógica y comparabilidad entre esquemas.

---

## Esquemas

### geo_ref

Contiene tablas de referencia geográfica y alias.

Uso:

* provincias
* departamentos
* localidades
* códigos postales
* equivalencias

Regla:

* no usar para staging
* no mezclar con resultados

---

### geo_work

Contiene tablas derivadas de bases nominales.

Uso:

* staging
* joins territoriales
* agregados

Regla:

* se puede recalcular
* no modifica fuentes

---

### ddbb_analisis

Esquema para análisis de consistencia.

Regla:

* fuera del flujo geo principal

---

## Sufijos de tablas

### _base

Extracto mínimo desde la fuente.

Ejemplo:

* anses_base
* alimentar_base

---

### _join

Resultado del cruce territorial.

Ejemplo:

* anses_join
* alimentar_join

---

### _agg_depto

Agregado por departamento.

Ejemplo:

* anses_agg_depto
* alimentar_agg_depto

---

## Convenciones de campos

### Fuente

Datos originales:

* provincia_fuente
* cp_fuente
* localidad_fuente

Opcionales:

* cp_raw
* provincia_norm

---

### Referencia

Datos normalizados:

* codprov_ref
* coddepto_ref
* codloc_ref

---

### Matching

* cp_match
* fl_match_cp
* fl_match_validado

Reglas:

* fl_match_cp = 1 → hubo match
* fl_match_validado = 1 → match aceptado

---

## Identificadores

* cuil
* cuit
* cuil_cuit

Evitar nombres originales largos.

---

## Tablas de referencia

### provincias

* codprov
* provincia

### departamentos

* coddepto
* codprov
* departamento

### localidades

* codloc
* coddepto
* codprov
* localidad

### códigos postales

* cp
* codprov_ref
* coddepto_ref

---

## Alias

Ejemplos:

* alias_provincias_anses
* alias_localidades_educacion

Campos mínimos:

* valor_fuente
* valor_normalizado
* cod_ref
* observacion
* created_at

---

## Estrategia del proyecto

### Etapa 1

* asignación por CP
* nivel: departamento

### Etapa 2

* descenso a localidad

### Etapa 3

* descenso a dirección

### Proceso continuo

* construcción de alias

---

## Regla final

Departamento primero.
Localidad después.
Dirección al final.
Alias siempre.
