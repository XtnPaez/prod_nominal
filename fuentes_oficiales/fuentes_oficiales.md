# FUENTES OFICIALES — GEO

## 1. Provincias

Fuente:
`unidades_geoestadisticas.provincias_2022_indec`

Campos clave:

* `cpr`
* `nam`

Uso:

* normalización de provincia
* referencia oficial IGN

---

## 2. Departamentos

Fuente:
`unidades_geoestadisticas.departamentos_2022_indec`

Campos clave:

* `cpr`
* `cde`
* `nam`

Uso:

* codificación de departamento
* referencia oficial IGN

---

## 3. Localidades

Fuente:
`public.localidadBahra`

Campos clave:

* `codigo_ase`
* `nombre_geo`
* `nombre_dep`
* `nombre_pro`

Uso:

* resolución posterior de localidad oficial
* no utilizada aún como eje principal de los cruces

---

## 4. Códigos postales

Fuente operativa:
`unidades_geoestadisticas.codigos_postales_2026_siempro`

Origen:
repositorio `cod_pos_AR`

Estado:

* codificada contra provincias IGN
* codificada contra departamentos IGN
* complementada con CABA
* pendiente resolución fina a nivel localidad

Campos clave:

* `cp`
* `codprov_ign`
* `coddepto_ign`

Uso:

* ancla territorial intermedia
* asignación de departamento a partir de código postal

---

## 5. Equivalencias de provincia ANSES → IGN

Tabla auxiliar:
`piloto_nominal.provincia_anses_ign`

Uso:

* traducción de los códigos provinciales propios de ANSES
* validación territorial previa al cruce por CP

Observación:

* necesaria porque el catálogo ANSES no coincide con IGN

---

## 6. Regla operativa

Cuando exista código postal:

1. normalizar provincia al catálogo oficial
2. cruzar por `cp + codprov_ign`
3. asignar `coddepto_ign`
4. usar localidad solo como etapa posterior, no como clave principal
