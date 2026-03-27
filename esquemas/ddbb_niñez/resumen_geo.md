# ddbb_ninez — resumen geo

## Tabla principal con datos geográficos

### Tabla: nina_nino_adolescente

* **campos geo:**

  * provincia
  * localidad
  * codigo_postal

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
  * código postal es el principal ancla territorial
  * provincia y localidad en texto libre
  * estructura similar a ANSES pero sin provincia codificada

---

## Tablas adicionales con datos geo (solo si aportan campos distintos)

* no se identifican tablas con datos geográficos adicionales relevantes

---

## Síntesis del esquema

* **tabla principal:** nina_nino_adolescente
* **nivel máximo alcanzable:** departamento
* **cuil asociado:** sí
* **uso de código postal:** sí

---

## Evaluación preliminar

* **completitud esperada:** media
* **complejidad de normalización:** media
* **riesgo principal:**

  * dependencia del código postal
  * provincia no codificada
  * ausencia de dirección

---

## Decisión

* trabajar

---

## Siguiente paso

* generar queries de calidad sobre:

  * nina_nino_adolescente
