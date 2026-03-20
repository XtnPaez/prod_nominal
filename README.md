# PROD_NOMINAL – Análisis de Esquemas y Datos Nominales

## Propósito

Este repositorio documenta la estructura, calidad y potencial de integración de distintos esquemas de base de datos nominales.

El objetivo es identificar, evaluar y explotar fuentes de datos para construir un padrón único de personas, utilizando CUIT/CUIL como clave principal de cruce.

---

## Cómo leer este repositorio

Orden recomendado:

1. general/overview.md
2. general/claves_transversales.md
3. esquemas/<schema>/<schema>.md
4. esquemas/<schema>/tablas_clave.md
5. esquemas/<schema>/hallazgos.md

---

## Estructura del repositorio

```
/
├── README.md
├── general/
│   ├── overview.md
│   ├── claves_transversales.md
│   ├── patrones_detectados.md
│   ├── riesgos_y_alertas.md
│   └── roadmap_analisis.md
├── glosario/
│   ├── criterios.md
│   ├── tipos_de_tabla.md
│   └── claves_y_joins.md
├── templates/
│   ├── template_esquema.md
│   └── template_tabla.md
├── tools/
│   └── validador_repo.py
└── esquemas/
    ├── ddbb_alimentar/
    │   ├── ddbb_alimentar.md
    │   ├── estructura.md
    │   ├── tablas_clave.md
    │   ├── relaciones.md
    │   ├── queries.md
    │   ├── hallazgos.md
    │   └── pendientes.md
    ├── ddbb_anses/
    ├── ddbb_niñez/
    ├── ddbb_educacion/
    └── ddbb_stess/
```

---

## Esquemas analizados

- esquemas/ddbb_alimentar/ddbb_alimentar.md
- esquemas/ddbb_anses/ddbb_anses.md
- esquemas/ddbb_niñez/ddbb_niñez.md
- esquemas/ddbb_educacion/ddbb_educacion.md
- esquemas/ddbb_stess/ddbb_stess.md

---

## Criterios clave del proyecto

### Clave de integración
- CUIT/CUIL → clave principal (master join)
- DNI → clave secundaria
- Nombre/apellido → validación débil

### Tipos de tablas
- nominal
- relación
- serie
- staging
- referencia

### Separación obligatoria
Cada esquema se documenta separando:
- estructura
- tablas clave
- relaciones
- queries
- hallazgos
- pendientes

---

## Validación de estructura

Ejecutar:

python tools/validador_repo.py .

Modo estricto:

python tools/validador_repo.py . --strict

---

## Convenciones

- Solo existe README.md en la raíz
- Cada esquema tiene un archivo principal con su nombre:
  esquemas/<schema>/<schema>.md
- No usar prefijos numéricos en archivos
- Un archivo = una función

---

## Estado del proyecto

Repositorio en construcción.

Prioridades:
- normalizar análisis por esquema
- identificar claves confiables
- evaluar calidad de datos
- preparar integración hacia padrón único

---

## Uso esperado

Debe permitir responder rápidamente:

- qué esquema aporta personas
- qué tablas son utilizables
- qué claves permiten cruce
- qué calidad tiene cada fuente

Si no responde esas preguntas → la documentación está incompleta.
