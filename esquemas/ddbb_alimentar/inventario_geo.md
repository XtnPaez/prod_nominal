# ddbb_alimentar — INVENTARIO GEO

## Clasificación de tablas

| tabla                | presencia_geo | codificacion  | cuil→domicilio | valor_geo |
| -------------------- | ------------- | ------------- | -------------- | --------- |
| titulares            | alta          | no codificado | 1 domicilio    | alto      |
| titulares_serie      | alta          | no codificado | múltiples      | muy alto  |
| unidades_convivencia | alta          | no codificado | múltiples      | muy alto  |
| menores              | sin geo       | n/a           | indirecto      | nulo      |
| menores_serie        | sin geo       | n/a           | indirecto      | nulo      |
| pa_pagados           | sin geo       | n/a           | no vinculable  | nulo      |

---

## Lectura rápida

* Solo 3 tablas sirven para geolocalizar:

  * titulares
  * titulares_serie
  * unidades_convivencia

* El resto no aporta geo

---

## Calidad general

* geo: alta disponibilidad (direcciones completas)
* codificación: inexistente (todo texto libre)
* vinculación CUIL: buena (titular como eje)

---

## Riesgos

* ambigüedad en provincia/localidad
* falta de normalización
* duplicación de domicilios (serie y convivencia)

---

## Oportunidades

* geocodificación masiva viable
* reconstrucción de hogares
* construcción de historial de domicilios

---

## Conclusión

El esquema es altamente explotable para geolocalización,
pero requiere normalización previa obligatoria.
