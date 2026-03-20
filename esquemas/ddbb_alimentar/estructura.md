# Estructura del esquema ddbb_alimentar

## Inventario de tablas

| tabla | categoría | observación |
|---|---|---|
| `titulares` | persona nominal directa | tabla principal del esquema |
| `menores` | persona nominal directa | persona dependiente asociada a titular |
| `unidades_convivencia` | relaciones | mezcla relación y atributos de personas |
| `pa_pagados` | eventos / prestaciones | pagos por CUIL y período |
| `titulares_serie` | eventos / prestaciones | serie histórica de titulares |
| `menores_serie` | eventos / prestaciones | serie histórica de menores |

## Clasificación analítica

### Persona nominal directa
- `titulares`
- `menores`

### Relaciones
- `unidades_convivencia`

### Eventos / prestaciones
- `pa_pagados`
- `titulares_serie`
- `menores_serie`

## Observaciones estructurales

- El esquema está razonablemente orientado a beneficiarios y pagos.
- Hay una clara separación entre tablas base y tablas serie.
- `unidades_convivencia` parece una tabla derivada o de explotación analítica más que una entidad transaccional limpia.
- No aparecen catálogos geográficos internos ni claves normalizadas de localidad/provincia.
