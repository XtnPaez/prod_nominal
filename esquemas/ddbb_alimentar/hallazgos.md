# Hallazgos — ddbb_alimentar

## Hallazgos clave

- `titulares` es la mejor puerta de entrada al modelo PERSONA dentro del esquema.
- `menores` complementa identidad, pero depende estructuralmente del vínculo con el titular.
- `unidades_convivencia` es analíticamente muy valiosa para derivar hogares, aunque esté mal normalizada.
- `pa_pagados` aporta la capa de evento/prestación de forma clara y explotable.
- las tablas `_serie` permiten reconstrucción longitudinal y enriquecen atributos nominales.

## Problemas estructurales

- mismos identificadores representados con tipos distintos según tabla
- falta de claves foráneas explícitas
- geografía sin codificación normalizada
- domicilio en texto libre
- ausencia parcial de nombre/apellido en la tabla más importante (`titulares`)

## Oportunidades de integración

- unificar `titulares` + `titulares_serie` para padrón actual + histórico
- unificar `menores` + `menores_serie` con estrategia equivalente
- derivar tabla de relaciones `titular_menor`
- derivar entidad `hogar` a partir de `unidades_convivencia`
- priorizar pipeline de normalización geográfica sobre titulares y unidades de convivencia

## Relevancia geográfica

Este esquema sí sirve para geolocalizar personas.

No sirve perfecto, claro. Tampoco pretendamos que venga con coordenadas y café. Pero tiene lo suficiente para una estrategia robusta:

- provincia
- localidad
- código postal
- calle
- número
- piso/depto

La geolocalización potencial es alta en titulares y unidades de convivencia, baja en menores y nula en pagos.

## Regla metodológica emergente del piloto

Para el resto de los esquemas conviene separar siempre:

1. tabla fuente de identidad principal
2. tabla fuente de relaciones
3. tabla fuente de eventos
4. tabla fuente geográfica

En Alimentar, esas piezas ya aparecen bastante visibles.
