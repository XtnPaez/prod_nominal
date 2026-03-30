# Q — Queries del piloto

## 1. Limpieza y preparación

```sql
UPDATE piloto_nominal.piloto_titulares
SET
    codprov_siempro = NULL,
    provincia_siempro = NULL,
    coddepto_siempro = NULL,
    departamento_siempro = NULL,
    localidad_siempro = NULL,
    cp_siempro_match = NULL,
    score_match_siempro = NULL,
    confianza_match_siempro = NULL,
    fl_match_siempro = NULL,
    fl_match_siempro_validado = NULL;
```

---

## 2. Join con tabla SIEMPRO

```sql
WITH candidatos AS (
    SELECT
        t.cuil,
        t.cp_declarado,
        t.codprov_declarado,

        cp.codprov_ign,
        cp.provincia_ign,
        cp.coddepto_ign,
        cp.departamento_ign,
        cp.localidad_correo,
        cp.cp AS cp_match,

        CASE
            WHEN t.codprov_declarado = cp.codprov_ign THEN 1
            ELSE 0
        END AS match_provincia,

        ROW_NUMBER() OVER (
            PARTITION BY t.cuil
            ORDER BY
                CASE
                    WHEN t.codprov_declarado = cp.codprov_ign THEN 1
                    ELSE 0
                END DESC
        ) AS rn

    FROM piloto_nominal.piloto_titulares t
    JOIN unidades_geoestadisticas.codigos_postales_2026_siempro cp
        ON t.cp_declarado = cp.cp
    WHERE t.cp_declarado IS NOT NULL
),
mejor_match AS (
    SELECT *
    FROM candidatos
    WHERE rn = 1
)
UPDATE piloto_nominal.piloto_titulares t
SET
    codprov_siempro = m.codprov_ign,
    provincia_siempro = m.provincia_ign,
    coddepto_siempro = m.coddepto_ign,
    departamento_siempro = m.departamento_ign,
    localidad_siempro = m.localidad_correo,
    cp_siempro_match = m.cp_match,
    score_match_siempro = m.match_provincia,
    confianza_match_siempro = CASE
        WHEN m.match_provincia = 1 THEN 'alta'
        ELSE 'media'
    END,
    fl_match_siempro = 1,
    fl_match_siempro_validado = CASE
        WHEN m.match_provincia = 1 THEN 1
        ELSE 0
    END,
    updated_at = now()
FROM mejor_match m
WHERE t.cuil = m.cuil;
```

---

## 3. Match validado (equivalente piloto viejo)

```sql
SELECT
    COUNT(*) AS cantidad_match_validado_siempro,
    ROUND(
        100.0 * COUNT(*) / (SELECT COUNT(*) FROM piloto_nominal.piloto_titulares),
        2
    ) AS porcentaje_sobre_total
FROM piloto_nominal.piloto_titulares
WHERE coddepto_siempro IS NOT NULL
  AND codprov_declarado = codprov_siempro;
```

---

## 4. Cobertura de asignación de departamento

```sql
SELECT
    COUNT(*) FILTER (WHERE coddepto_siempro IS NOT NULL) AS con_depto,
    COUNT(*) AS total,
    ROUND(
        100.0 * COUNT(*) FILTER (WHERE coddepto_siempro IS NOT NULL) / COUNT(*),
        2
    ) AS porcentaje_cobertura
FROM piloto_nominal.piloto_titulares;
```

---

## 5. Comparación completa (declarado vs apócrifo vs siempro)

```sql
SELECT
    cuil,

    -- declarado
    provincia_declarada,
    localidad_declarada,
    cp_declarado,
    codprov_declarado,

    -- apócrifo
    codprov_apocrifo,
    coddepto_apocrifo,
    fl_match_apocrifo,
    fl_match_apocrifo_validado,

    -- siempro
    codprov_siempro,
    coddepto_siempro,
    fl_match_siempro,
    fl_match_siempro_validado,

    -- comparaciones
    CASE
        WHEN codprov_declarado = codprov_siempro THEN 1
        ELSE 0
    END AS fl_provincia_ok_siempro,

    CASE
        WHEN codprov_declarado = codprov_apocrifo THEN 1
        ELSE 0
    END AS fl_provincia_ok_apocrifo,

    CASE
        WHEN coddepto_apocrifo IS NOT NULL
         AND coddepto_siempro IS NOT NULL
         AND coddepto_apocrifo = coddepto_siempro
        THEN 1
        ELSE 0
    END AS fl_depto_coincidente

FROM piloto_nominal.piloto_titulares;
```

---

## 6. Matriz de comparación final

```sql
SELECT
    CASE
        WHEN coddepto_apocrifo IS NOT NULL THEN 1 ELSE 0
    END AS apocrifo_match,

    CASE
        WHEN coddepto_siempro IS NOT NULL THEN 1 ELSE 0
    END AS siempro_match,

    COUNT(*) AS cantidad
FROM piloto_nominal.piloto_titulares
GROUP BY 1,2
ORDER BY 1,2;
```

---

## 7. Control de calidad provincial

```sql
SELECT
    COUNT(*) FILTER (
        WHERE codprov_declarado = codprov_siempro
    ) AS provincia_ok,
    COUNT(*) AS total,
    ROUND(
        100.0 * COUNT(*) FILTER (
            WHERE codprov_declarado = codprov_siempro
        ) / COUNT(*),
        2
    ) AS porcentaje_ok
FROM piloto_nominal.piloto_titulares
WHERE coddepto_siempro IS NOT NULL;
```
