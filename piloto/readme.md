# PILOTO — Validación de asignación de departamento por código postal

## Objetivo

Evaluar la viabilidad de asignar **departamento a CUIL** utilizando código postal como clave de cruce, comparando una fuente apócrifa con una fuente normalizada y validada.

---

## Universo de análisis

### Piloto Alimentar

* base: titulares
* tamaño: ~50.000 registros

### ANSES

* base: `ddbb_anses.anses`
* tamaño: **11.283.777 registros**

---

## Estrategia

1. tomar código postal declarado
2. normalizar provincia si hace falta
3. cruzar contra tabla de códigos postales
4. asignar departamento
5. medir cobertura

---

## Fuentes utilizadas

### Fuente apócrifa

* tabla: `piloto_codpos_apocrifos`

### Fuente normalizada SIEMPRO

* tabla: `unidades_geoestadisticas.codigos_postales_2026_siempro`
* origen: repositorio `cod_pos_AR`
* codificada contra provincias y departamentos IGN

---

## Resultado del piloto Alimentar

### Fuente apócrifa

* casos validados: **26.495**
* cobertura: ~53%

### Fuente SIEMPRO

* casos validados: **48.584**
* cobertura: **97,17%**

Lectura:

* la fuente SIEMPRO mejora fuertemente la cobertura
* el pipeline quedó validado

---

## Resultado sobre ANSES

* total registros: **11.283.777**
* candidatos: **11.227.845**
* casos con departamento asignado: **9.392.161**
* cobertura sobre total: **83,24%**
* cobertura sobre candidatos: **83,65%**

Se recuperaron **1.321.648 casos de CABA** luego de completar la tabla de códigos postales con esa jurisdicción.

---

## Conclusión

El pipeline:

`CUIL → CP → provincia normalizada → departamento`

es **operativamente viable** y puede ser escalado al resto de los esquemas.

---

## Producto

* asignación territorial por departamento
* base para mapificación en QGIS
* indicador: cantidad de CUIL por departamento
