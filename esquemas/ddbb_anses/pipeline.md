# ddbb_anses — pipeline

## Objetivo

Asignar **departamento** a los CUIL/CUIT de la base ANSES para construir el primer entregable operativo:

> **cantidad de CUIL por departamento**

---

## Tabla de trabajo principal

### Origen nominal

* `ddbb_anses.anses`

### Campos relevantes

* `cuil_cuit_nu` → identificador nominal
* `provincia_cd` → provincia codificada
* `localidad_tx` → localidad declarada
* `codigo_postal_nu` → código postal declarado

### Nivel máximo alcanzable

* **departamento**

Observación:

* la tabla no tiene dirección
* el cruce territorial dependerá de `provincia_cd` + `codigo_postal_nu`

---

## Diagnóstico preliminar

Resultados observados sobre `ddbb_anses.anses`:

* total de registros: **11.283.777**
* códigos postales distintos: **1.752**
* distribución de CP consistente con geografía real
* ejemplos de CP frecuentes:

  * `2000`
  * `1900`
  * `7600`
  * `8000`
  * `4400`

Lectura:

* el campo `codigo_postal_nu` es usable
* `provincia_cd` ya viene codificada
* ANSES es una base apta para asignación territorial a nivel departamento

---

## Tabla territorial de referencia

### Fuente esperada

* `unidades_geoestadisticas.codigos_postales_2026_siempro`

### Origen

Repositorio:

* `cod_pos_AR`

### Estado

* codificada contra provincias
* codificada contra departamentos
* pendiente localidad

### Campos relevantes

* `cp`
* `codprov_ign`
* `provincia_ign`
* `coddepto_ign`
* `departamento_ign`

### Rol

* tabla puente para asignar departamento a partir de código postal
* validación territorial restringida por provincia

---

## Lógica del cruce

Condición principal:

* `ddbb_anses.anses.codigo_postal_nu = unidades_geoestadisticas.codigos_postales_2026_siempro.cp`
* `ddbb_anses.anses.provincia_cd = unidades_geoestadisticas.codigos_postales_2026_siempro.codprov_ign`

Secuencia:

1. tomar CUIL/CUIT desde `ddbb_anses.anses`
2. tomar provincia codificada (`provincia_cd`)
3. tomar código postal (`codigo_postal_nu`)
4. cruzar contra `codigos_postales_2026_siempro`
5. asignar:

   * `coddepto_ign`
   * `departamento_ign`
6. construir tabla resultado para agregación final

---

## Esquemas involucrados

### Lectura

* `ddbb_anses`

### Escritura requerida

* `prod_nominal`
* `unidades_geoestadisticas`

---

## Dependencias operativas

### 1. Permisos de escritura

El pipeline **no puede ejecutarse todavía en el servidor** porque aún no están disponibles los permisos de escritura necesarios.

### 2. Tabla territorial faltante

Antes de correr el cruce, hay que subir a `prod_nominal` la tabla:

* `cod_pos_AR` ya trabajada y normalizada
* nombre esperado en servidor:

  * `unidades_geoestadisticas.codigos_postales_2026_siempro`

---

## Alerta

> **Estado actual: bloqueado por permisos de escritura y carga de tabla territorial**
>
> El diseño del pipeline está definido y ANSES ya fue diagnosticada como base apta para el cruce.
> La ejecución queda pendiente hasta:
>
> 1. obtener permisos de escritura en el servidor
> 2. cargar `codigos_postales_2026_siempro` en `unidades_geoestadisticas`

---

## Tabla resultado esperada

Nombre sugerido:

* `ddbb_anses.anses_departamentos`
* o equivalente dentro de esquema de trabajo en `prod_nominal`

Campos mínimos:

* `cuil_cuit_nu`
* `provincia_cd`
* `codigo_postal_nu`
* `coddepto_ign`
* `departamento_ign`

Campos recomendados:

* `fl_match_cp`
* `fl_match_validado`
* `created_at`

---

## Criterio de validación

Un caso se considerará válido cuando:

* exista match por código postal
* la provincia de ANSES coincida con la provincia de la tabla territorial

Condición lógica:

* `codigo_postal_nu = cp`
* `provincia_cd = codprov_ign`

---

## Producto final

Con la tabla ya enriquecida se generará:

* cantidad de CUIL/CUIT por departamento

Agregación esperada:

* `GROUP BY coddepto_ign, departamento_ign`

---

## Resultado esperado del pipeline

* tabla nominal enriquecida con departamento
* cobertura medible del cruce
* primer indicador territorial operativo para ANSES

---

## Próximo paso

1. obtener permisos de escritura
2. cargar `codigos_postales_2026_siempro`
3. ejecutar cruce territorial
4. medir cobertura efectiva
5. generar agregado final por departamento
