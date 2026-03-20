# ddbb_alimentar

## Overview general

El esquema `ddbb_alimentar` funciona como piloto metodológico muy útil porque concentra las cuatro piezas que importan para el proyecto: personas, relaciones, eventos y geografía.

Permite identificar titulares y menores, reconstruir vínculos titular-menor, observar pagos y series temporales, y además aporta domicilio del titular con un nivel de detalle suficiente como para pensar geocodificación posterior.

## Tablas del esquema

- `titulares`
- `menores`
- `unidades_convivencia`
- `pa_pagados`
- `titulares_serie`
- `menores_serie`

## Lectura analítica rápida

- **Entidad central operativa:** `titulares`
- **Entidad dependiente principal:** `menores`
- **Relación clave:** `cuiltitular`
- **Evento principal:** pagos por período
- **Activo geográfico clave:** domicilio del titular

## Evaluación global del esquema

| eje | evaluación | síntesis |
|---|---|---|
| identidad | alta/media | fuerte en titulares, más débil en menores |
| atributos personales | media | suficientes para identificación auxiliar |
| relaciones | alta | el vínculo titular-menor está claro |
| eventos/prestaciones | alta | pagos y series permiten trazabilidad |
| geografía | media-alta | hay domicilio, pero con texto libre |

## Valor para el proyecto

`ddbb_alimentar` es un muy buen esquema piloto porque ya deja probar:

1. consolidación de personas
2. derivación de hogares o unidades convivenciales
3. construcción de historial de prestaciones
4. normalización y geocodificación de domicilios

## Hipótesis de trabajo emergentes

- `cuiltitular` debe tratarse como clave estructural dominante del esquema.
- `menores` depende relacionalmente de `titulares`.
- `unidades_convivencia` no es un modelo limpio, pero es muy útil como tabla puente operativa.
- la calidad geográfica va a definir gran parte del valor real del esquema.
