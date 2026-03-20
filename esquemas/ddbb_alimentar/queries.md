# Queries sugeridas — ddbb_alimentar

## 1. Duplicados por CUIL de titular

```sql
SELECT cuiltitular, COUNT(*) AS cantidad
FROM ddbb_alimentar.titulares
GROUP BY cuiltitular
HAVING COUNT(*) > 1;
```

## 2. Titulares sin CUIL o DNI

```sql
SELECT *
FROM ddbb_alimentar.titulares
WHERE cuiltitular IS NULL
   OR ndoctitular IS NULL;
```

## 3. Menores sin vínculo a titular

```sql
SELECT *
FROM ddbb_alimentar.menores
WHERE cuiltitular IS NULL;
```

## 4. Cantidad de menores por titular

```sql
SELECT cuiltitular, COUNT(*) AS cantidad_menores
FROM ddbb_alimentar.menores
GROUP BY cuiltitular
ORDER BY cantidad_menores DESC;
```

## 5. Calidad geográfica básica de titulares

```sql
SELECT *
FROM ddbb_alimentar.titulares
WHERE provincia IS NULL
   OR localidad IS NULL
   OR calle IS NULL
   OR numero IS NULL;
```

## 6. Cruce de pagos con titulares

```sql
SELECT t.cuiltitular, t.provincia, t.localidad, p.periodo, p.importe
FROM ddbb_alimentar.titulares t
JOIN ddbb_alimentar.pa_pagados p
  ON t.cuiltitular = p.cuil;
```

## 7. Cobertura de dirección completa

```sql
SELECT COUNT(*) AS total,
       COUNT(*) FILTER (WHERE calle IS NOT NULL AND numero IS NOT NULL) AS con_direccion_minima,
       COUNT(*) FILTER (WHERE provincia IS NOT NULL AND localidad IS NOT NULL) AS con_admin_minima
FROM ddbb_alimentar.titulares;
```

## 8. Homogeneidad de formato de identificadores

```sql
SELECT 'titulares' AS tabla, COUNT(*) AS total, COUNT(*) FILTER (WHERE cuiltitular IS NULL) AS cuil_null
FROM ddbb_alimentar.titulares
UNION ALL
SELECT 'menores', COUNT(*), COUNT(*) FILTER (WHERE cuilmenor IS NULL)
FROM ddbb_alimentar.menores;
```
