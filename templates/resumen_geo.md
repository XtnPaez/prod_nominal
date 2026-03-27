# {esquema} — resumen geo

## Tabla principal con datos geográficos

### Tabla: {nombre_tabla}

* **campos geo:**

  * {campo}
  * {campo}

* **tipo de dato geo:**

  * provincia / departamento / localidad / direccion / codigo_postal

* **CUIL/CUIT:**

  * campo: {campo}
  * relación: directa / indirecta

* **nivel máximo potencial:**

  * provincia / departamento / localidad / direccion

* **observaciones:**

  * {notas clave}
  * {limitaciones}

---

## Tablas adicionales con datos geo (solo si aportan campos distintos)

### Tabla: {nombre_tabla}

* **campos geo:**

  * {campo diferencial}

* **observaciones:**

  * {qué aporta distinto}

---

## Síntesis del esquema

* **tabla principal:** {tabla}
* **nivel máximo alcanzable:** {nivel}
* **cuil asociado:** sí / no
* **uso de código postal:** sí / no

---

## Evaluación preliminar

* **completitud esperada:** alta / media / baja
* **complejidad de normalización:** baja / media / alta
* **riesgo principal:**

  * {riesgo}

---

## Decisión

* trabajar / trabajar con reservas / descartar

---

## Siguiente paso

* generar queries de calidad sobre:

  * {tabla}
