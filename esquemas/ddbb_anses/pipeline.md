# ddbb_anses — pipeline

## Objetivo

Asignar **departamento** a los CUIL/CUIT de la base ANSES para construir el primer entregable operativo:

> **cantidad de CUIL por departamento**

---

## Tabla de trabajo principal

### Origen nominal

* `ddbb_anses.anses`

### Campos utilizados

* `cuil_cuit_nu` → identificador nominal
* `provincia_cd` → código de provincia (catálogo ANSES)
* `codigo_postal_nu` → código postal

### Nivel máximo alcanzable

* **departamento**

---

## Diagnóstico

Resultados sobre la base ANSES:

* total registros: **11.283.777**
* candidatos (CP + provincia): **11.227.845**
* casos con departamento asignado: **8.070.513**
* cobertura sobre total: **71,52%**
* cobertura sobre candidatos: **71,88%**

Observaciones:

* el campo `codigo_postal_nu` presenta distribución geográfica consistente
* el campo `provincia_cd` está completo pero utiliza un catálogo propio de ANSES
* existe inconsistencia entre provincia y código postal en una proporción significativa de casos

---

## Problema detectado

Los códigos de provincia de ANSES no coinciden con los códigos utilizados en las capas oficiales.

Ejemplo:

| ANSES | IGN |
| ----- | --- |
| 01    | 02  |
| 02    | 06  |
| 13    | 82  |

Esto impide usar directamente la provincia como filtro en el join.

---

## Solución implementada

### 1. Tabla de equivalencias

Se creó:

* `piloto_nominal.provincia_anses_ign`

Función:

* traducir `provincia_cd` (ANSES) → `codprov_ign`

---

### 2. Normalización de provincia

Se incorpora en la tabla de trabajo:

* `codprov_anses_ign`

---

### 3. Estrategia de cruce

El cruce se realiza con:

* `cp`
* `codprov_anses_ign`

Contra:

* `unidades_geoestadisticas.codigos_postales_2026_siempro`

Condición:

```
cp = cp
AND codprov_anses_ign = codprov_ign
```

---

### 4. Criterio de asignación

Se asigna departamento cuando:

* existe correspondencia CP + provincia normalizada
* el par CP–provincia tiene un único departamento asociado

---

## Tabla territorial

### Fuente

* `unidades_geoestadisticas.codigos_postales_2026_siempro`

Origen:

* repositorio `cod_pos_AR`

Características:

* codificada contra provincias IGN
* codificada contra departamentos IGN
* validada

Campos utilizados:

* `cp`
* `codprov_ign`
* `coddepto_ign`

---

## Resultado

Se generó una tabla enriquecida con:

* `cuil`
* `codprov`
* `cp`
* `codprov_anses_ign`
* `coddepto_ign`

Y posteriormente:

* vista agregada por departamento con geometría:

`piloto_nominal.v_total_x_depto_anses`

---

## Producto final

Tabla espacial:

* cantidad de CUIL por departamento
* lista para visualización en QGIS

---

## Lectura del resultado

* el método permite asignar territorio a más de **8 millones de registros**
* la cobertura es alta para una base sin dirección
* el uso de CP como clave es válido
* la calidad del dato de provincia en ANSES requiere normalización previa

---

## Limitaciones

* CP no identifica unívocamente localidad
* existen CP asociados a múltiples departamentos
* parte del universo queda sin asignación (~28%)
* depende de la calidad del CP declarado

---

## Dependencias operativas

### Permisos

* actualmente el trabajo se ejecuta en entorno auxiliar (`piloto_nominal`)
* pendiente ejecución directa en `prod_nominal` por falta de permisos de escritura

### Datos

* es necesario cargar en `prod_nominal` la tabla:

  * `codigos_postales_2026_siempro`

---

## Estado

> **Pipeline validado**
>
> Resultado consistente y utilizable
> Listo para escalado al resto de los esquemas

---

## Próximo paso

1. replicar proceso en:

   * Alimentar
   * Educación
   * Niñez
   * STESS

2. consolidar indicador:

   * CUIL por departamento a nivel sistema

3. evaluar mejora futura:

   * incorporación de localidad
   * refinamiento de CP ambiguos

---
