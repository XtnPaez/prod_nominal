# Registro Único de Personas – Queries y Análisis de Integración

## Objetivo
Evaluar la **posibilidad real de unificar** las bases **Alimentar**, **STESS** y **Educación** en un **Registro Único de Personas** usando el **CUIL** como identificador común, con los datos *tal cual están hoy*.

---

## 1) Query principal – Tamaño del Registro Único (CUIL únicos)

```sql
select count(distinct cuil_norm) as registro_unico_cuil
from (

  select lpad(regexp_replace(cuiltitular::text, '[^0-9]', '', 'g'), 11, '0') as cuil_norm
  from ddbb_alimentar.titulares
  where cuiltitular is not null

  union all

  select lpad(regexp_replace(cuilmenor, '[^0-9]', '', 'g'), 11, '0')
  from ddbb_alimentar.menores
  where cuilmenor is not null and btrim(cuilmenor) <> ''

  union all

  select lpad(regexp_replace(cuil, '[^0-9]', '', 'g'), 11, '0')
  from ddbb_stess.stess_202509
  where cuil is not null and btrim(cuil) <> ''

  union all

  select lpad(regexp_replace(cuil_adulto, '[^0-9]', '', 'g'), 11, '0')
  from ddbb_educacion.vouchers_datos_nominales
  where cuil_adulto is not null and btrim(cuil_adulto) <> ''

  union all

  select lpad(regexp_replace(cuil_menor, '[^0-9]', '', 'g'), 11, '0')
  from ddbb_educacion.vouchers_datos_nominales
  where cuil_menor is not null and btrim(cuil_menor) <> ''

) x
where length(cuil_norm) = 11;
```

**Resultado obtenido:**  
**Registro Único posible:** **8.758.568 personas (CUIL únicos)**

**Qué muestra:**  
La cantidad exacta de personas únicas que pueden consolidarse hoy en un Registro Único, unificando todas las fuentes y eliminando duplicaciones interprograma.

---

## 2) Control de calidad del identificador (IDs válidos)

```sql
select
  count(*) as total_ids,
  sum(case when length(cuil_norm) = 11 then 1 else 0 end) as ids_validos_11,
  sum(case when length(cuil_norm) <> 11 then 1 else 0 end) as ids_invalidos
from (
  select regexp_replace(cuiltitular::text, '[^0-9]', '', 'g') as cuil_norm
  from ddbb_alimentar.titulares where cuiltitular is not null

  union all
  select regexp_replace(cuilmenor, '[^0-9]', '', 'g')
  from ddbb_alimentar.menores

  union all
  select regexp_replace(cuil, '[^0-9]', '', 'g')
  from ddbb_stess.stess_202509

  union all
  select regexp_replace(cuil_adulto, '[^0-9]', '', 'g')
  from ddbb_educacion.vouchers_datos_nominales

  union all
  select regexp_replace(cuil_menor, '[^0-9]', '', 'g')
  from ddbb_educacion.vouchers_datos_nominales
) y;
```

**Resultados obtenidos:**
- Total de identificadores analizados: **9.652.388**
- Identificadores válidos (11 dígitos): **9.652.388**
- Identificadores inválidos: **0**

**Interpretación:**  
No existe pérdida de registros por problemas de formato del CUIL.  
La integración es **técnicamente limpia** desde el punto de vista del identificador.

---

## 3) Suma ingenua vs unión real (solapamiento)

Valores de referencia obtenidos previamente:
- Alimentar (titulares + menores): **6.942.185**
- STESS: **1.025.839**
- Educación (adultos + menores): **1.456.073**

**Suma ingenua:** 9.424.097  
**Registro Único real:** 8.758.568  

**Solapamiento interprograma estimado:**  
**665.529 personas** (≈ **7,1 %** de la suma ingenua)

---

## 4) Conclusiones para el Registro Único

Con los datos actuales, **es plenamente viable** construir un Registro Único de Personas basado en CUIL:

- El identificador es consistente y completo en todas las fuentes.
- No hay pérdida por CUIL inválidos.
- El solapamiento entre programas es moderado y esperable.
- El Registro Único consolidaría **≈ 8,76 millones de personas reales**.

La estrategia correcta es:
- Consolidar identidad **fuera** de las tablas transaccionales.
- Tratar Alimentar, STESS y Educación como **fuentes** del Registro Único.
- Usar el CUIL normalizado como clave primaria canónica.

Este resultado habilita el diseño inmediato de:
- una tabla `registro_unico_personas`,
- reglas de precedencia de atributos,
- y vistas interprograma consistentes para análisis y gestión.
