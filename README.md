# GEO — Evaluación de geolocalización de bases nominales

## Propósito

Evaluar bases de datos exclusivamente desde su capacidad para **geolocalizar personas**.

No se analizan aspectos de negocio.
Solo interesa si una persona puede ser ubicada en el territorio y con qué precisión.

---

## Pregunta central

Para cada tabla:

* ¿tiene datos geográficos?
* ¿qué campos?
* ¿está vinculada a CUIL/CUIT?
* ¿hasta qué nivel permite ubicar a la persona?

---

## Metodología

1. Identificar tablas con datos geográficos
2. Listar campos geo
3. Verificar vínculo con CUIL/CUIT
4. Determinar nivel máximo alcanzable:

   * provincia
   * departamento
   * localidad
   * dirección
5. Evaluar calidad de datos (queries)
6. Decidir:

   * trabajar
   * trabajar con reservas
   * descartar

---

## Niveles de geolocalización

* **Provincia** → campo provincia
* **Departamento** → provincia + departamento/partido o equivalente
* **Localidad** → provincia + localidad
* **Dirección** → calle + número (y opcionales)

---

## Criterios de descarte (operativos)

* sin campos geo → descartar
* sin CUIL/CUIT o vínculo indirecto débil → bajo valor
* baja completitud → no se trabaja ese nivel

---

## Fuentes oficiales

* provincias (INDEC)
* departamentos (INDEC)
* localidades (BAHRA)

Estas son la única referencia válida para normalización.

---

## Esquemas analizados

| esquema   | tablas geo | nivel max | calidad | decisión  |
| --------- | ---------- | --------- | ------- | --------- |
| alimentar | 3          | dirección | alta    | trabajar  |
| anses     | -          | -         | -       | pendiente |
| stess     | -          | -         | -       | pendiente |
| educacion | -          | -         | -       | pendiente |
| niñez     | -          | -         | -       | pendiente |

---

## Estado actual

* alimentar → identificado y validado
* resto → pendiente de análisis

---

## Estructura del repo

* `esquemas/` → análisis por base

  * `resumen_geo.md` → inventario y potencial geo
  * `queries_calidad.sql` → evaluación de calidad

* `criterios/` → reglas de análisis

* `fuentes_oficiales/` → capas de referencia

---

## Regla principal

Si no ayuda a ubicar a una persona en el territorio, no importa.
