# ddbb_alimentar — CUIL → DOMICILIO

## Modelo general

Entidad clave:

* cuiltitular

Conclusión:
El titular es la única entidad con capacidad directa de geolocalización.

---

## Evaluación por tabla

### titulares

Relación:

* cuiltitular → dirección

Tipo:
1 domicilio

Detalle:

* dirección completa en mismo registro 
* no hay versión histórica

Conclusión:
Fuente base de domicilio actual

---

### titulares_serie

Relación:

* cuil_titular → dirección

Tipo:
múltiples domicilios

Detalle:

* un registro por periodo 
* permite reconstruir cambios de domicilio

Conclusión:
Fuente histórica principal

---

### unidades_convivencia

Relación:

* cuil_titular → dirección
* cuil_menor → dirección (indirecto)

Tipo:
múltiples domicilios

Detalle:

* múltiples registros por hogar 
* mismo domicilio repetido por menor

Conclusión:
Permite asignar domicilio a menores

---

### menores

Relación:

* cuilmenor → (sin domicilio)
* cuiltitular → domicilio indirecto

Tipo:
indirecto

Detalle:

* no contiene datos geográficos 

Conclusión:
Depende completamente del titular

---

### menores_serie

Tipo:
indirecto

Detalle:

* sin campos geográficos 

Conclusión:
Sin aporte geo

---

### pa_pagados

Relación:

* cuil → sin domicilio

Tipo:
no vinculable

Detalle:

* no contiene geo 

Conclusión:
Irrelevante para ubicación

---

## Síntesis

| entidad | acceso a domicilio | tipo               |
| ------- | ------------------ | ------------------ |
| titular | directo            | 1 / múltiples      |
| menor   | indirecto          | depende de titular |
| pago    | nulo               | no aplica          |

---

## Modelo resultante

* unidad real de geolocalización: titular
* extensión a menores: vía convivencia
* historial: titulares_serie

---

## Conclusión final

El esquema permite:

* geolocalizar titulares directamente
* geolocalizar menores indirectamente
* reconstruir historial de domicilios

Limitación:

* no existe domicilio propio por menor
