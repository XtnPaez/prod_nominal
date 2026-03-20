# BRIEF — Estado del proyecto

## Estado actual

* Alimentar: análisis completo
* Tabla CP (correo): procesada
* Tabla CP normalizada: construida y validada
* ANSES: pendiente
* STESS: pendiente
* Educación: pendiente
* Niñez: pendiente

---

## Hallazgos clave

* las bases nominales contienen datos geográficos, pero no estructurados
* la codificación oficial es prácticamente inexistente
* el principal problema no es la falta de datos, sino su ambigüedad

---

## Insight principal

El matching directo por localidad es inviable.

Se adopta estrategia alternativa:

> uso de código postal como ancla territorial intermedia

---

## Avance metodológico

Se implementó pipeline:

1. normalización de provincia → codprov
2. normalización de códigos postales
3. asignación de departamento usando:

   * codprov + codpos
4. evaluación de calidad de matching

Resultados:

* provincia: 100% exacta
* departamento: 98%+ exacta
* residuo explicado por diferencias nominales (no errores geo)

---

## Estado del problema geo

* provincia → resuelto
* departamento → resuelto (operativamente)
* localidad → pendiente
* geocodificación → no necesaria en esta etapa

---

## Riesgos actuales

* calidad del código postal en bases nominales
* ambigüedad residual en localidades
* dependencia de texto libre para localidad final

---

## Oportunidad concreta

* asignación masiva de departamento a personas
* generación de métricas territoriales (primer entregable)
* base para modelo geográfico unificado

---

## Estado general

Fase de diseño superada.
Pipeline ETL territorial validado sobre códigos postales.

Próximo paso:
cruce con Alimentar para asignación de departamento.
