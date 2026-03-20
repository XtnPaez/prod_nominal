# Tablas clave — ddbb_alimentar

## `ddbb_alimentar.titulares`

### Tipo
Persona nominal directa

### Descripción operativa
Registra a la persona titular o adulta responsable asociada al beneficio. Es la mejor tabla del esquema para identificar personas y para iniciar procesos de geolocalización.

### Campos relevantes
| campo | tipo | rol analítico |
|---|---|---|
| `cuiltitular` | numeric | identificador principal |
| `ndoctitular` | varchar(15) | identificador alternativo |
| `fechanactitular` | date | atributo de identidad auxiliar |
| `sexotitular` | bpchar(1) | atributo personal |
| `provincia` | varchar(50) | geografía administrativa |
| `localidad` | varchar(100) | geografía administrativa |
| `cod_postal` | varchar(10) | geografía auxiliar |
| `calle` | varchar(100) | dirección |
| `numero` | varchar(20) | dirección |
| `piso` | varchar(10) | dirección auxiliar |
| `depto` | varchar(10) | dirección auxiliar |
| `monto` | numeric(10,2) | prestación asociada |

### Eje A. Identidad
#### Identificadores presentes
- CUIL/CUIT: `cuiltitular`
- DNI: `ndoctitular`
- Otras claves: `id` técnico

#### Evaluación
- Completitud esperada: alta
- Calidad esperable: buena, porque además tiene índice por `cuiltitular`
- Riesgos: tipo `numeric` en vez de texto; posible pérdida de ceros o inconsistencias de formato al exportar
- Nivel de confianza: **Alto**

### Eje B. Atributos personales
- Nombre / apellido: no está presente
- Sexo: `sexotitular`
- Fecha de nacimiento: `fechanactitular`

#### Evaluación
- Consistencia esperable: media
- Problemas potenciales: ausencia de nombre/apellido limita matching manual o probabilístico
- Nivel de confianza: **Medio**

### Eje C. Relaciones
- Claves de vínculo: `cuiltitular`
- Cardinalidad esperada: 1 titular → N menores
- Posibles joins:
  - con `menores.cuiltitular`
  - con `unidades_convivencia.cuil_titular`
  - con `pa_pagados.cuil`
  - con `titulares_serie.cuil_titular`

#### Evaluación
- Fortaleza relacional: alta
- Riesgos: si hay duplicados por titular, el join se multiplica
- Nivel de integrabilidad: **Alto**

### Eje D. Eventos / prestaciones
- ¿Registra eventos?: parcialmente
- Tipo de evento: prestación monetaria asociada al titular
- Variables temporales: `createdat`, `updatedat`
- Variables monetarias: `monto`

#### Evaluación
- Trazabilidad temporal: baja dentro de la tabla base; mejor en `titulares_serie`
- Utilidad analítica: alta como padrón actual

### Eje E. Geografía
#### Campos geográficos disponibles
- Provincia: `provincia`
- Departamento / municipio: no explícito
- Localidad: `localidad`
- Código postal: `cod_postal`
- Calle: `calle`
- Número: `numero`
- Piso / depto: `piso`, `depto`

#### Calidad geográfica
- Estructurado / texto libre: mixto, mayormente texto libre
- Granularidad: domicilio
- Consistencia interna esperable: media
- Potencial de geolocalización: **Alta**

### Calidad de datos esperable
- Nulls críticos: bajos en identificadores, posibles en componentes de domicilio
- Duplicados: posibles por cargas repetidas
- Formatos inválidos: CUIL/DNI como texto o numeric sin validación explícita
- Inconsistencias internas: provincia-localidad, calle-numero incompletos

### Valor para el registro único de personas
Es tabla candidata a fuente principal para persona adulta responsable dentro del universo Alimentar.

### Decisión analítica
- Prioridad: **Alta**
- Usar como: **fuente principal**
- Requiere normalización previa: **Sí**

### Queries sugeridas
```sql
SELECT cuiltitular, COUNT(*)
FROM ddbb_alimentar.titulares
GROUP BY cuiltitular
HAVING COUNT(*) > 1;
```

