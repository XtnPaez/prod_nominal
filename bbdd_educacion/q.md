# educacion — q

## 1. base

```sql
DROP TABLE IF EXISTS geo_work.educacion_base;

CREATE TABLE geo_work.educacion_base (
    cuil text,
    provincia_fuente text,
    departamento_fuente text,
    localidad_fuente text,
    calle_fuente text,
    numero_fuente text,
    cp_raw text,
    cp_fuente integer,
    codprov_ref text,
    coddepto_ref text
);
```

## 2. carga

```sql
INSERT INTO geo_work.educacion_base
SELECT
    cuit::text,
    provincia,
    partido,
    localidad,
    calle,
    num_casilla,
    codigo_postal,
    NULLIF(regexp_replace(codigo_postal::text, '[^0-9]', '', 'g'), '')::integer,
    NULL,
    NULL
FROM ddbb_educacion.becas_belgrano_serie;
```

## 3. alias provincias

```sql
UPDATE geo_work.educacion_base e
SET codprov_ref = p.codprov_ref
FROM geo_ref.alias_provincias_educacion p
WHERE e.provincia_fuente = p.provincia_fuente;
```

## 4. alias departamentos (similitud)

```sql
-- ver pipeline.md (uso de pg_trgm)
```

## 5. join

```sql
TRUNCATE geo_work.educacion_join;

INSERT INTO geo_work.educacion_join
SELECT
    e.cuil,
    e.provincia_fuente,
    e.departamento_fuente,
    e.localidad_fuente,
    e.codprov_ref,
    e.cp_fuente,
    a.coddepto_ref,
    NULL::integer,
    0,
    1
FROM geo_work.educacion_base e
JOIN geo_ref.alias_departamentos_educacion a
  ON e.provincia_fuente = a.provincia_fuente
 AND e.departamento_fuente = a.departamento_fuente;
```

## 6. cobertura

```sql
SELECT
    COUNT(*) total,
    (SELECT COUNT(*) FROM geo_work.educacion_join) con_depto
FROM geo_work.educacion_base;
```
