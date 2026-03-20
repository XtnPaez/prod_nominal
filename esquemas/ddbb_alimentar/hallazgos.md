# ddbb_alimentar — HALLAZGOS

## 1. Núcleo de geolocalización

* El esquema se apoya completamente en **cuiltitular**
* Es la única entidad con domicilio propio

---

## 2. Calidad de datos geográficos

* Dirección completa disponible (calle + número)
* Alto potencial de geocodificación
* Sin codificación (todo texto libre)

---

## 3. Modelo de domicilios

* titulares → domicilio único (estado actual)
* titulares_serie → domicilios múltiples (histórico)
* unidades_convivencia → domicilio replicado por hogar

---

## 4. Cobertura poblacional

* titulares → geolocalización directa
* menores → geolocalización indirecta vía titular
* cobertura efectiva: alta

---

## 5. Principales problemas

* falta de normalización geográfica
* ambigüedad en provincia/localidad
* duplicación de domicilios (convivencia)
* ausencia de claves geográficas oficiales

---

## 6. Fortalezas

* modelo claro CUIL → domicilio
* disponibilidad de dirección completa
* existencia de historial (serie)

---

## 7. Riesgos

* errores en geocodificación por texto libre
* inconsistencias territoriales
* pérdida de precisión sin ETL previo

---

## 8. Oportunidades

* geocodificación masiva viable
* reconstrucción de hogares
* análisis temporal de movilidad

---

## 9. Valor geo del esquema

alto

---

## 10. Conclusión

El esquema es uno de los más explotables para geolocalización,
pero depende completamente de procesos de normalización previa.
