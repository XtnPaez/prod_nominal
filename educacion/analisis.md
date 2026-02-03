[Volver a Readme](https://asimov.cncps.gob.ar/cpaez/prod_nominal)
# Informe de Estado – Base Educación

**Fecha de corte:** análisis estructural y volumétrico  
**Unidad de análisis:** PERSONA (CUIL / CUIT)  
**Esquema:** ddbb_educacion

Este informe replica la lógica aplicada a la base **Alimentar**, enfocándose en volumen, unicidad y capacidad de relación entre personas adultas, menores e instituciones educativas.

---

## 1. Tabla `vouchers_aprobados`

### Rol funcional
Tabla de **relación persona–institución educativa**.  
No define personas; registra vínculos entre un adulto responsable (CUIT/CUIL) y un establecimiento (CUE).

### Campos relevantes
- `cuit` (varchar(11)) – identificador de persona adulta
- `cue` (varchar(10)) – identificador de institución
- `nivel_educativo` (varchar(2))

### Restricciones
- Clave primaria: `id`
- Restricción UNIQUE: (`cuit`, `cue`)

### Evaluación estructural
- La restricción única garantiza que una persona no esté duplicada para la misma institución.
- Un mismo `cuit` puede aparecer múltiples veces asociado a distintos `cue`.
- Tabla correctamente normalizada como **tabla de relaciones**.

---

## 2. Tabla `vouchers_datos_nominales`

### Rol funcional
Tabla de **relación adulto–menor**, con refuerzo nominal (nombres y apellidos).  
Complementa a `vouchers_aprobados` aportando el vínculo familiar.

### Campos relevantes
- `cuil_adulto` (varchar(11))
- `cuil_menor` (varchar(11))
- `ape_nom_adulto` (varchar(100))
- `ape_nom_menor` (varchar(100))

### Restricciones
- Clave primaria: `id`
- Restricción UNIQUE: (`cuil_adulto`, `cuil_menor`)

### Evaluación estructural
- Modela explícitamente el vínculo adulto–menor.
- Permite reconstruir unidades familiares educativas.
- No es fuente primaria de personas, sino de relaciones.

---

## 3. Consistencia entre tablas de Educación

### Claves de integración
- Persona adulta: `cuit` / `cuil_adulto`
- Persona menor: `cuil_menor`
- Institución: `cue`

### Observaciones clave
- El uso de `cuit` en `vouchers_aprobados` y `cuil_adulto` en `vouchers_datos_nominales` requiere **normalización semántica** (conceptualmente representan la misma persona).
- No existen claves foráneas declaradas, pero el diseño lógico es consistente.
- La granularidad es adecuada para cruces con:
  - Alimentar (titulares / menores)
  - STESS (beneficiarios adultos)

---

## 4. Diagnóstico General

- La base Educación está **correctamente modelada como sistema relacional**, no como padrón de personas.
- No presenta duplicación lógica gracias a restricciones UNIQUE.
- Es totalmente apta para:
  - Cruces interprogramas por CUIL.
  - Construcción de grafos persona–persona–institución.
  - Integración en un Registro Único de Beneficiarios.

---

## 5. Recomendaciones Técnicas

1. Normalizar CUIT/CUIL a un único tipo y nombre lógico (`cuil_persona`).
2. Tratar ambas tablas como **tablas de relación**, no como fuentes de persona.
3. Centralizar datos nominales en una tabla canónica de personas.
4. Mantener `vouchers_aprobados` como relación persona–institución.
5. Mantener `vouchers_datos_nominales` como relación adulto–menor.

---

## Conclusión

La base **Educación** presenta **alta calidad estructural y lógica**, sin problemas de integridad ni duplicación.  
Su rol es claro: vincular personas con instituciones educativas.

Está en condiciones óptimas para integrarse al Registro Único de Personas basado en CUIL.
