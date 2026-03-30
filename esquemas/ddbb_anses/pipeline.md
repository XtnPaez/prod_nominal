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

* la tabla no tiene dirección (sin calle ni número)
* el cruce territorial dependerá de `provincia_cd` + `codigo_postal_nu`

---

## Tabla territorial de referencia

### Fuente

* `unidades_geoestadisticas.codigos_postales_2026_siempro`

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

El cruce se hará usando:

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

### Solo lectura

* `ddbb_anses`
* `unidades_geoestadisticas`

### Escritura requerida

* esquema de trabajo auxiliar fuera de `prod_nominal`

---

## Restricción operativa

En `prod_nominal` solo hay permisos de **SELECT**.

Por lo tanto, el pipeline requiere una etapa manual/intermedia:

1. extraer desde `prod_nominal`:

   * subconjunto de ANSES con:

     * `cuil_cuit_nu`
     * `provincia_cd`
     * `localidad_tx`
     * `codigo_postal_nu`

2. llevar esos datos a un esquema/entorno con permisos de escritura

3. ejecutar allí el cruce territorial

4. obtener tabla resultado con:

   * `cuil_cuit_nu`
   * `codprov`
   * `coddepto`
   * `departamento`

---

## Tabla resultado esperada

Nombre sugerido:

* `piloto_nominal.anses_departamentos`
* o equivalente en esquema de trabajo

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
* base lista para producir el primer indicador territorial de ANSES

---

## Próximo paso

1. extraer universo base ANSES
2. medir completitud de:

   * `provincia_cd`
   * `codigo_postal_nu`
3. correr cruce territorial
4. medir cobertura efectiva
5. generar agregado final por departamento
