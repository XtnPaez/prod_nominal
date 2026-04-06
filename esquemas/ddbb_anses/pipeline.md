# ddbb_anses — pipeline

## Objetivo

Asignar **departamento** a los CUIL/CUIT de la base ANSES para construir el primer entregable operativo:

> **cantidad de CUIL por departamento**

---

## Tabla de trabajo principal

### Origen nominal

* `ddbb_anses.anses`

### Campos utilizados

* `cuil_cuit_nu`
* `provincia_cd`
* `codigo_postal_nu`

### Nivel máximo alcanzable

* **departamento**

Observación:

* la tabla no tiene dirección
* el cruce territorial depende de provincia + código postal

---

## Diagnóstico

Resultados sobre la base ANSES:

* total registros: **11.283.777**
* candidatos (`cp` + provincia): **11.227.845**
* casos con departamento asignado: **9.392.161**
* cobertura sobre total: **83,24%**
* cobertura sobre candidatos: **83,65%**

Lectura:

* el campo `codigo_postal_nu` es usable
* la cobertura final es alta
* el método es válido para producción de indicadores territoriales

---

## Problema detectado

Los códigos de provincia de ANSES no coinciden con los códigos IGN.

Por eso fue necesario crear una tabla de equivalencias:

* `piloto_nominal.provincia_anses_ign`

Ejemplo:

* `01` (ANSES) → `02` (IGN, CABA)
* `02` (ANSES) → `06` (IGN, Buenos Aires)

---

## Tabla territorial de referencia

### Fuente

* `unidades_geoestadisticas.codigos_postales_2026_siempro`

### Origen

* repositorio `cod_pos_AR`

### Campos utilizados

* `cp`
* `codprov_ign`
* `coddepto_ign`

### Observación

La tabla fue complementada con códigos postales de CABA, lo que permitió recuperar una gran cantidad de casos inicialmente no asignados.

---

## Lógica del cruce

Secuencia:

1. tomar CUIL desde `ddbb_anses.anses`
2. traducir `provincia_cd` a `codprov_ign`
3. cruzar por:

   * `codigo_postal_nu = cp`
   * `codprov_anses_ign = codprov_ign`
4. asignar:

   * `coddepto_ign`

---

## Resultado

Se obtuvo una tabla nominal enriquecida con departamento y una cobertura de **9.392.161 registros**, equivalente al **83,24%** del total.

Se recuperaron **1.321.648 casos de CABA** luego de completar la tabla postal con esa jurisdicción.

---

## Producto final

* tabla enriquecida con departamento
* vista espacial agregada por departamento:

  * `piloto_nominal.v_total_x_depto_anses`

Uso:

* visualización en QGIS
* agregación territorial
* primer entregable operativo de ANSES

---

## Limitaciones

* no hay dirección
* el análisis depende de la calidad del código postal
* el 16,76% restante queda sin asignación

---

## Estado

> **Pipeline validado**
>
> Cobertura alta y metodología lista para réplica en otros esquemas.

---

## Próximo paso

* replicar proceso en otras bases nominales
* consolidar indicador de CUIL por departamento a nivel sistema
