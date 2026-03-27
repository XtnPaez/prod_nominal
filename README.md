# GEO — Evaluación de geolocalización de bases nominales

## Propósito

Evaluar bases de datos exclusivamente desde su capacidad para **geolocalizar personas**.

El análisis se enfoca únicamente en:

* existencia de datos geográficos
* vínculo con CUIL/CUIT
* nivel de precisión alcanzable
* viabilidad operativa

---

## Pregunta central

Para cada esquema:

* ¿existe vínculo CUIL → ubicación?
* ¿qué nivel geográfico se puede alcanzar?
* ¿vale la pena trabajar esa base?

---

## Metodología

1. Identificar la tabla principal con datos geo

   * o construir una vista ad hoc si el geo está fragmentado

2. Detectar:

   * campos geográficos
   * vínculo con CUIL/CUIT

3. Determinar nivel máximo alcanzable:

   * provincia
   * departamento
   * localidad
   * dirección

4. Evaluar calidad (etapa siguiente)

5. Decidir:

   * trabajar
   * trabajar con reservas
   * descartar

---

## Regla operativa

* sin CUIL → no sirve
* sin datos geo → no sirve
* si no permite ubicar → no sirve

---

## Uso de código postal

El código postal se considera dato geográfico válido.

Se utiliza como **ancla territorial intermedia** para:

* asignar provincia
* asignar departamento
* reducir ambigüedad en localidad

---

## Infraestructura clave

### Repositorio de códigos postales

https://asimov.cncps.gob.ar/cpaez/cod_pos_AR

Estado:

* codificado contra provincias (INDEC)
* codificado contra departamentos (INDEC)
* pendiente codificación a nivel localidad

Rol:

* puente entre bases nominales y capas oficiales
* permite transformar CP declarativo en referencia territorial codificada
* pieza central del pipeline geo

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

## Lectura rápida por esquema

* **Alimentar**
  dirección + CP + CUIL → máxima precisión

* **ANSES**
  sin dirección, pero con CP y provincia codificada

* **Educación**
  estructura completa: dirección + departamento + CP

* **Niñez**
  similar a ANSES pero sin codificación

* **STESS**
  requiere reconstrucción (join), alto potencial

---

## Estado actual

* inventario geo completo
* tablas principales identificadas
* niveles de geolocalización definidos
* infraestructura de CP operativa (provincia + departamento)

---

## Siguiente paso

Evaluación de calidad de datos por esquema:

* completitud
* consistencia
* cobertura real

---

## Regla final

Si no ayuda a ubicar a una persona en el territorio, no importa.
