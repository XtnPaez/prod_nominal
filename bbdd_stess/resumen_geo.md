# stess — resumen geo

* **tabla:** stess_202404 / padron_stess
* **geo:** provincia_cod, municipio_desc, localidad_desc, domicilio
* **nivel:** no asignable (actual)
* **cuil:** sí (directo)
* **codificación:** provincia codificada / resto texto inconsistente
* **cp:** no disponible

---

## resultado

* **registros:** 128.503
* **con municipio + localidad:** 55.685
* **cobertura geo útil:** ~43%

---

## lectura

* inconsistencia entre provincia y municipio/localidad
* valores incompatibles territorialmente (ej: CABA + municipios de PBA)
* sin código postal como ancla
* estructura no apta para asignación masiva de departamento

---

## decisión

> postergar

---

## potencial

* posible uso en etapas avanzadas con lógica de dirección
* requiere limpieza estructural previa
* no apta para pipeline actual basado en CP
