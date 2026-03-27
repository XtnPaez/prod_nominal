# GEO — Evaluación de geolocalización de bases nominales

## Propósito

Evaluar bases de datos exclusivamente desde su capacidad para **geolocalizar personas**.

El análisis se enfoca únicamente en:

* presencia de datos geográficos
* vínculo con CUIL/CUIT
* nivel de precisión alcanzable
* viabilidad operativa

---

## Pregunta central

Para cada esquema:

* ¿existe vínculo CUIL → ubicación?
* ¿qué nivel geográfico se puede alcanzar?
* ¿vale la pena trabajar esa base?

---

## Metodología

1. Identificar la tabla principal con datos geo

   * o construir una vista ad hoc si el geo está fragmentado

2. Detectar:

   * campos geográficos
   * vínculo con CUIL/CUIT

3. Determinar nivel máximo alcanzable:

   * provincia
   * departamento
   * localidad
   * dirección

4. Evaluar calidad (posterior)

5. Decidir:

   * trabajar
   * trabajar con reservas
   * descartar

---

## Regla operativa

* si no hay CUIL vinculado → no sirve
* si no hay geo → no sirve
* si el geo no permite ubicar → no sirve

---

## Uso de código postal

El código postal se considera dato geográfico válido.

Se utiliza como **ancla territorial intermedia** para:

* asignar provincia
* asignar departamento
* acotar matching de localidad

---

## Esquemas analizados

| esquema   | tabla principal         | nivel máximo |
| --------- | ----------------------- | ------------ |
| alimentar | titulares               | dirección    |
| anses     | anses                   | departamento |
| educacion | becas_belgrano          | dirección    |
| niñez     | nina_nino_adolescente   | departamento |
| stess     | vista_ad_hoc_padron_geo | dirección    |


| esquema   | cuil | código postal | decisión              |
| --------- | ---- | ------------- | --------------------- |
| alimentar | sí   | sí            | trabajar              |
| anses     | sí   | sí            | trabajar              |
| educacion | sí   | sí            | trabajar              |
| niñez     | sí   | sí            | trabajar              |
| stess     | sí   | no            | trabajar con reservas |


---

## Lectura rápida por esquema

* **Alimentar**
  mejor caso general: dirección + CP + CUIL

* **ANSES**
  sin dirección, pero con CP y provincia codificada

* **Educación**
  completo: dirección + departamento explícito + CP

* **Niñez**
  similar a ANSES pero con menor calidad estructural

* **STESS**
  requiere reconstrucción (join), pero potencial alto

---

## Estado actual

* inventario geo completo en todos los esquemas
* identificación de tablas principales
* definición de nivel geográfico alcanzable

---

## Estructura del repo

* `esquemas/`

  * `resumen_geo.md` → análisis por esquema
  * `queries_calidad.sql` → evaluación (siguiente etapa)

* `criterios/`

  * reglas de análisis

* `fuentes_oficiales/`

  * capas de referencia para normalización

---

## Siguiente paso

Evaluación de calidad de datos por esquema:

* completitud
* consistencia
* potencial real de uso

---

## Regla final

Si no ayuda a ubicar a una persona en el territorio, no importa.
