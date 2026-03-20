# TABLA: <nombre_tabla>

## Esquema
<nombre_esquema>

## Tipo de tabla
- [ ] nominal
- [ ] relación
- [ ] serie
- [ ] staging
- [ ] referencia

## Descripción
Qué representa cada fila.

## Granularidad
Unidad de registro:
- persona
- beneficio
- evento
- grupo familiar
- otro:

## Clave primaria (técnica)
- campo/s:
- tipo:
- observaciones:

## Clave operativa (real)
- campo/s:
- nivel de confianza: alto / medio / bajo
- problemas detectados:

## Campos clave
### Identificación
- cuit/cuil:
- dni:
- nombre:
- apellido:

### Otros relevantes
- ...

## Campos para join
| campo | posible destino | calidad |
|------|----------------|--------|
|      |                |        |

## Calidad de datos
- nulos:
- duplicados:
- inconsistencias:
- formatos raros:

## Relaciones
- FK explícitas:
- relaciones inferidas:

## Uso recomendado
Para qué sirve esta tabla:
- [ ] padrón base
- [ ] enriquecimiento
- [ ] validación
- [ ] descartar

## Observaciones
Libre. Acá pensás.

## Queries asociadas
Referencia a queries en `04_queries_base.md` o específicas.

## Pendientes
- [ ] validar clave operativa
- [ ] chequear duplicados
- [ ] evaluar join con ...