# FUENTES OFICIALES — GEO

## 1. Provincias

Fuente:
unidades_geoestadisticas.provincias_2022_indec

Campos clave:

- cpr → código provincia
- nam → nombre

Tipo:
codificado

Uso:

- normalización de provincia
- clave primaria geográfica

Estado en proyecto:
- usada para codificar provincia en tabla CP
- resultado operativo: resuelto

---

## 2. Departamentos

Fuente:
unidades_geoestadisticas.departamentos_2022_indec

Campos clave:

- cpr → código provincia
- cde → código departamento
- nam → nombre

Tipo:
codificado

Uso:

- segundo nivel administrativo
- desambiguación territorial

Clave:
cpr + cde

Estado en proyecto:
- usada para codificar partido/departamento en tabla CP
- matching realizado dentro del subconjunto provincial ya codificado

Observación:
- parte de los scores bajos responde a diferencias nominales y no a errores territoriales
- ejemplos típicos:
  - nombres oficiales extendidos
  - títulos como General o Coronel
  - apóstrofes
  - abreviaturas

---

## 3. Localidades

Fuente:
public.localidadBahra

Campos clave:

- codigo_ase → código localidad
- nombre_geo → nombre
- nombre_dep → departamento
- nombre_pro → provincia
- latitud / longitud

Tipo:
codificado

Uso:

- desambiguación de localidades
- geocodificación sin API
- resolución final de localidad oficial

Estado en proyecto:
- pendiente de uso en el cruce final con tablas nominales

---

## 4. Fuente puente no oficial pero estratégica

Fuente:
public.cod_pos_ar

Campos clave:

- cpr → código fuente
- provincia
- partido
- localidad
- cp

Tipo:
semi estructurado

Uso:
- tabla puente para bajar bases nominales a departamento
- ancla intermedia de asignación territorial usando código postal

Observación:
- no es fuente oficial de codificación final
- sí es fuente operativa central del pipeline

---

## 5. Tabla de trabajo derivada

Tabla:
public.codpos_normalizada

Rol:
- staging principal del ETL geo por código postal

Contiene:

- campos originales de cod_pos_ar
- codprov normalizado
- coddepto normalizado
- score y confianza de provincia
- score y confianza de departamento

Uso:
- cruce con bases nominales por codprov + codpos
- asignación de coddepto
- preparación para resolución de localidad oficial

---

## 6. Modelo jerárquico

Provincia → Departamento → Localidad

- provincia: cpr
- departamento: cde
- localidad: codigo_ase

---

## 7. Regla operativa

Toda tabla no codificada debe contrastarse contra estas capas antes de cualquier geocodificación.

Cuando exista código postal:
- primero se codifica provincia
- luego se asigna departamento usando codprov + codpos
- recién después se intenta resolver localidad oficial