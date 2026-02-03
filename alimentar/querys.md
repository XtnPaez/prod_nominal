# Queries – Base Alimentar (ddbb_alimentar)

Objetivo: obtener métricas simples de volumen, unicidad y relacionabilidad entre **titulares** y **menores** (clave: **CUIL**).

---

## 1) Titulares – volumen y unicidad

### 1.1 Total de registros en titulares
```sql
select count(*) as titulares_total
from ddbb_alimentar.titulares;
```
**Qué mide:** cantidad total de filas (volumen bruto) en `titulares`.

---

### 1.2 Titulares únicos por CUIL (no nulo)
```sql
select count(distinct cuiltitular) as titulares_cuil_unicos
from ddbb_alimentar.titulares
where cuiltitular is not null;
```
**Qué mide:** cantidad de personas titulares distintas según `cuiltitular`.

---

### 1.3 Titulares con CUIL nulo
```sql
select count(*) as titulares_cuil_null
from ddbb_alimentar.titulares
where cuiltitular is null;
```
**Qué mide:** filas sin identificador CUIL (problema de integridad de clave).

---

### 1.4 Cantidad de CUIL de titulares duplicados (cuántos CUIL se repiten)
```sql
select count(*) as cuils_duplicados
from (
  select cuiltitular
  from ddbb_alimentar.titulares
  where cuiltitular is not null
  group by cuiltitular
  having count(*) > 1
) x;
```
**Qué mide:** cuántos valores distintos de `cuiltitular` aparecen en más de una fila (indicador de duplicación).

---

## 2) Menores – volumen y unicidad

### 2.1 Total de registros en menores
```sql
select count(*) as menores_total
from ddbb_alimentar.menores;
```
**Qué mide:** cantidad total de filas (volumen bruto) en `menores`.

---

### 2.2 Menores únicos por CUIL (no nulo ni vacío)
```sql
select count(distinct cuilmenor) as menores_cuil_unicos
from ddbb_alimentar.menores
where cuilmenor is not null and btrim(cuilmenor) <> '';
```
**Qué mide:** cantidad de personas menores distintas según `cuilmenor`.

---

### 2.3 Menores con CUIL nulo o vacío
```sql
select count(*) as menores_cuil_null_o_vacio
from ddbb_alimentar.menores
where cuilmenor is null or btrim(cuilmenor) = '';
```
**Qué mide:** filas de menores sin identificador usable (nulo o solo espacios).

---

### 2.4 Cantidad de CUIL de menor duplicados (cuántos CUIL se repiten)
```sql
select count(*) as cuilmenor_duplicados
from (
  select cuilmenor
  from ddbb_alimentar.menores
  where cuilmenor is not null and btrim(cuilmenor) <> ''
  group by cuilmenor
  having count(*) > 1
) x;
```
**Qué mide:** cuántos valores distintos de `cuilmenor` aparecen en más de una fila (indicador de duplicación).

---

## 3) Relación titulares–menores (relacionabilidad)

### 3.1 Titulares con al menos 1 menor (según la tabla menores)
```sql
select count(distinct cuiltitular) as titulares_con_menores
from ddbb_alimentar.menores
where cuiltitular is not null;
```
**Qué mide:** cuántos titulares aparecen referenciados en `menores` (cobertura de vínculo).

---

### 3.2 Titulares sin menores (según cruce titulares vs menores)
```sql
select count(distinct t.cuiltitular) as titulares_sin_menores
from ddbb_alimentar.titulares t
left join ddbb_alimentar.menores m
  on m.cuiltitular = t.cuiltitular
where t.cuiltitular is not null
  and m.cuiltitular is null;
```
**Qué mide:** cuántos titulares existen en `titulares` pero no tienen ningún menor asociado en `menores`.

---

### 3.3 Distribución: menores por titular (resumen estadístico)
```sql
with por_titular as (
  select m.cuiltitular,
         count(*) as menores_total,
         count(distinct m.cuilmenor) as menores_unicos
  from ddbb_alimentar.menores m
  where m.cuiltitular is not null
  group by m.cuiltitular
)
select
  count(*) as titulares_con_menores,
  avg(menores_total)::numeric(10,2) as prom_menores_total,
  min(menores_total) as min_menores_total,
  percentile_cont(0.50) within group (order by menores_total) as p50_menores_total,
  percentile_cont(0.90) within group (order by menores_total) as p90_menores_total,
  percentile_cont(0.99) within group (order by menores_total) as p99_menores_total,
  max(menores_total) as max_menores_total
from por_titular;
```
**Qué mide:** distribución de cantidad de menores por titular:
- promedio, mínimo, mediana (p50), percentiles altos (p90, p99) y máximo.
- también incluye `menores_unicos` por titular dentro del CTE (útil si luego querés auditar duplicados por titular).

---

### 3.4 Menores sin titular (integridad de vínculo)
```sql
select count(*) as menores_sin_titular
from ddbb_alimentar.menores
where cuiltitular is null;
```
**Qué mide:** filas de `menores` que no referencian a ningún titular (orfandad inmediata).

---

### 3.5 Menores cuyo titular no existe en titulares (orfandad por cruce)
```sql
select count(*) as menores_titular_inexistente
from ddbb_alimentar.menores m
left join ddbb_alimentar.titulares t
  on t.cuiltitular = m.cuiltitular
where m.cuiltitular is not null
  and t.cuiltitular is null;
```
**Qué mide:** menores que sí tienen `cuiltitular`, pero ese titular no está en la tabla `titulares` (orfandad referencial real).

---

## Nota operativa
- Si querés acelerar estas métricas, índices recomendados:
  - `titulares(cuiltitular)` (ya existe)
  - `menores(cuiltitular)` (existe)
  - `menores(cuilmenor)` (recomendable si se audita duplicación por menor frecuentemente)
