# GEO — Geolocalización de Bases Nominales

## Objetivo

Evaluar bases de datos exclusivamente desde su capacidad para **geolocalizar personas**.

---

## Alcance

El análisis se enfoca en:

* presencia de datos geográficos
* nivel de codificación
* vínculo CUIL/CUIT → domicilio
* potencial de geocodificación

---

## Enfoque

* análisis por tabla
* el esquema es solo contexto
* solo importa lo que permite ubicar personas

---

## Estructura del proyecto

* esquemas/ → análisis por base
* fuentes_oficiales/ → capas de referencia
* criterios/ → reglas del análisis

---

## Regla principal

Si no ayuda a ubicar a una persona en el territorio, no importa.
