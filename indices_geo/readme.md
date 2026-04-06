# indices_geo — Índices operativos

## Propósito

Definir los índices necesarios para optimizar:

* joins por código postal
* joins por provincia
* agregaciones por departamento

El foco es exclusivamente el flujo geo.

---

## Alcance

Se aplican sobre:

* tablas de `geo_ref`
* tablas de `geo_work`

No se indexan tablas fuente originales salvo necesidad explícita.

---

## Estrategia

### Claves principales

* cp
* codprov
* coddepto
* cuil

---

### Índices compuestos

* (cp, codprov_ref)
* (coddepto_ref)
* (cuil)

---

## Regla

Indexar solo lo necesario para:

* join territorial
* agregación final

Evitar sobreindexar.

---

## Uso

Los índices se crean una vez cargadas las tablas base y antes de ejecutar joins masivos.
