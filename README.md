# GEO — Evaluación de geolocalización de bases nominales

## Propósito

Evaluar bases de datos exclusivamente desde su capacidad para **geolocalizar personas**.

El análisis se enfoca en:

* existencia de datos geográficos
* vínculo con CUIL/CUIT
* nivel de precisión alcanzable
* viabilidad operativa

---

## Metodología

1. identificar tabla principal con geo
2. detectar vínculo con CUIL/CUIT
3. definir nivel máximo alcanzable
4. usar código postal como ancla territorial cuando corresponda
5. asignar departamento
6. medir cobertura real

---

## Infraestructura clave

### Repositorio de códigos postales

`cod_pos_AR`

Rol:

* fuente operativa para asignación territorial por código postal
* codificada contra provincias y departamentos IGN
* complementada con CABA para mejorar cobertura

---

## Esquemas analizados

| esquema   | tabla principal         | nivel máximo |
| --------- | ----------------------- | ------------ |
| alimentar | titulares               | dirección    |
| anses     | anses                   | departamento |
| educacion | becas_belgrano          | dirección    |
| niñez     | nina_nino_adolescente   | departamento |
| stess     | vista_ad_hoc_padron_geo | dirección    |

---

| esquema   | cuil | código postal | decisión              |
| --------- | ---- | ------------- | --------------------- |
| alimentar | sí   | sí            | trabajar              |
| anses     | sí   | sí            | trabajar              |
| educacion | sí   | sí            | trabajar              |
| niñez     | sí   | sí            | trabajar              |
| stess     | sí   | no            | trabajar con reservas |

---

## Estado actual

### Alimentar

* piloto validado
* cobertura con fuente SIEMPRO: **97,17%**

### ANSES

* pipeline validado
* **11.283.777** registros
* **9.392.161** con departamento asignado
* cobertura: **83,24%**

---

## Resultado principal hasta ahora

Ya se validó el indicador:

> **cantidad de CUIL por departamento**

sobre ANSES, con salida espacial para QGIS.

---

## Próximo paso

* replicar el mismo proceso en:

  * Educación
  * Niñez
  * STESS
  * Alimentar como corrida completa

* consolidar un indicador territorial unificado para todo el sistema

---

## Regla final

Si no ayuda a ubicar a una persona en el territorio, no importa.
