# CONTROL DE AVANCE

| esquema   | tabla                | geo     | codificacion | cuil→domicilio | valor_geo | estado |
|----------|---------------------|--------|-------------|---------------|----------|--------|
| alimentar | titulares            | alta    | no           | 1 domicilio    | alto      | listo  |
| alimentar | titulares_serie      | alta    | no           | múltiples      | muy alto  | listo  |
| alimentar | unidades_convivencia | alta    | no           | múltiples      | muy alto  | listo  |
| alimentar | menores              | sin geo | n/a          | indirecto      | nulo      | listo  |
| alimentar | menores_serie        | sin geo | n/a          | indirecto      | nulo      | listo  |
| alimentar | pa_pagados           | sin geo | n/a          | no vinculable  | nulo      | listo  |

---

## Avance ETL geo

| componente | estado |
|-----------|--------|
| tabla CP base (correo) | lista |
| tabla CP normalizada | lista |
| codificación provincia en CP | resuelta |
| codificación departamento en CP | resuelta |
| reinterpretación de confianza departamento | aplicada |
| join CP + Alimentar | pendiente |
| asignación de departamento a Alimentar | pendiente |
| asignación de localidad oficial | pendiente |

---

## Métricas ETL CP

| componente | resultado |
|-----------|-----------|
| provincia | 100% exacta |
| departamento | 98.25% exacta |
| departamento aceptable / revisable | 1.75% |
| lectura operativa | éxito |

---

## Estado por esquema

- alimentar: análisis completo / ETL listo para cruce por CP
- anses: pendiente
- stess: pendiente
- educacion: pendiente
- niñez: pendiente

---

## Estado general

Se cerró exitosamente la fase de codificación territorial de la tabla de códigos postales.  
El proyecto entra en etapa de cruce con bases nominales, comenzando por Alimentar.