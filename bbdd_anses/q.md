# bbdd_anses — q

## 1. Crear tabla base

```sql
DROP TABLE IF EXISTS geo_work.anses_base;

CREATE TABLE geo_work.anses_base
(
    cuil text,
    codprov_fuente text,
    cp_fuente integer,
    codprov_ref text,
    created_at timestamp with time zone DEFAULT now(),
    updated_at timestamp with time zone DEFAULT now()
);
```

## 2. Cargar extracto mínimo

```sql
INSERT INTO geo_work.anses_base (
    cuil,
    codprov_fuente,
    cp_fuente
)
SELECT
    cuil_cuit_nu::text AS cuil,
    provincia_cd::text AS codprov_fuente,
    codigo_postal_nu::integer AS cp_fuente
FROM ddbb_anses.anses
WHERE cuil_cuit_nu IS NOT NULL;
```

## 3. Crear alias de provincias ANSES

```sql
DROP TABLE IF EXISTS geo_ref.alias_provincias_anses;

CREATE TABLE geo_ref.alias_provincias_anses
(
    codprov_fuente text PRIMARY KEY,
    provincia_fuente text,
    codprov_ref text,
    provincia_ref text,
    created_at timestamp with time zone DEFAULT now(),
    updated_at timestamp with time zone DEFAULT now()
);
```

```sql
INSERT INTO geo_ref.alias_provincias_anses (
    codprov_fuente,
    provincia_fuente,
    codprov_ref,
    provincia_ref
)
VALUES
('01','CAPITAL FEDERAL','02','CIUDAD AUTONOMA DE BUENOS AIRES'),
('02','BUENOS AIRES','06','BUENOS AIRES'),
('03','CATAMARCA','10','CATAMARCA'),
('04','CORDOBA','14','CORDOBA'),
('05','CORRIENTES','18','CORRIENTES'),
('06','ENTRE RIOS','30','ENTRE RIOS'),
('07','JUJUY','38','JUJUY'),
('08','LA RIOJA','46','LA RIOJA'),
('09','MENDOZA','50','MENDOZA'),
('10','SALTA','66','SALTA'),
('11','SAN JUAN','70','SAN JUAN'),
('12','SAN LUIS','74','SAN LUIS'),
('13','SANTA FE','82','SANTA FE'),
('14','SANTIAGO DEL ESTERO','86','SANTIAGO DEL ESTERO'),
('15','TUCUMAN','90','TUCUMAN'),
('16','CHACO','22','CHACO'),
('17','CHUBUT','26','CHUBUT'),
('18','FORMOSA','34','FORMOSA'),
('19','LA PAMPA','42','LA PAMPA'),
('20','MISIONES','54','MISIONES'),
('21','NEUQUEN','58','NEUQUEN'),
('22','RIO NEGRO','62','RIO NEGRO'),
('23','SANTA CRUZ','78','SANTA CRUZ'),
('24','TIERRA DEL FUEGO','94','TIERRA DEL FUEGO'),
('99','SIN INFORMAR',NULL,NULL);
```

## 4. Asignar provincia de referencia

```sql
UPDATE geo_work.anses_base a
SET
    codprov_ref = p.codprov_ref,
    updated_at = now()
FROM geo_ref.alias_provincias_anses p
WHERE a.codprov_fuente = p.codprov_fuente;
```

## 5. Crear tabla join

```sql
DROP TABLE IF EXISTS geo_work.anses_join;

CREATE TABLE geo_work.anses_join
(
    cuil text,
    codprov_fuente text,
    codprov_ref text,
    cp_fuente integer,
    coddepto_ref text,
    cp_match integer,
    fl_match_cp integer,
    fl_match_validado integer,
    created_at timestamp with time zone DEFAULT now(),
    updated_at timestamp with time zone DEFAULT now()
);
```

## 6. Ejecutar join territorial

```sql
WITH cp_unico AS (
    SELECT
        cp,
        codprov_ref,
        MIN(coddepto_ref) AS coddepto_ref
    FROM geo_ref.codigos_postales
    WHERE cp IS NOT NULL
      AND codprov_ref IS NOT NULL
      AND coddepto_ref IS NOT NULL
    GROUP BY cp, codprov_ref
    HAVING COUNT(DISTINCT coddepto_ref) = 1
)
INSERT INTO geo_work.anses_join (
    cuil,
    codprov_fuente,
    codprov_ref,
    cp_fuente,
    coddepto_ref,
    cp_match,
    fl_match_cp,
    fl_match_validado
)
SELECT
    a.cuil,
    a.codprov_fuente,
    a.codprov_ref,
    a.cp_fuente,
    u.coddepto_ref,
    u.cp,
    1 AS fl_match_cp,
    1 AS fl_match_validado
FROM geo_work.anses_base a
JOIN cp_unico u
    ON a.cp_fuente = u.cp
   AND a.codprov_ref = u.codprov_ref;
```

## 7. Medir cobertura

```sql
SELECT
    b.total_base,
    j.con_depto,
    ROUND(100.0 * j.con_depto / NULLIF(b.total_base, 0), 2) AS pct_sobre_total
FROM
    (SELECT COUNT(*) AS total_base FROM geo_work.anses_base) b,
    (SELECT COUNT(*) AS con_depto FROM geo_work.anses_join) j;
```

## 8. Crear agregado por departamento

```sql
DROP TABLE IF EXISTS geo_work.anses_agg_depto;

CREATE TABLE geo_work.anses_agg_depto AS
SELECT
    coddepto_ref,
    COUNT(DISTINCT cuil) AS total_cuiles
FROM geo_work.anses_join
WHERE coddepto_ref IS NOT NULL
GROUP BY coddepto_ref;
```
