# ddbb_anses — resumen geo

## Tabla principal con datos geográficos

### Tabla: personas

* **campos geo:**

  * provincia
  * localidad
  * cod_postal

* **tipo de dato geo:**

  * provincia
  * localidad
  * codigo_postal

* **CUIL/CUIT:**

  * campo: cuil
  * relación: directa

* **nivel máximo potencial:**

  * departamento

* **observaciones:**

  * no hay dirección (sin calle ni número)
  * el código postal es el principal ancla geográfica
  * provincia y localidad en texto libre
  * la precisión depende casi totalmente de la calidad del CP

---

## Tablas adicionales con datos geo (solo si aportan campos distintos)

* no se identifican tablas con campos geo adicionales relevantes

---

## Síntesis del esquema

* **tabla principal:** personas
* **nivel máximo alcanzable:** departamento
* **cuil asociado:** sí
* **uso de código postal:** sí

---

## Evaluación preliminar

* **completitud esperada:** media
* **complejidad de normalización:** baja
* **riesgo principal:**

  * dependencia total del código postal
  * ausencia de dirección impide geocodificación fina

---

## Decisión

* trabajar

---

## Siguiente paso

* generar queries de calidad sobre:

  * personas
