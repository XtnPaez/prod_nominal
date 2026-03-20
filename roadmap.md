# ROADMAP — GEO

## Fase 1 — Inventario geo

Objetivo:
Identificar qué tablas tienen datos geográficos

Output:

- inventario_geo.md por esquema

Estado:

- Alimentar: completo
- resto: pendiente

---

## Fase 2 — Codificación

Objetivo:
Evaluar si los datos están codificados

Output:

- codificacion.md por esquema

Estado:

- Alimentar: completo

---

## Fase 3 — CUIL → domicilio

Objetivo:
Determinar si se puede ubicar a cada persona

Output:

- cuil_domicilio.md

Estado:

- Alimentar: completo

---

## Fase 4 — Estrategia de normalización geográfica (CP + fuentes oficiales)

Objetivo:
Construir un pipeline de asignación territorial robusto usando código postal como ancla intermedia

Pipeline:

1. Codificar provincia en tablas nominales
   - provincia → codprov

2. Construir tabla de códigos postales normalizada
   - input: public.cod_pos_ar
   - output: public.codpos_normalizada

3. Codificar provincia en tabla CP
   - provincia_texto → codprov
   - resultado: exactitud operativa total

4. Codificar departamento en tabla CP
   - codprov + partido_texto → coddepto
   - resultado: alta cobertura operativa
   - los casos de score menor responden en general a diferencias nominales del tipo:
     - abreviaturas
     - títulos
     - apóstrofes
     - nombres oficiales extendidos

5. Cruce CP + provincia sobre tablas nominales
   - codprov + codpos → asignación de coddepto

6. Resolución de localidad oficial
   - codprov + coddepto + localidad_texto → codigo_ase

7. Generación de tabla final geocodificada
   - cuil → codprov → coddepto → codlocalidad

Output:

- public.codpos_normalizada
- reglas de matching
- métricas de calidad
- tabla nominal enriquecida con coddepto

Estado:

- provincia: resuelto
- departamento: resuelto
- join con Alimentar: pendiente
- localidad oficial: pendiente

---

## Fase 5 — Validación y calidad

Objetivo:
Medir confiabilidad de la asignación geográfica

Métricas:

- % registros con CP válido
- % asignación de departamento
- % asignación de localidad
- % casos ambiguos

Estado:

- provincia CP: validada
- departamento CP: validado
- Alimentar: pendiente

---

## Fase 6 — Modelo unificado

Objetivo:
Construir modelo común de domicilios geocodificados

Estado:

- pendiente

---

## Fase actual

Fase 1–3 completadas  
Fase 4 ejecutada para tabla CP  
Próximo paso: cruce Alimentar + codpos_normalizada para asignar coddepto