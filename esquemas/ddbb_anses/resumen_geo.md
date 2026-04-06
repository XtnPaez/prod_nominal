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

  * no hay dirección
  * provincia viene codificada, pero en catálogo propio de ANSES
  * código postal es la clave principal del cruce territorial
  * localidad existe, pero no se usa como clave principal

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

* **completitud esperada:** alta
* **complejidad de normalización:** media
* **riesgo principal:**

  * diferencia entre catálogo provincial de ANSES y codificación IGN

---

## Decisión

* trabajar

---

## Siguiente paso

* cruce por código postal y provincia normalizada
