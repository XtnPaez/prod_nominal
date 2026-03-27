# ddbb_stess — resumen geo

## Tabla principal con datos geográficos

### Tabla: vista_ad_hoc_padron_geo

* **origen:**

  * padron_stess
  * stess_serie

* **join interno:**

  * por cuil

* **campos geo:**

  * provincia_cod
  * provincia_desc
  * municipio_desc
  * localidad_desc
  * domicilio

* **tipo de dato geo:**

  * provincia
  * departamento
  * localidad
  * direccion

* **CUIL/CUIT:**

  * campo: cuil
  * relación: directa

* **nivel máximo potencial:**

  * direccion

* **observaciones:**

  * el geo útil no está concentrado en una sola tabla
  * `padron_stess` aporta el vínculo nominal por CUIL
  * `stess_serie` aporta los campos geo consolidados del esquema
  * `provincia_cod` viene codificada, lo que mejora la normalización
  * `municipio_desc` funciona como equivalente operativo de departamento, pero requiere validación
  * `domicilio` existe, aunque su calidad real debe medirse

---

## Tablas adicionales con datos geo (solo si aportan campos distintos)

* no se identifican tablas con datos geo adicionales relevantes fuera de la reconstrucción padron + serie

---

## Síntesis del esquema

* **tabla principal:** vista_ad_hoc_padron_geo
* **nivel máximo alcanzable:** direccion
* **cuil asociado:** sí
* **uso de código postal:** no
* **requiere join interno:** sí

---

## Evaluación preliminar

* **completitud esperada:** media
* **complejidad de normalización:** media
* **riesgo principal:**

  * necesidad de reconstrucción por join
  * municipio/localidad en texto libre
  * calidad incierta del campo domicilio

---

## Decisión

* trabajar con reservas

---

## Siguiente paso

* generar queries de calidad sobre:

  * vista_ad_hoc_padron_geo
