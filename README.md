# Proyecto de análisis geográfico de bases nominales

## Propósito

Este repositorio se enfoca exclusivamente en el análisis geográfico de bases nominales.

El objetivo no es estudiar integralmente cada esquema ni modelar la persona en todos sus atributos, sino responder tres preguntas operativas:

1. qué tablas tienen datos geográficos y cuáles no
2. si esos datos geográficos están codificados, parcialmente codificados o en texto libre
3. si para cada CUIL/CUIT se puede obtener una dirección, una localización aproximada o múltiples domicilios

## Preguntas rectoras

Toda tabla debe analizarse desde estas preguntas:

- ¿Tiene campos geográficos?
- ¿Qué tipo de geografía aporta?
- ¿La geografía está codificada o no?
- ¿El dato sirve para georreferenciar personas?
- ¿La unidad identificable es persona, hogar, prestación o establecimiento?
- ¿Se puede vincular un CUIL/CUIT con una dirección?
- ¿Puede haber más de una dirección por CUIL/CUIT?

## Alcance

Este repositorio se concentra en:

- detección de campos geográficos
- evaluación de granularidad geográfica
- evaluación de codificación
- evaluación de trazabilidad domicilio ↔ CUIL/CUIT
- identificación de tablas con potencial de geocodificación
- documentación de fuentes oficiales codificadas para normalización y cruce

Queda fuera del alcance principal:

- análisis funcional completo de programas
- modelado integral de relaciones familiares
- análisis de prestaciones no vinculadas a localización
- calidad general de datos que no impacte en georreferenciación

## Ejes de análisis obligatorios

Cada tabla debe analizarse con estos ejes:

### A. Presencia geográfica

- tiene o no tiene campos geográficos
- campos detectados
- tipo de dato geográfico presente

### B. Nivel de granularidad

- país
- provincia
- departamento / partido
- municipio
- localidad
- código postal
- calle
- número
- piso / departamento
- coordenadas
- establecimiento o referencia territorial

### C. Codificación

Clasificación esperada:

- codificada
- parcialmente codificada
- no codificada

Se debe indicar:

- qué campo está codificado
- contra qué catálogo o capa podría validarse
- qué campos están en texto libre

### D. Vinculación con CUIL/CUIT

Determinar si la tabla permite asociar una geografía a:

- CUIL/CUIT directo
- DNI
- titular / beneficiario / menor / adulto
- ninguna entidad nominal clara

También debe indicarse:

- una dirección por CUIL/CUIT
- múltiples direcciones por CUIL/CUIT a lo largo del tiempo
- una dirección compartida por múltiples personas
- imposibilidad de resolver domicilio

### E. Potencial de georreferenciación

Clasificación:

- alto: dirección completa o coordenadas
- medio: localidad / municipio / CP
- bajo: solo provincia
- nulo: sin dato geográfico utilizable

## Tipología de tablas

Las tablas deben clasificarse en una de estas categorías:

- nominal con geografía directa
- nominal sin geografía
- evento con geografía
- relación con geografía derivada
- establecimiento / operativo / sede
- catálogo geográfico
- catálogo no geográfico

## Productos del análisis

Para cada esquema se debe producir:

- inventario de tablas con y sin geografía
- evaluación de codificación
- evaluación de posibilidad de obtener domicilio por CUIL/CUIT
- identificación de tablas prioritarias para geocodificación
- identificación de tablas que requieren normalización previa

En la raíz del proyecto debe existir:

- un brief operativo
- una tabla de control de avance
- un documento de fuentes oficiales

## Regla práctica

Si una tabla no ayuda a localizar personas, hogares, prestaciones territorializadas o establecimientos, su valor para este proyecto es secundario.
