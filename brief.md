# Brief

## Hallazgos clave

- Alimentar es un esquema apto como piloto metodológico del proyecto.
- `cuiltitular` emerge como clave estructural dominante.
- `titulares` es la tabla base más fuerte para identidad y geografía.
- `menores` aporta nominalidad y vínculo, pero no geografía propia.
- `unidades_convivencia` habilita derivación de hogares.
- `pa_pagados` y tablas `_serie` permiten trazabilidad temporal del beneficio.

## Problemas recurrentes detectados

- heterogeneidad de tipos de datos para identificadores
- falta de constraints relacionales explícitas
- geografía en texto libre
- ausencia de nombre/apellido en la tabla base de titulares
- posible duplicación entre tablas snapshot y serie

## Reglas emergentes

- tratar CUIL como texto normalizado de 11 dígitos en la capa de integración
- distinguir tabla principal de identidad, tabla de vínculo y tabla de eventos
- analizar geografía como eje obligatorio en todas las tablas
- no asumir que una tabla denormalizada reemplaza al modelo relacional

## Patrones detectados

- adulto responsable ↔ menor dependiente
- pagos por período
- tabla actual + tabla histórica/serie
- domicilio asociado al adulto, no al menor
