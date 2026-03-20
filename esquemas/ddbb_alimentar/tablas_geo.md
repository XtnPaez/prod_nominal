# ddbb_alimentar — TABLAS GEO

---

# Tabla: titulares

## 1. Presencia geográfica

Tipo: alta

Campos:

* provincia
* localidad
* cod_postal
* calle
* numero
* piso
* depto

Evaluación:
Dirección completa → geocodificación directa viable 

---

## 2. Nivel de codificación

Tipo: no codificado

Detalle:
Todos los campos son texto libre

---

## 3. Relación con CUIL/CUIT

Clave:

* cuiltitular

Tipo:
1 domicilio

---

## 4. Potencial de geocodificación

alto

Motivo:
Dirección completa

---

## 5. Problemas

* texto libre
* inconsistencia provincia/localidad
* número varchar

---

## 6. Valor geo

alto

Resumen:
Tabla base para geolocalización

---

# Tabla: titulares_serie

## 1. Presencia geográfica

Tipo: alta

Campos:

* provincia_titular
* municipio_titular
* cod_postal
* calle
* numero

Evaluación:
Dirección completa con dimensión temporal 

---

## 2. Nivel de codificación

Tipo: no codificado

---

## 3. Relación con CUIL/CUIT

Clave:

* cuil_titular

Tipo:
múltiples domicilios

---

## 4. Potencial de geocodificación

alto

Motivo:
Permite historial de domicilios

---

## 5. Problemas

* municipio vs localidad inconsistente
* texto libre

---

## 6. Valor geo

muy alto

Resumen:
Histórico de ubicación

---

# Tabla: unidades_convivencia

## 1. Presencia geográfica

Tipo: alta

Campos:

* provincia
* localidad
* cod_postal
* calle
* numero

Evaluación:
Dirección completa compartida 

---

## 2. Nivel de codificación

Tipo: no codificado

---

## 3. Relación con CUIL/CUIT

Clave:

* cuil_titular
* cuil_menor

Tipo:
múltiples domicilios

---

## 4. Potencial de geocodificación

alto

Motivo:
Permite reconstrucción de hogares

---

## 5. Problemas

* duplicación por menor
* cardinalidad inflada

---

## 6. Valor geo

muy alto

Resumen:
Unidad geográfica de hogar

---

# Tabla: menores

## 1. Presencia geográfica

Tipo: sin geo

Campos:

* ninguno 

Evaluación:
No aporta geolocalización

---

## 2. Nivel de codificación

Tipo: n/a

---

## 3. Relación con CUIL/CUIT

Clave:

* cuiltitular

Tipo:
indirecto

---

## 4. Potencial de geocodificación

bajo

Motivo:
Depende de titulares

---

## 5. Problemas

* sin geo propio

---

## 6. Valor geo

nulo

Resumen:
Irrelevante para geo

---

# Tabla: menores_serie

## 1. Presencia geográfica

Tipo: sin geo

Evaluación:
No contiene datos geográficos 

---

## 2. Nivel de codificación

Tipo: n/a

---

## 3. Relación con CUIL/CUIT

Tipo:
indirecto

---

## 4. Potencial de geocodificación

bajo

---

## 5. Problemas

* sin geo

---

## 6. Valor geo

nulo

---

# Tabla: pa_pagados

## 1. Presencia geográfica

Tipo: sin geo

Evaluación:
No contiene campos geográficos 

---

## 2. Nivel de codificación

Tipo: n/a

---

## 3. Relación con CUIL/CUIT

Clave:

* cuil

Tipo:
no vinculable a domicilio

---

## 4. Potencial de geocodificación

nulo

---

## 5. Problemas

* no aporta ubicación

---

## 6. Valor geo

nulo

---
