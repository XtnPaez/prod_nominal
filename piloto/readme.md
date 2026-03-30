# PILOTO — Validación de asignación de departamento por código postal

## Objetivo

Evaluar la viabilidad de asignar **departamento a CUIL** utilizando código postal como clave de cruce, comparando:

* una fuente **apócrifa**
* una fuente **normalizada y validada** (`cod_pos_AR`)

---

## Universo de análisis

* Base: titulares (Alimentar)
* Tamaño: ~50.000 registros
* Unidad: CUIL

---

## Estrategia

Para cada registro:

1. tomar código postal declarado
2. cruzar contra tabla de códigos postales
3. asignar departamento
4. validar contra provincia declarada

---

## Fuentes utilizadas

### 1. Fuente apócrifa

Tabla: `piloto_codpos_apocrifos`

* origen no controlado
* incluye:

  * cp
  * departamento
  * coordenadas

---

### 2. Fuente normalizada (SIEMPRO)

Tabla: `codigos_postales_2026_siempro`

Repositorio:
https://asimov.cncps.gob.ar/cpaez/cod_pos_AR

Características:

* codificada contra IGN
* incluye:

  * cp
  * codprov_ign
  * coddepto_ign
* validada

---

## Criterio de validación

Un caso se considera **válido** cuando:

* se asigna departamento
* la provincia inferida coincide con la provincia declarada

```text
coddepto IS NOT NULL
AND codprov_declarado = codprov_fuente
```

---

## Resultados

### Fuente apócrifa

* casos validados: 26.495
* cobertura: ~53%

---

### Fuente SIEMPRO

* casos validados: 48.584
* cobertura: 97,17%

---

## Comparación

| fuente   | casos válidos | cobertura |
| -------- | ------------- | --------- |
| apócrifa | 26.495        | ~53%      |
| siempro  | 48.584        | 97,17%    |

---

## Lectura

* el uso de código postal como clave de asignación territorial es **válido**
* la calidad de la fuente impacta directamente en la cobertura
* la tabla normalizada mejora significativamente los resultados
* la validación por provincia elimina asignaciones inconsistentes

---

## Conclusión

El pipeline:

```
CUIL → CP → provincia → departamento
```

es **operativamente viable** para escalar al total de bases nominales.

---

## Siguiente paso

* aplicar el proceso a todos los esquemas
* generar indicador: cantidad de CUIL por departamento
* evaluar cobertura real sobre universo completo

---

## Nota

La tabla `codigos_postales_2026_siempro` es una derivación validada de datos de Correo Argentino cruzados con capas oficiales IGN.
