# ddbb_anses — resumen geo

## Tabla principal con datos geográficos

### Tabla: anses

* **campos geo:**

  * provincia_cd
  * localidad_tx
  * codigo_postal_nu

* **tipo de dato geo:**

  * provincia
  * localidad
  * codigo_postal

* **CUIL/CUIT:**

  * campo: cuil_cuit_nu
  * relación: directa

* **nivel máximo potencial:**

  * departamento

* **observaciones:**

  * provincia viene codificada (ventaja estructural)
  * no hay dirección (sin calle ni número)
  * código postal es el principal ancla territorial
  * localidad en texto libre, requiere normalización
  * posible presencia de múltiples CUIL asociados (estructura familiar)

---

## Tablas adicionales con datos geo (solo si aportan campos distintos)

* no se identifican tablas con datos geográficos adicionales relevantes

---

## Síntesis del esquema

* **tabla principal:** anses
* **nivel máximo alcanzable:** departamento
* **cuil asociado:** sí
* **uso de código postal:** sí

---

## Evaluación preliminar

* **completitud esperada:** media
* **complejidad de normalización:** baja
* **riesgo principal:**

  * dependencia del código postal
  * imposibilidad de geocodificación a nivel dirección

---

## Decisión

* trabajar

---

## Siguiente paso

* generar queries de calidad sobre:

  * anses
