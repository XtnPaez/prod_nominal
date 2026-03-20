# Instrucciones del proyecto

## Rol del analista

El analista actúa como especialista en geografía de datos nominales.

Su tarea es:

- detectar campos geográficos
- evaluar su calidad estructural
- determinar si están codificados
- establecer si se puede vincular una dirección a CUIL/CUIT
- identificar tablas útiles para normalización y geocodificación

No es objetivo principal de este proyecto:

- agotar el análisis funcional de cada base
- documentar en profundidad prestaciones sin relevancia geográfica
- modelar relaciones personales salvo cuando impacten en domicilio compartido

## Principio rector

Toda tabla debe responder, directa o indirectamente, a alguna de estas preguntas:

- ¿hay geografía?
- ¿qué geografía hay?
- ¿sirve para geocodificar?
- ¿está asociada a un CUIL/CUIT?
- ¿permite una o varias direcciones por persona?

## Reglas de documentación

1. Solo existe un README.md en la raíz.
2. No se usan carpetas numeradas.
3. Cada esquema tiene su propia carpeta en `esquemas/<schema>/`.
4. Cada esquema debe tener archivos separados por función.
5. Cada tabla analizada debe seguir la plantilla de tabla geográfica.
6. Las fuentes oficiales se documentan por separado, fuera de los esquemas.

## Documentos obligatorios por esquema

- `<schema>.md`
- `inventario_geo.md`
- `tablas_prioritarias.md`
- `codificacion.md`
- `cuil_domicilio.md`
- `hallazgos.md`
- `pendientes.md`

## Criterios de evaluación geográfica

### Geografía presente

- sí
- no

### Codificación

- codificada
- parcialmente codificada
- no codificada

### Vinculación nominal

- por CUIL/CUIT
- por DNI
- por nombre
- sin clave nominal utilizable

### Resolución de domicilio por CUIL/CUIT

- una dirección probable
- múltiples direcciones posibles
- solo localización aproximada
- no resoluble

### Potencial geo

- alto
- medio
- bajo
- nulo

## Criterio operativo

Se priorizan las tablas que cumplan al menos una de estas condiciones:

- tienen dirección o semidirección
- tienen códigos geográficos
- tienen coordenadas
- permiten asociar ubicación a CUIL/CUIT
- permiten reconstruir histórico de domicilios

## Regla final

Una tabla puede ser importante para la base y aun así no ser prioritaria para este proyecto.
Aquí importa primero su valor geográfico.
