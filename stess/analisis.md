[Volver a Readme](https://asimov.cncps.gob.ar/cpaez/prod_nominal)

# Informe de Estado – Base STESS

**Fecha de corte:** análisis estructural (sin métricas volumétricas)  
**Unidad de análisis:** PERSONA (CUIL)  
**Esquema:** ddbb_stess

Este informe sigue la misma lógica aplicada a **Alimentar** y **Educación**, describiendo rol, estructura, calidad esperable y capacidad de integración de la base STESS dentro de un Registro Único de Personas.

---

## 1. Tabla `stess_202509`

### Rol funcional
Tabla **transaccional de liquidaciones**.  
Registra eventos de pago asociados a personas, no personas únicas.

### Campos clave
- `id` (bigserial) – identificador técnico
- `cuil` (varchar(11)) – identificador de persona
- `apellido_y_nombre` (varchar(25))
- `tipo_doc` (varchar(2))
- `nro_doc` (varchar(8))
- `fecha_nacimiento` (date)
- `sexo` (varchar(1))
- `importe_total` (numeric(10,2))
- `tipo_liquidacion` (varchar(2))
- `liqui_plan` (varchar(2))
- `periodo_liquidado` / `periodo_de_liquidacion`
- `provincia_cod` (varchar(2))
- `provincia_desc`, `municipio_desc`, `localidad_desc`
- `domicilio` (varchar(30))
- `createdat`, `updatedat`

### Evaluación estructural
- Una misma persona (`cuil`) puede aparecer múltiples veces.
- No existe unicidad por persona (correcto para el rol de la tabla).
- Mezcla datos nominales, administrativos y geográficos.
- Campo `cuil` es el ancla principal para integración interprograma.

---

## 2. Tabla `padron_stess`

### Rol funcional
Tabla de **consolidación lógica por persona**.  
Funciona como índice de presencia de CUIL en STESS.

### Campos
- `cuil` (varchar(11))
- `apellido_y_nombre` (varchar(25))
- `programas` (text)
- `tablas` (text)

### Evaluación estructural
- Orientada a una fila por persona.
- No tiene clave primaria ni restricciones de unicidad declaradas.
- Es candidata natural a:
  - vista materializada,
  - o tabla puente hacia el Registro Único.

---

## 3. Tablas de referencia (`ref_*`)

### Listado
- `ref_sexo`
- `ref_tipo_doc`
- `ref_tipo_liquidacion`
- `ref_liqui_plan`
- `ref_provincia`

### Rol
- Normalización de dominios.
- No contienen personas ni eventos.
- Cardinalidad baja y estable.

### Evaluación
- Correctamente separadas del modelo transaccional.
- Aptas para joins de normalización semántica.

---

## 4. Diagnóstico General

- STESS **no es un padrón**, es una base de eventos.
- El CUIL está presente pero no normalizado como clave única.
- La calidad de integración depende de:
  - consistencia del CUIL,
  - estabilidad de datos nominales,
  - uso correcto de tablas de referencia.

---

## 5. Relación con otras bases

- Con **Alimentar**: cruce directo por CUIL adulto.
- Con **Educación**: cruce por CUIL adulto (previa normalización CUIT/CUIL).
- Con Registro Único: STESS debe aportar **eventos**, no identidad.

---

## 6. Recomendaciones Técnicas

1. No usar `stess_202509` como fuente de persona.
2. Consolidar identidad en una tabla canónica externa.
3. Tratar STESS como fuente de **hechos / eventos**.
4. Formalizar `padron_stess` como vista o tabla con UNIQUE(cuil).
5. Normalizar provincia, sexo y tipo_doc vía `ref_*`.

---

## Conclusión

La base **STESS** presenta una estructura **correcta para su función transaccional**, pero **no debe ser interpretada como padrón de personas**.

Su integración al ecosistema debe realizarse:
- vía CUIL,
- con consolidación externa de identidad,
- y uso controlado de sus datos nominales.

Es una fuente sólida de **historial y eventos**, indispensable pero subordinada al Registro Único de Personas.
