# Análisis Integral de Cobertura y Consistencia Geográfica

## Universo consolidado por CUIL -- Esquemas STESS, ALIMENTAR y EDUCACIÓN

Fecha de generación: 2026-02-27

------------------------------------------------------------------------

# 1. Cobertura Geográfica por Esquema

## 1.1 ddbb_alimentar

Total de registros: 11.354.665

Cobertura: - Provincia informada: 6.948.319 - Localidad informada:
6.948.261 - Calle informada: 6.948.242 - Altura informada: 6.904.331 -
Código postal informado: 6.948.286 - Domicilio completo (provincia +
localidad + calle + altura): 6.904.311

Interpretación: El esquema ALIMENTAR presenta alta completitud
territorial en sus tablas principales (titulares y unidades de
convivencia). La diferencia entre calle informada y altura informada es
marginal, lo que indica consistencia estructural en la captura del
domicilio. Es la fuente con mayor aporte efectivo de domicilios
estructurados.

------------------------------------------------------------------------

## 1.2 ddbb_educacion

Total de registros: 1.373.998

Cobertura: - Provincia informada: 35.979 - Municipio/Partido informado:
35.979 - Localidad informada: 35.979 - Calle informada: 35.979 - Altura
informada: 35.973 - Domicilio completo: 35.973

Interpretación: El volumen con información geográfica es
significativamente menor en relación al total del esquema. La cobertura
territorial se concentra exclusivamente en las tablas de becas, lo que
implica que el esquema EDUCACIÓN aporta geografía solo para una fracción
reducida del universo nominal.

------------------------------------------------------------------------

## 1.3 ddbb_stess

Total de registros: 2.584.425

Cobertura: - Provincia informada: 1.037.647 - Municipio informado:
799.422 - Localidad informada: 695.812 - Domicilio (texto libre):
673.282 - Domicilio completo (según regla adaptada a STESS): 570.282

Interpretación: STESS aporta volumen significativo de datos provinciales
y municipales, aunque con menor estructura de domicilio. El campo
domicilio es texto libre y no desagregado en calle/altura, lo que limita
la granularidad analítica respecto de ALIMENTAR.

------------------------------------------------------------------------

# 2. Universo Único por CUIL

Total de CUIL únicos: 8.758.568

## 2.1 Cobertura general

-   CUIL con algún dato geográfico: 7.616.352
-   CUIL con provincia informada: 7.616.352
-   CUIL con municipio informado: 795.581
-   CUIL con localidad informada: 7.377.996
-   CUIL con domicilio estructurado: 6.884.715

Interpretación: El 86,9% del universo único posee al menos provincia
informada. El 78,6% posee localidad. El 78,6% posee domicilio
estructurado. El municipio presenta cobertura significativamente menor,
lo que responde a la heterogeneidad estructural entre esquemas.

------------------------------------------------------------------------

# 3. Consistencia Territorial (Valores Distintos por CUIL)

## 3.1 Provincias distintas por CUIL

-   0 provincias: 1.142.216
-   1 provincia: 7.581.038
-   2 provincias: 35.314

Interpretación: La gran mayoría de los CUIL presentan una única
provincia declarada. El 0,4% presenta dos provincias distintas, lo que
sugiere movilidad o inconsistencias inter-fuente.

------------------------------------------------------------------------

## 3.2 Localidades distintas por CUIL

-   0 localidades: 1.380.572
-   1 localidad: 7.264.968
-   2 localidades: 113.024
-   3 o más: 4

Interpretación: Existe un 1,3% del universo con más de una localidad
asociada. Los casos con 3 o más localidades son marginales.

------------------------------------------------------------------------

## 3.3 Domicilios distintos por CUIL

-   0 domicilios: 1.873.853
-   1 domicilio: 6.873.053
-   2 domicilios: 11.650
-   3 o más: 12

Interpretación: La mayoría de los individuos con información
estructurada presentan un único domicilio. Los casos con múltiples
domicilios son excepcionales y potencialmente vinculados a actualización
temporal o divergencias entre esquemas.

------------------------------------------------------------------------

# 4. Conclusiones Generales

1.  ALIMENTAR es la principal fuente de domicilios estructurados.
2.  STESS aporta volumen provincial y municipal relevante, pero con
    menor estructura.
3.  EDUCACIÓN tiene cobertura territorial limitada al subconjunto de
    becas.
4.  El universo consolidado presenta alta estabilidad territorial: más
    del 98% de los CUIL con provincia informada tienen una única
    provincia asociada.
5.  Las inconsistencias territoriales son marginales en términos
    porcentuales.

Este análisis permite: - Evaluar calidad territorial por esquema. -
Identificar conflictos inter-fuente. - Determinar nivel máximo de
desagregación publicable con respaldo empírico.
