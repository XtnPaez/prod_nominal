[Volver a Readme](https://asimov.cncps.gob.ar/cpaez/prod_nominal)

# Queries – Base Educación (ddbb_educacion)

Objetivo: replicar la lógica aplicada en **Alimentar** para medir **volumen**, **unicidad** y **relacionabilidad**, usando como unidad de persona el **CUIL/CUIT**.

---

## 1) Tabla `vouchers_aprobados` (adulto–institución)

### 1.1 Total de registros
```sql
select count(*) as vouchers_aprobados_total
from ddbb_educacion.vouchers_aprobados;
```
Cantidad total de filas (volumen bruto).

---

### 1.2 Adultos únicos (por CUIT)
```sql
select count(distinct cuit) as adultos_unicos_cuit
from ddbb_educacion.vouchers_aprobados
where cuit is not null and btrim(cuit) <> '';
```
Cantidad de personas adultas distintas en esta tabla.

---

### 1.3 Instituciones únicas (por CUE)
```sql
select count(distinct cue) as instituciones_unicas_cue
from ddbb_educacion.vouchers_aprobados
where cue is not null and btrim(cue) <> '';
```
Cantidad de establecimientos educativos distintos.

---

### 1.4 Pares (CUIT, CUE) únicos
```sql
select count(distinct (cuit, cue)) as pares_cuit_cue_unicos
from ddbb_educacion.vouchers_aprobados
where cuit is not null and btrim(cuit) <> ''
  and cue  is not null and btrim(cue)  <> '';
```
Chequeo lógico de la restricción UNIQUE del vínculo adulto–institución.

---

### 1.5 Duplicados del par (CUIT, CUE)
```sql
select cuit, cue, count(*) as repeticiones
from ddbb_educacion.vouchers_aprobados
group by cuit, cue
having count(*) > 1
order by repeticiones desc
limit 20;
```
Detecta duplicación del vínculo (no debería devolver filas).

---

### 1.6 Distribución: instituciones por adulto
```sql
with por_adulto as (
  select cuit, count(*) as cues_por_adulto
  from ddbb_educacion.vouchers_aprobados
  where cuit is not null and btrim(cuit) <> ''
  group by cuit
)
select
  count(*) as adultos_con_al_menos_1_cue,
  avg(cues_por_adulto)::numeric(10,2) as prom_cues_por_adulto,
  min(cues_por_adulto) as min_cues,
  percentile_cont(0.50) within group (order by cues_por_adulto) as p50_cues,
  percentile_cont(0.90) within group (order by cues_por_adulto) as p90_cues,
  percentile_cont(0.99) within group (order by cues_por_adulto) as p99_cues,
  max(cues_por_adulto) as max_cues
from por_adulto;
```
Mide cuántas instituciones tiene asociado cada adulto.

---

### 1.7 Nulos o vacíos en claves
```sql
select
  sum(case when cuit is null or btrim(cuit) = '' then 1 else 0 end) as cuit_null_o_vacio,
  sum(case when cue  is null or btrim(cue)  = '' then 1 else 0 end) as cue_null_o_vacio
from ddbb_educacion.vouchers_aprobados;
```
Control básico de integridad de claves.

---

## 2) Tabla `vouchers_datos_nominales` (adulto–menor)

### 2.1 Total de registros
```sql
select count(*) as datos_nominales_total
from ddbb_educacion.vouchers_datos_nominales;
```
Volumen bruto de vínculos adulto–menor.

---

### 2.2 Adultos únicos (por CUIL)
```sql
select count(distinct cuil_adulto) as adultos_unicos_cuil
from ddbb_educacion.vouchers_datos_nominales
where cuil_adulto is not null and btrim(cuil_adulto) <> '';
```
Cantidad de adultos distintos en la tabla.

---

### 2.3 Menores únicos (por CUIL)
```sql
select count(distinct cuil_menor) as menores_unicos_cuil
from ddbb_educacion.vouchers_datos_nominales
where cuil_menor is not null and btrim(cuil_menor) <> '';
```
Cantidad de menores distintos.

---

### 2.4 Pares (adulto, menor) únicos
```sql
select count(distinct (cuil_adulto, cuil_menor)) as pares_adulto_menor_unicos
from ddbb_educacion.vouchers_datos_nominales
where cuil_adulto is not null and btrim(cuil_adulto) <> ''
  and cuil_menor  is not null and btrim(cuil_menor)  <> '';
```
Chequeo lógico de la restricción UNIQUE del vínculo adulto–menor.

---

### 2.5 Duplicados del par (adulto, menor)
```sql
select cuil_adulto, cuil_menor, count(*) as repeticiones
from ddbb_educacion.vouchers_datos_nominales
group by cuil_adulto, cuil_menor
having count(*) > 1
order by repeticiones desc
limit 20;
```
Detecta duplicaciones del vínculo (no debería devolver filas).

---

### 2.6 Distribución: menores por adulto
```sql
with por_adulto as (
  select cuil_adulto, count(*) as menores_por_adulto
  from ddbb_educacion.vouchers_datos_nominales
  where cuil_adulto is not null and btrim(cuil_adulto) <> ''
  group by cuil_adulto
)
select
  count(*) as adultos_con_al_menos_1_menor,
  avg(menores_por_adulto)::numeric(10,2) as prom_menores_por_adulto,
  min(menores_por_adulto) as min_menores,
  percentile_cont(0.50) within group (order by menores_por_adulto) as p50_menores,
  percentile_cont(0.90) within group (order by menores_por_adulto) as p90_menores,
  percentile_cont(0.99) within group (order by menores_por_adulto) as p99_menores,
  max(menores_por_adulto) as max_menores
from por_adulto;
```
Mide cuántos menores están asociados a cada adulto.

---

### 2.7 Nulos o vacíos en claves
```sql
select
  sum(case when cuil_adulto is null or btrim(cuil_adulto) = '' then 1 else 0 end) as cuil_adulto_null_o_vacio,
  sum(case when cuil_menor  is null or btrim(cuil_menor)  = '' then 1 else 0 end) as cuil_menor_null_o_vacio
from ddbb_educacion.vouchers_datos_nominales;
```
Control básico de integridad de claves.

---

## 3) Cruce entre tablas (adultos)

### 3.1 Adultos presentes en ambas tablas
```sql
select count(distinct a.cuit) as adultos_en_ambas
from ddbb_educacion.vouchers_aprobados a
join ddbb_educacion.vouchers_datos_nominales d
  on d.cuil_adulto = a.cuit
where a.cuit is not null and btrim(a.cuit) <> '';
```
Mide intersección directa entre ambas fuentes.

---

### 3.2 Adultos solo en vouchers_aprobados
```sql
select count(distinct a.cuit) as adultos_solo_aprobados
from ddbb_educacion.vouchers_aprobados a
left join ddbb_educacion.vouchers_datos_nominales d
  on d.cuil_adulto = a.cuit
where a.cuit is not null and btrim(a.cuit) <> ''
  and d.cuil_adulto is null;
```
Adultos con institución asociada pero sin vínculo adulto–menor.

---

### 3.3 Adultos solo en vouchers_datos_nominales
```sql
select count(distinct d.cuil_adulto) as adultos_solo_datos_nominales
from ddbb_educacion.vouchers_datos_nominales d
left join ddbb_educacion.vouchers_aprobados a
  on a.cuit = d.cuil_adulto
where d.cuil_adulto is not null and btrim(d.cuil_adulto) <> ''
  and a.cuit is null;
```
Adultos con menores asociados pero sin vínculo institucional.

---

## Nota técnica
Si la intersección (3.1) da cero, el problema no es de datos sino de **normalización de identificadores** (CUIT vs CUIL).  
Antes de integrar con otras bases, se recomienda unificar ambos a un único campo lógico (`cuil_persona`).
