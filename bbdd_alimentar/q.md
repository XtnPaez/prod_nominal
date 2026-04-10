# alimentar — q

## 1. Crear tabla base

```sql
DROP TABLE IF EXISTS geo_work.alimentar_base;

CREATE TABLE geo_work.alimentar_base
(
    cuil text,
    provincia_fuente text,
    cp_raw text,
    cp_fuente integer,
    codprov_ref text,
    created_at timestamp with time zone DEFAULT now(),
    updated_at timestamp with time zone DEFAULT now()
);
```

---

## 2. Cargar extracto mínimo

```sql
INSERT INTO geo_work.alimentar_base (
    cuil,
    provincia_fuente,
    cp_raw,
    cp_fuente
)
SELECT
    cuiltitular::text,
    provincia::text,
    cod_postal::text,
    NULLIF(regexp_replace(cod_postal::text, '[^0-9]', '', 'g'), '')::integer
FROM ddbb_alimentar.titulares
WHERE cuiltitular IS NOT NULL;
```

---

## 3. Alias de provincias

```sql
DROP TABLE IF EXISTS geo_ref.alias_provincias_alimentar;

CREATE TABLE geo_ref.alias_provincias_alimentar
(
    provincia_fuente text PRIMARY KEY,
    codprov_ref text,
    provincia_ref text
);
```

```sql
INSERT INTO geo_ref.alias_provincias_alimentar VALUES
('BUENOS AIRES','06','BUENOS AIRES'),
('CATAMARCA','10','CATAMARCA'),
('CHACO','22','CHACO'),
('CHUBUT','26','CHUBUT'),
('CIUDAD DE BUENOS AIRES','02','CIUDAD AUTONOMA DE BUENOS AIRES'),
('CORDOBA','14','CORDOBA'),
('CORRIENTES','18','CORRIENTES'),
('ENTRE RIOS','30','ENTRE RIOS'),
('FORMOSA','34','FORMOSA'),
('JUJUY','38','JUJUY'),
('LA PAMPA','42','LA PAMPA'),
('LA RIOJA','46','LA RIOJA'),
('MENDOZA','50','MENDOZA'),
('MISIONES','54','MISIONES'),
('NEUQUEN','58','NEUQUEN'),
('RIO NEGRO','62','RIO NEGRO'),
('SALTA','66','SALTA'),
('SAN JUAN','70','SAN JUAN'),
('SAN LUIS','74','SAN LUIS'),
('SANTA CRUZ','78','SANTA CRUZ'),
('SANTA FE','82','SANTA FE'),
('SANTIAGO DEL ESTERO','86','SANTIAGO DEL ESTERO'),
('TIERRA DEL FUEGO','94','TIERRA DEL FUEGO'),
('TUCUMAN','90','TUCUMAN');
```

```sql
UPDATE geo_work.alimentar_base a
SET codprov_ref = p.codprov_ref
FROM geo_ref.alias_provincias_alimentar p
WHERE a.provincia_fuente = p.provincia_fuente;
```

---

## 4. Crear join

```sql
DROP TABLE IF EXISTS geo_work.alimentar_join;

CREATE TABLE geo_work.alimentar_join
(
    cuil text,
    provincia_fuente text,
    codprov_ref text,
    cp_fuente integer,
    coddepto_ref text,
    cp_match integer,
    fl_match_cp integer,
    fl_match_validado integer
);
```

---

## 5. Join territorial

```sql
WITH cp_unico AS (
    SELECT
        cp,
        codprov_ref,
        MIN(coddepto_ref) AS coddepto_ref
    FROM geo_ref.codigos_postales
    GROUP BY cp, codprov_ref
    HAVING COUNT(DISTINCT coddepto_ref) = 1
)
INSERT INTO geo_work.alimentar_join
SELECT
    a.cuil,
    a.provincia_fuente,
    a.codprov_ref,
    a.cp_fuente,
    u.coddepto_ref,
    u.cp,
    1,
    1
FROM geo_work.alimentar_base a
JOIN cp_unico u
    ON a.cp_fuente = u.cp
   AND a.codprov_ref = u.codprov_ref;
```

---

## 6. Cobertura

```sql
SELECT
    b.total_base,
    j.con_depto,
    ROUND(100.0 * j.con_depto / b.total_base, 2)
FROM
    (SELECT COUNT(*) AS total_base FROM geo_work.alimentar_base) b,
    (SELECT COUNT(*) AS con_depto FROM geo_work.alimentar_join) j;
```

---

## 7. Agregado

```sql
DROP TABLE IF EXISTS geo_work.alimentar_agg_depto;

CREATE TABLE geo_work.alimentar_agg_depto AS
SELECT
    coddepto_ref,
    COUNT(DISTINCT cuil) AS total_cuiles
FROM geo_work.alimentar_join
GROUP BY coddepto_ref;
```