```sql
SELECT *
FROM ddbb_alimentar.titulares
WHERE provincia IS NULL
   OR localidad IS NULL;
```

---

## `ddbb_alimentar.menores`

### Tipo
Persona nominal directa

### Descripción operativa
Registra menores beneficiarios vinculados a un titular. Es una tabla nominal útil, pero relacionalmente dependiente.

### Campos relevantes
| campo | tipo | rol analítico |
|---|---|---|
| `cuilmenor` | varchar(15) | identificador principal potencial |
| `ndocmenor` | varchar(15) | DNI alternativo |
| `apellidoynombre` | varchar(50) | atributo nominal |
| `fechadenacimiento` | date | atributo personal |
| `sexo` | bpchar(1) | atributo personal |
| `cuiltitular` | numeric | vínculo con titular |

### Eje A. Identidad
#### Identificadores presentes
- CUIL/CUIT: `cuilmenor`
- DNI: `ndocmenor`
- Otras claves: `id`

#### Evaluación
- Completitud esperada: media
- Calidad esperable: media
- Riesgos: longitud variable, posible mezcla entre CUIL real y valor faltante/incorrecto
- Nivel de confianza: **Medio**

### Eje B. Atributos personales
- Nombre / apellido: `apellidoynombre` combinado
- Sexo: `sexo`
- Fecha de nacimiento: `fechadenacimiento`

#### Evaluación
- Consistencia esperable: media
- Problemas potenciales: nombre no separado; longitud acotada a 50
- Nivel de confianza: **Medio**

### Eje C. Relaciones
- Claves de vínculo: `cuiltitular`
- Cardinalidad esperada: N menores → 1 titular
- Posibles joins:
  - con `titulares.cuiltitular`
  - con `unidades_convivencia.cuil_menor`
  - con `menores_serie.cuil_beneficiario`

#### Evaluación
- Fortaleza relacional: alta
- Riesgos: si `cuiltitular` está ausente, el menor queda huérfano
- Nivel de integrabilidad: **Alto**

### Eje D. Eventos / prestaciones
- ¿Registra eventos?: no directamente
- Tipo de evento: no aplica
- Variables temporales: `createdat`, `updatedat`

#### Evaluación
- Trazabilidad temporal: baja
- Utilidad analítica: alta para universo de beneficiarios menores

### Eje E. Geografía
#### Campos geográficos disponibles
- No tiene geografía propia

#### Calidad geográfica
- Estructurado / texto libre: no aplica
- Granularidad: nula
- Potencial de geolocalización: **Baja** por dependencia del titular

### Calidad de datos esperable
- Nulls críticos: posibles en `cuilmenor` y `ndocmenor`
- Duplicados: posibles por múltiples cargas
- Formatos inválidos: CUIL/DNI no validados
- Inconsistencias internas: menores con titular nulo

### Valor para el registro único de personas
Aporta persona menor nominal y permite reconstrucción de relación familiar/convivencial.

### Decisión analítica
- Prioridad: **Alta**
- Usar como: **fuente principal complementaria**
- Requiere normalización previa: **Sí**

---

## `ddbb_alimentar.unidades_convivencia`

### Tipo
Relaciones

### Descripción operativa
Tabla denormalizada que combina atributos de titular y menor en una misma fila. Útil para explotación rápida, pero conceptualmente mezcla entidad y vínculo.

### Campos relevantes
| campo | tipo | rol analítico |
|---|---|---|
| `cuil_titular` | numeric | vínculo adulto |
| `sexo_titular` | bpchar(1) | atributo titular |
| `edad_titular` | int8 | atributo titular |
| `provincia` | varchar(50) | geografía del hogar |
| `localidad` | varchar(100) | geografía del hogar |
| `calle` | varchar(100) | domicilio |
| `numero` | varchar(20) | domicilio |
| `cuil_menor` | numeric | vínculo menor |
| `nombre_menor` | varchar(100) | atributo menor |
| `sexo_menor` | bpchar(1) | atributo menor |
| `edad_menor` | int8 | atributo menor |

