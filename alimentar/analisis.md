[Volver a Readme](https://asimov.cncps.gob.ar/cpaez/prod_nominal)

# Informe de Estado – Base Alimentar

**Fecha de corte:** análisis estructural y volumétrico  
**Unidad de análisis:** PERSONA (CUIL)  
**Esquema:** ddbb_alimentar

---

## 1. Tabla `titulares`

### Volumen
- Registros totales: **2.541.973**
- Titulares únicos (CUIL): **2.541.973**
- CUIL nulos: **0**
- CUIL duplicados: **0**

### Evaluación
- Correspondencia 1 a 1 entre registro y persona.
- Integridad perfecta del identificador CUIL.
- Tabla **canónica y confiable** para adultos titulares.
- Apta para ser base del registro único de personas adultas.

---

## 2. Tabla `menores`

### Volumen
- Registros totales: **4.406.346**
- Menores únicos (CUIL): **4.400.212**
- CUIL nulos o vacíos: **0**
- CUIL de menor duplicados: **6.134**

### Evaluación
- Alta cobertura nominal.
- Existencia de duplicados de CUIL de menor (~0,14% del total).
- Requiere deduplicación lógica por CUIL de menor.
- Tabla válida como fuente de personas menores, con ajuste menor.

---

## 3. Relación titulares–menores

### Cobertura
- Titulares con al menos un menor: **2.506.389**
- Titulares sin menores: **35.584**
- Menores sin titular asociado: **0**
- Menores con titular inexistente: **0**

### Evaluación
- Relación totalmente consistente (sin orfandades).
- Distribución esperable y estable.
- La estructura es **altamente relacionable** y sólida.

---

## 4. Diagnóstico General

- La base Alimentar presenta **excelente calidad estructural**.
- `titulares` es una tabla limpia, sin duplicados ni nulos.
- `menores` presenta duplicación marginal y controlable.
- No existen problemas de integridad referencial.
- El modelo es apto para:
  - Construcción de registro único de personas.
  - Análisis familiar / unidad de convivencia.
  - Cruces con otros programas por CUIL.

---

## 5. Recomendaciones Técnicas

1. Normalizar tipo de dato CUIL (unificar numeric/varchar).
2. Crear vista deduplicada de `menores` por CUIL.
3. Declarar `cuiltitular` como UNIQUE en titulares (si aplica).
4. Usar `titulares` como fuente prioritaria de adultos.
5. Tratar `menores` como fuente válida con deduplicación previa.

---

**Conclusión:**  
La base Alimentar está en **estado operativo óptimo** para integración en un Registro Único de Beneficiarios, con mínimos ajustes técnicos y sin riesgos estructurales.
