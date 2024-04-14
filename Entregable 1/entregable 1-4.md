# Entregable 1 del proyecto

## 5. Diseño Conceptual

### 1. Almacén Central

### 2. Corte

![Corte ER](Diagramas-ER/Corte_ER.png)

### 3. Confección

### 4. Almacén de Tránsito

### 5. Acabados

![Acabados ER](Diagramas-ER/acabados_ER.png)

#### Diccionario de datos: 

**Entidad:	Empleado**

**Semántica:	Personas de la empresa que trabajan en los procesos del mismo.**

| **Atributo** | **Naturaleza** | **Formato** | **Valores válidos** | **Unidad** | **Derivada de** | **Semántica** | **Ontología** |
|--------------|----------------|-------------|---------------------|------------|-----------------|---------------|---------------|
| dni          | int            | 99999999    | 8 dígitos           |            |                 | Número de identificación único de la persona en el sistema | Identificador principal de la persona en la empresa |
| nombre       | char           | xxxxxxxxx   | Cadena              |            |                 | Nombre Completo del cliente | Nombre del trabajador en el negocio |
| telefono     | int            | 99999999999| 10 dígitos          |            |                 | Número de teléfono de contacto de la persona | Número de teléfono asociado a la persona en la empresa |
| fechaNac     | date           | DD/MM/AAAA | calendario          |            |                 | Fecha de nacimiento de una persona | Fecha de nacimiento de la persona que es empleado en la empresa |
| cargo        | char           | xxxxxxxxxxx| Cadena              |            |                 | Cargo actual de la persona en la empresa |  |

**Entidad:	Área**

**Semántica:	Unidad de negocio con procesos para un objetivo en específico**

| **Atributo** | **Naturaleza** | **Formato** | **Valores válidos** | **Unidad** | **Derivada de** | **Semántica** | **Ontología** |
|--------------|----------------|-------------|---------------------|------------|-----------------|---------------|---------------|
| IdArea       | int            | XXX999      | Cadena y números    |            |                 | Número de identificación único de área en el sistema | Identificador principal del área en la empresa |
| nombre       | char           | xxxxxxxx    | Cadena              |            |                 | Nombre del área | Nombre del área en el negocio |

**Entidad:	Reporte**

**Semántica:	Representa los registros completos del área en forma de listas con lotes, prendas, cajas y fechas en la que se hizo un proceso de acabado.**

| **Atributo** | **Naturaleza** | **Formato** | **Valores válidos** | **Unidad** | **Derivada de** | **Semántica** | **Ontología** |
|--------------|----------------|-------------|---------------------|------------|-----------------|---------------|---------------|
| IdReporte    | int            | XXX999      | Cadena y números    |            |                 | Número del reporte de área de acabados en el sistema | Identificador principal del reporte del área en la empresa |
| TipoReporte  | char           | xxxxxxxxx   | Cadena              |            |                 | Nombre del reporte | Nombre de los tipos del área de acabados |
| FechaInicio  | date           | DD/MM/AAAA  | calendario          |            |                 | Fecha de inicio del periodo para mostrar el reporte | Parámetro de inicio de registro en el reporte |
| FechaFinal   | date           | DD/MM/AAAA  | calendario          |            |                 | Fecha de final del periodo para mostrar el reporte | Parámetro de final de registro en el reporte |

**Entidad:	Acabados**

**Semántica:	Procesos internos del área en la cual el operario del área se encarga de terminar y terminar los lotes de prendas.**

| **Atributo** | **Naturaleza** | **Formato** | **Valores válidos** | **Unidad** | **Derivada de** | **Semántica** | **Ontología** |
|--------------|----------------|-------------|---------------------|------------|-----------------|---------------|---------------|
| IdAcabado    | int            | XXX999      | Cadena y números    |            |                 | Número de Id del proceso interno de acabados | Identificador principal del de los proceso de acabados |
| TipoAcabado  | char           | xxxxxxxxx   | Cadena              |            |                 | Nombre del proceso de acabado | Nombre del proceso de acabados |
| Estado       | booleano       | true - false| true - false        |            |                 | Estado de cada proceso interno del área de acabados | Parámetro que permitirá avanzar por cada proceso de acabado en secuencia. |

**Entidad:	Prenda**

**Semántica:	unidad mínima del sistema, producto final del área de confección y elemento de los lotes de prendas.**

| **Atributo** | **Naturaleza** | **Formato** | **Valores válidos** | **Unidad** | **Derivada de** | **Semántica** | **Ontología** |
|--------------|----------------|-------------|---------------------|------------|-----------------|---------------|---------------|
| IdPrenda     | int            | XXX999999   | Cadena y números    |            |                 | Identificador de prenda de ropa | Identificador de prenda de ropa en el sistema |
| nombre       | char           | xxxxxxxxx   | Cadena              |            |                 | Nombre de la prenda asignada | Nombre de prendas del negocio |
| TipoPrenda   | char           | xxxxxxxxx   | Cadena              |            |                 | Tipo de prenda según la clasificación en el sistema | Tipo de prendas registradas en el negocio |

**Entidad:	Caja**

**Semántica:	Agrupación de prendas según su tipo o entrega previa.**

| **Atributo** | **Naturaleza** | **Formato** | **Valores válidos** | **Unidad** | **Derivada de** | **Semántica** | **Ontología** |
|--------------|----------------|-------------|---------------------|------------|-----------------|---------------|---------------|
| IdCaja       | int            | XXX999999   | Cadena y números    |            |                 | Identificador de caja como conjunto de prendas | Identificador de prenda de ropa en el sistema |
| capacidad    | int            | 99999999    | 8 dígitos           |            |                 | Capacidad máxima de caja | Capacidad máxima en la cual se puede llenar de prendas |






### 6. Inspeccion de Calidad

![Inspeccion_calidad ER](Diagramas-ER/inspeccion_calidad_ER.png)

### 7. PCP



**[Regresar al índice](../README.md)**