### Eje A. Identidad
- CUIL/CUIT: `cuil_titular`, `cuil_menor`
- DNI: no visible
- Nivel de confianza: **Medio-Alto**

### Eje B. Atributos personales
- No hay fecha de nacimiento
- Hay sexo y edad para ambas partes
- `nombre_menor` presente, pero no nombre del titular
- Nivel de confianza: **Medio**

### Eje C. Relaciones
- Clave de vínculo: par `cuil_titular` + `cuil_menor`
- Cardinalidad esperada: 1 titular → N menores
- Nivel de integrabilidad: **Alto**

### Eje D. Eventos / prestaciones
- Registra monto, pero no período
- Funciona más como snapshot convivencial que como evento puro

### Eje E. Geografía
- Provincia, localidad, código postal, calle, número, piso, depto
- Potencial de geolocalización: **Alta**
- Problema: no queda claro si representa domicilio del hogar o del titular únicamente

### Calidad de datos esperable
- Riesgo alto de duplicación relacional
- Riesgo de inconsistencia con tablas base

### Valor para el registro único de personas
Muy útil para derivar unidades de convivencia u hogares, pero no debe ser tabla maestra de persona.

### Decisión analítica
- Prioridad: **Alta**
- Usar como: **fuente de relación**
- Requiere normalización previa: **Sí**

---

## `ddbb_alimentar.pa_pagados`

### Tipo
Eventos / prestaciones

### Descripción operativa
Tabla de pagos por CUIL y período.

### Campos relevantes
| campo | tipo | rol analítico |
|---|---|---|
| `cuil` | int8 | identificador de beneficiario |
| `r` | int4 | variable a interpretar |
| `importe` | numeric(10,2) | monto |
| `periodo` | varchar(20) | temporalidad |
| `origen` | varchar(10) | procedencia |

### Eje A. Identidad
- CUIL/CUIT: `cuil`
- Nivel de confianza: **Alto**

### Eje B. Atributos personales
- no aplica

### Eje C. Relaciones
- join probable con `titulares.cuiltitular`
- también posible relación con series
- Nivel de integrabilidad: **Alto**

### Eje D. Eventos / prestaciones
- sí, claramente
- tipo: pago
- temporalidad: `periodo`
- monto: `importe`
- Utilidad analítica: **Muy alta**

### Eje E. Geografía
- no tiene campos geográficos
- Potencial de geolocalización: **Nula**

### Calidad de datos esperable
- Duplicados posibles por período
- Riesgo principal: no distinguir persona exacta si hubiera adultos y menores compartiendo lógica de CUIL distinta

### Valor para el registro único de personas
Aporta historial de prestación, no identidad.

### Decisión analítica
- Prioridad: **Alta**
- Usar como: **fuente de eventos**
- Requiere normalización previa: **Sí**, al menos para homogeneizar período

---

## `ddbb_alimentar.titulares_serie`

### Tipo
Eventos / prestaciones

### Descripción operativa
Serie histórica de titulares por período. Amplía la tabla base con nombre, prenatal y variables territoriales.

### Lectura analítica rápida
- mejora atributos respecto de `titulares`
- agrega `apellido_nombre_titular`
- incorpora `periodo`
- geografía sigue siendo texto libre

### Decisión analítica
- Prioridad: **Alta**
- Usar como: **fuente complementaria + historial**
- Requiere normalización previa: **Sí**

---

## `ddbb_alimentar.menores_serie`

### Tipo
Eventos / prestaciones

### Descripción operativa
Serie histórica de menores beneficiarios por período.

### Lectura analítica rápida
- contiene `cuil_beneficiario`, `dni_beneficiario`, `cuil_titular`
- permite observar continuidad temporal del menor
- suma nombre completo y período

### Decisión analítica
- Prioridad: **Alta**
- Usar como: **fuente complementaria + historial**
- Requiere normalización previa: **Sí**
