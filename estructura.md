[Volver a Readme](https://asimov.cncps.gob.ar/cpaez/prod_nominal/src/master/README.md)

# Informe de Estructura de Base de Datos  
**Unidad de análisis: PERSONA (CUIL)**

---

## Esquema ddbb_stess

### ref_sexo
Tabla de referencia.

Campos:
- codigo (varchar(1)) PK
- descripcion (varchar(15))

---

### ref_tipo_doc
Tabla de referencia.

Campos:
- codigo (varchar(2)) PK
- descripcion (varchar(20))

---

### ref_tipo_liquidacion
Tabla de referencia.

Campos:
- codigo (varchar(2)) PK
- descripcion (varchar(50))

---

### ref_liqui_plan
Tabla de referencia.

Campos:
- codigo (varchar(3)) PK
- descripcion (varchar(100))

---

### ref_provincia
Tabla de referencia.

Campos:
- codigo (varchar(2)) PK
- descripcion (varchar(50))

---

### stess_202509
Tabla transaccional de liquidaciones.

Campos:
- id (bigserial) PK
- cuil (varchar(11))
- apellido_y_nombre (varchar(25))
- tipo_doc (varchar(2))
- nro_doc (varchar(8))
- fecha_nacimiento (date)
- sexo (varchar(1))
- importe_total (numeric(10,2))
- provincia_cod (varchar(2))
- provincia_desc (varchar(15))
- municipio_desc (varchar(15))
- localidad_desc (varchar(15))
- domicilio (varchar(30))
- createdat (timestamptz)
- updatedat (timestamptz)

Observaciones:
- Una persona puede aparecer múltiples veces.
- CUIL no es único.

---

### padron_stess
Tabla de consolidación lógica por persona.

Campos:
- cuil (varchar(11))
- apellido_y_nombre (varchar(25))
- programas (text)
- tablas (text)

---

## Esquema ddbb_alimentar

### titulares
Personas adultas titulares.

Campos:
- id (bigserial) PK
- cuiltitular (numeric)
- ndoctitular (varchar(15))
- fechanactitular (date)
- sexotitular (char(1))
- provincia (varchar(50))
- localidad (varchar(100))
- cod_postal (varchar(10))
- calle (varchar(100))
- numero (varchar(20))
- piso (varchar(10))
- depto (varchar(10))
- monto (numeric(10,2))
- createdat (timestamptz)
- updatedat (timestamptz)

---

### menores
Personas menores asociadas a titulares.

Campos:
- id (bigserial) PK
- cuilmenor (varchar(15))
- ndocmenor (varchar(15))
- apellidoynombre (varchar(50))
- fechadenacimiento (date)
- sexo (char(1))
- cuiltitular (numeric)

---

### unidades_convivencia
Tabla derivada y denormalizada.

Campos:
- id (bigserial) PK
- cuil_titular (numeric)
- sexo_titular (char(1))
- edad_titular (int8)
- provincia (varchar(50))
- localidad (varchar(100))
- cod_postal (char(10))
- calle (varchar(100))
- numero (varchar(20))
- piso (varchar(10))
- depto (varchar(10))
- monto (numeric(10,2))
- cuil_menor (numeric)
- nombre_menor (varchar(100))
- sexo_menor (char(1))
- edad_menor (int8)

Observaciones:
- No es tabla fuente.
- Reproduce información de titulares y menores.

---

## Esquema ddbb_educacion

### vouchers_aprobados
Relación persona–institución.

Campos:
- id (bigserial) PK
- cuit (varchar(11))
- cue (varchar(10))
- nivel_educativo (varchar(2))
- createdat (timestamptz)
- updatedat (timestamptz)

Restricción única:
- (cuit, cue)

---

### vouchers_datos_nominales
Relación adulto–menor.

Campos:
- id (bigserial) PK
- cuil_adulto (varchar(11))
- cuil_menor (varchar(11))
- ape_nom_adulto (varchar(100))
- ape_nom_menor (varchar(100))
- createdat (timestamptz)
- updatedat (timestamptz)

Restricción única:
- (cuil_adulto, cuil_menor)

---

## Conclusiones
- El CUIL es la clave transversal del sistema.
- Existen tablas fuente de personas, tablas de eventos y tablas de relación.
- Un registro único debe construirse consolidando por CUIL con reglas de prioridad.
