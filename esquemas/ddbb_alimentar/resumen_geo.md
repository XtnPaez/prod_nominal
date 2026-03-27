# ddbb_alimentar — resumen geo

## Tabla principal con datos geográficos

### Tabla: titulares

* **campos geo:**

  * provincia
  * localidad
  * cod_postal
  * calle
  * numero
  * piso
  * depto

* **tipo de dato geo:**

  * provincia
  * localidad
  * direccion
  * codigo_postal

* **CUIL/CUIT:**

  * campo: cuiltitular
  * relación: directa

* **nivel máximo potencial:**

  * direccion

* **observaciones:**

  * contiene todos los niveles de geo en una sola tabla
  * código postal usable como ancla territorial (tabla externa normalizada)
  * provincia y localidad en texto libre
  * no tiene departamento explícito

---

## Tablas adicionales con datos geo (solo si aportan campos distintos)

### Tabla: titulares_serie

* **campos geo:**

  * municipio_titular
  * departamento

* **observaciones:**

  * aporta campo de departamento explícito
  * municipio_titular puede funcionar como localidad
  * útil como complemento para codificación territorial

---

## Síntesis del esquema

* **tabla principal:** titulares
* **nivel máximo alcanzable:** direccion
* **cuil asociado:** sí
* **uso de código postal:** sí

---

## Evaluación preliminar

* **completitud esperada:** media
* **complejidad de normalización:** media
* **riesgo principal:**

  * ambigüedad en localidad
  * dependencia de CP para bajar a departamento

---

## Decisión

* trabajar

---

## Siguiente paso

* generar queries de calidad sobre:

  * titulares
