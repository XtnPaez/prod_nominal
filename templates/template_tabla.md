# Plantilla de análisis de tabla

## Tabla
`<schema>.<tabla>`

## Tipo
- Persona nominal directa / Relaciones / Eventos-prestaciones / Catálogo-dimensión

## Descripción operativa
Breve explicación de qué registra la tabla y para qué parece haber sido diseñada.

## Campos relevantes
| campo | tipo | rol analítico |
|---|---|---|
| | | |

## Eje A. Identidad
### Identificadores presentes
- CUIL/CUIT:
- DNI:
- Otras claves:

### Evaluación
- Completitud:
- Calidad esperable:
- Riesgos:
- Nivel de confianza: Alto / Medio / Bajo

## Eje B. Atributos personales
- Nombre / apellido:
- Sexo:
- Fecha de nacimiento:
- Otros atributos:

### Evaluación
- Consistencia esperable:
- Problemas potenciales:
- Nivel de confianza: Alto / Medio / Bajo

## Eje C. Relaciones
- Claves de vínculo:
- Cardinalidad esperada:
- Cardinalidad probable:
- Posibles joins:

### Evaluación
- Fortaleza relacional:
- Riesgos:
- Nivel de integrabilidad: Alto / Medio / Bajo

## Eje D. Eventos / prestaciones
- ¿Registra eventos?:
- Tipo de evento:
- Variables temporales:
- Variables monetarias o de estado:

### Evaluación
- Trazabilidad temporal:
- Utilidad analítica:

## Eje E. Geografía
### Campos geográficos disponibles
- Provincia:
- Departamento / municipio:
- Localidad:
- Código postal:
- Calle:
- Número:
- Piso / depto:
- Otros:

### Calidad geográfica
- Estructurado / texto libre:
- Granularidad:
- Consistencia interna esperable:
- Potencial de geolocalización: Alta / Media / Baja / Nula

## Calidad de datos esperable
- Nulls críticos:
- Duplicados:
- Formatos inválidos:
- Inconsistencias internas:

## Valor para el registro único de personas
Explicación breve del aporte concreto de la tabla al modelo PERSONA.

## Decisión analítica
- Prioridad: Alta / Media / Baja
- Usar como: fuente principal / fuente complementaria / fuente de relación / fuente de eventos / catálogo
- Requiere normalización previa: Sí / No

## Queries sugeridas
```sql
-- completar
```

## Observaciones
Notas libres.
