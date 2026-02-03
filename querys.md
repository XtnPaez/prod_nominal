[Volver a Readme](https://asimov.cncps.gob.ar/cpaez/prod_nominal)

# Queries – STESS (ddbb_stess) 

Objetivo: obtener métricas simples (volumen, unicidad, recurrencia, calidad mínima y cobertura del padrón) para elaborar el informe al estilo **Alimentar**.  
Unidad de análisis: **PERSONA (CUIL)**.  
Tabla principal: `ddbb_stess.stess_202509` (eventos / liquidaciones).  
Tabla de padrón lógico: `ddbb_stess.padron_stess`.

---

## 1) Volumen y cobertura (stess_202509)

### 1.1 Total de eventos (filas)
```sql
select count(*) as stess_total_eventos
from ddbb_stess.stess_202509;
```
**Qué muestra:** volumen bruto de la tabla (cantidad total de registros de liquidación).

---

### 1.2 Personas únicas por CUIL
```sql
select count(distinct cuil) as personas_unicas_cuil
from ddbb_stess.stess_202509
where cuil is not null and btrim(cuil) <> '';
```
**Qué muestra:** cantidad de personas distintas que aparecen en la base (cobertura nominal por CUIL).

---

### 1.3 Eventos con CUIL nulo o vacío
```sql
select count(*) as eventos_cuil_null_o_vacio
from ddbb_stess.stess_202509
where cuil is null or btrim(cuil) = '';
```
**Qué muestra:** registros no integrables por falta de CUIL (si da >0, es un problema crítico).

---

## 2) Recurrencia por persona (cuántos eventos tiene cada CUIL)

### 2.1 Distribución de eventos por persona (resumen estadístico)
```sql
with por_persona as (
  select cuil, count(*) as eventos_por_persona
  from ddbb_stess.stess_202509
  where cuil is not null and btrim(cuil) <> ''
  group by cuil
)
select
  count(*) as personas_con_eventos,
  avg(eventos_por_persona)::numeric(10,2) as prom_eventos_por_persona,
  min(eventos_por_persona) as min_eventos,
  percentile_cont(0.50) within group (order by eventos_por_persona) as p50_eventos,
  percentile_cont(0.90) within group (order by eventos_por_persona) as p90_eventos,
  percentile_cont(0.99) within group (order by eventos_por_persona) as p99_eventos,
  max(eventos_por_persona) as max_eventos
from por_persona;
```
**Qué muestra:** distribución de “eventos por persona”:
- promedio, mínimo, mediana (p50), percentiles altos (p90, p99) y máximo.
Sirve para dimensionar si STESS es “1 evento por persona” o “múltiples eventos por persona”.

---

## 3) Calidad nominal mínima

### 3.1 Distribución de valores de sexo
```sql
select sexo, count(*) as eventos
from ddbb_stess.stess_202509
group by sexo
order by eventos desc;
```
**Qué muestra:** frecuencias de códigos de sexo dentro de los eventos.
Sirve para detectar valores fuera de dominio o codificación inesperada.

---

### 3.2 Tipo de documento nulo o vacío
```sql
select count(*) as tipo_doc_null_o_vacio
from ddbb_stess.stess_202509
where tipo_doc is null or btrim(tipo_doc) = '';
```
**Qué muestra:** completitud del campo `tipo_doc` (si da >0, falta un dato nominal clave).

---

## 4) Cobertura del padrón lógico (padron_stess)

### 4.1 Personas de eventos presentes en `padron_stess`
```sql
select count(distinct s.cuil) as personas_en_padron
from ddbb_stess.stess_202509 s
join ddbb_stess.padron_stess p
  on p.cuil = s.cuil
where s.cuil is not null and btrim(s.cuil) <> '';
```
**Qué muestra:** cuántas personas con eventos están efectivamente representadas en el padrón lógico.

---

### 4.2 Personas de eventos NO presentes en `padron_stess`
```sql
select count(distinct s.cuil) as personas_fuera_padron
from ddbb_stess.stess_202509 s
left join ddbb_stess.padron_stess p
  on p.cuil = s.cuil
where s.cuil is not null and btrim(s.cuil) <> ''
  and p.cuil is null;
```
**Qué muestra:** brecha del padrón lógico respecto a los eventos (si da >0, el padrón está incompleto).

---

## Opcional (si querés auditar outliers)

### O.1 Top CUIL con más eventos
```sql
select cuil, count(*) as eventos_por_persona
from ddbb_stess.stess_202509
where cuil is not null and btrim(cuil) <> ''
group by cuil
order by eventos_por_persona desc
limit 20;
```
**Qué muestra:** casos extremos de recurrencia (útil para detectar duplicaciones o patrones administrativos).
