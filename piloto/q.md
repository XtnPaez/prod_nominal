# Q — Queries del piloto

## 2. Join con tabla SIEMPRO

```sql id="q02001"
WITH cp_unico AS (
    SELECT
        cp,
        codprov_ign,
        MIN(coddepto_ign) AS coddepto_ign
    FROM unidades_geoestadisticas.codigos_postales_2026_siempro
    WHERE cp IS NOT NULL
      AND codprov_ign IS NOT NULL
      AND coddepto_ign IS NOT NULL
    GROUP BY cp, codprov_ign
    HAVING COUNT(DISTINCT coddepto_ign) = 1
)
UPDATE piloto_nominal.bbdd_anses a
SET
    codprov_ign = u.codprov_ign,
    coddepto_ign = u.coddepto_ign,
    cp_match = u.cp,
    fl_match_cp = 1,
    fl_match_validado = 1,
    updated_at = now()
FROM cp_unico u
WHERE a.cp = u.cp
  AND a.codprov_anses_ign = u.codprov_ign;
```

---

## 3. Match validado

```sql id="q02002"
SELECT
    COUNT(*) AS cantidad_match_validado,
    ROUND(
        100.0 * COUNT(*) / (SELECT COUNT(*) FROM piloto_nominal.bbdd_anses),
        2
    ) AS porcentaje_sobre_total
FROM piloto_nominal.bbdd_anses
WHERE coddepto_ign IS NOT NULL;
```

---

## 4. Cobertura de asignación de departamento

```sql id="q02003"
SELECT
    COUNT(*) AS total,
    COUNT(*) FILTER (
        WHERE cp IS NOT NULL
          AND codprov_anses_ign IS NOT NULL
    ) AS candidatos,
    COUNT(*) FILTER (
        WHERE coddepto_ign IS NOT NULL
    ) AS con_depto,
    ROUND(
        100.0 * COUNT(*) FILTER (
            WHERE coddepto_ign IS NOT NULL
        ) / COUNT(*),
        2
    ) AS pct_sobre_total,
    ROUND(
        100.0 * COUNT(*) FILTER (
            WHERE coddepto_ign IS NOT NULL
        ) / NULLIF(
            COUNT(*) FILTER (
                WHERE cp IS NOT NULL
                  AND codprov_anses_ign IS NOT NULL
            ),
            0
        ),
        2
    ) AS pct_sobre_candidatos
FROM piloto_nominal.bbdd_anses;
```
