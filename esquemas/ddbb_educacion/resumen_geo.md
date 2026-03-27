# ddbb_educacion — resumen geo

## Tabla principal con datos geográficos

### Tabla: becas_belgrano

* **campos geo:**

  * provincia
  * partido
  * localidad
  * codigo_postal
  * calle
  * num_casilla
  * dto

* **tipo de dato geo:**

  * provincia
  * departamento
  * localidad
  * direccion
  * codigo_postal

* **CUIL/CUIT:**

  * campo: cuit
  * relación: directa

* **nivel máximo potencial:**

  * direccion

* **observaciones:**

  * contiene todos los niveles geo en una sola tabla
  * partido funciona como departamento explícito
  * código postal disponible (ancla territorial fuerte)
  * dirección presente (aunque "num_casilla" puede no ser número estándar)
  * provincia/localidad en texto libre

---

## Tablas adicionales con datos geo (solo si aportan campos distintos)

### Tabla: becas_belgrano_serie

* **campos geo:**

  * mismos campos que tabla principal

* **observaciones:**

  * no aporta nuevos campos geo
  * solo agrega dimensión temporal

---

## Síntesis del esquema

* **tabla principal:** becas_belgrano
* **nivel máximo alcanzable:** direccion
* **cuil asociado:** sí
* **uso de código postal:** sí

---

## Evaluación preliminar

* **completitud esperada:** media-alta
* **complejidad de normalización:** media
* **riesgo principal:**

  * calidad de dirección (num_casilla no siempre interpretable)
  * texto libre en localidad

---

## Decisión

* trabajar

---

## Siguiente paso

* generar queries de calidad sobre:

  * becas_belgrano
