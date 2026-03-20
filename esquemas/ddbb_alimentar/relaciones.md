# Relaciones — ddbb_alimentar

## Eje relacional principal

El esquema se organiza alrededor de `cuiltitular`.

## Relaciones identificadas

### 1. Titular → menores

```sql
menores.cuiltitular = titulares.cuiltitular
```

- cardinalidad esperada: **1 a N**
- uso: reconstrucción de grupo conviviente o familiar operativo

### 2. Titular → unidad de convivencia

```sql
unidades_convivencia.cuil_titular = titulares.cuiltitular
```

- cardinalidad esperada: **1 a N**
- uso: derivar hogares y chequear consistencia de domicilio

### 3. Menor → unidad de convivencia

```sql
unidades_convivencia.cuil_menor = menores.cuilmenor / menores_serie.cuil_beneficiario
```

- cardinalidad esperada: **1 a 1** o **1 a N** según histórico/cortes
- riesgo: diferencias de tipo de dato y formato

### 4. Titular → pagos

```sql
pa_pagados.cuil = titulares.cuiltitular
```

- cardinalidad esperada: **1 a N** por período
- uso: historia de prestación

### 5. Titular → serie histórica

```sql
titulares_serie.cuil_titular = titulares.cuiltitular
```

### 6. Menor → serie histórica

```sql
menores_serie.cuil_beneficiario = menores.cuilmenor
```

## Riesgos relacionales

- tipos distintos para los mismos identificadores (`numeric`, `varchar`, `int8`)
- ausencia de constraints de foreign key explícitas
- posibilidad de duplicados por múltiples períodos o múltiples cargas

## Decisiones sugeridas

- estandarizar todos los CUIL como texto limpio de 11 dígitos
- separar joins de padrón actual y joins históricos
- derivar tabla puente `persona_relaciones` a partir de titular-menor
