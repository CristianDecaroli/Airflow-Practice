# **Práctica de Airflow**
Para esta práctica, Airflow se ejecutará en un [docker-compose.yml](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html) que se encargará de inicializar toda la arquitectura de la herramienta.

**This file contains several service definitions:**

- `airflow-scheduler `- The scheduler monitors all tasks and DAGs, then triggers the task instances once their dependencies are complete.

- `airflow-webserver` - The webserver is available at http://localhost:8080.

- `airflow-worker` - The worker that executes the tasks given by the scheduler.

- `airflow-triggerer` - The triggerer runs an event loop for deferrable tasks.

- `airflow-init` - The initialization service.

- `postgres` - The database.

- `redis` - The redis - broker that forwards messages from scheduler to worke

---

Airflow tiene un archivo llamado `airflow.cfg` que tiene varias secciones relacionadas a funcionalidades de la herramienta. 
También, si utilizamos `docker-compose`, se pueden realizar las configuraciones necesarias desde este archivo.

Para saber más acerca de qué podemos modificar o agregar al funcionamiento de Airlow, podemos ir a la [documentación oficial acerca de la configuración](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html).

---

En Airflow, se pueden guardar [variables de entornos](https://airflow.apache.org/docs/apache-airflow/stable/howto/variable.html) desde la interfaz en `Admin/variable`. Al crearlas, se le asigna un valor. Luego se pueden importar en el código principal del dag, de esta manera:
```py
from airflow.models import Variable
```
De esta manera podemos utilizar variables de entorno.

---

Desde la interfaz de Amazon, también se pueden crear [connections](https://airflow.apache.org/docs/apache-airflow/1.10.9/howto/connection/index.html). Ejemplo, podriamos crear una conexión de PotgreSQL. La manera de utilizarlas es importarla utilizando el nombre de la conexión.
```py
from airflow.providers.postgres.operators.postgres import PostgresOperator
```

---

Para contruir `dags` hay varias maneras:
- **Standar contructors**
- **@dag Decorator**
- **Context Manager**

Generalmente se utiliza esta última. Es la utilizaré en esta práctica. (se usará en los dags)

---

Para definir dependencias entre tareas hay dos opciones:

- **downstream** y **upstream**
- **bitshift operators** esta última es la más empleada. (se usará en los dags)

---

Además de los operadores predeterminados, podemos crear [custom operators](https://airflow.apache.org/docs/apache-airflow/stable/howto/custom-operator.html#creating-a-custom-operator), que son nada más y nada menos que operadores personalizados que podremos utilizar.

---

`Orquestación`:

A veces se suele usar CRON para setear fechas y horas:

```plaintext
+------------------------------+
|       Formato de CRON        |
+------------------------------+
* * * * *
| | | | |
| | | | +---- Día de la semana (0-6, 0=Domingo)
| | | +------ Mes (1-12)
| | +-------- Día del mes (1-31)
| +---------- Hora (0-23)
+------------ Minuto (0-59)
```

---

**Posibles Fallos:**
- La API a la que queremos acceder está caída, no responde adecuadamente.
- Error de lógica en el código.
- Algún proceso del que dependemos se ejecutó incorrectamente.
- Se ha borrado una tabla de una base de datos.
- Un sesor llegó al timeout (esto se puede configurar)

---

**Trigger Rules**

Airflow tiene configurado por defecto un trigger rules llamado `all_success`.

En Apache Airflow, las **Trigger Rules** determinan cuándo una tarea debe ejecutarse en función del estado de las tareas anteriores en el DAG (Directed Acyclic Graph). Por defecto, una tarea en Airflow se ejecuta cuando **todas sus tareas upstream (anteriores) han sido exitosas** (`all_success`), pero se pueden cambiar según el caso.

---

**Principales Trigger Rules en Airflow**

1. `all_success` (por defecto)

   📌 Se ejecuta solo si **todas** las tareas upstream han sido exitosas.  
   ✅ Ejemplo: Ideal para tareas que dependen de la finalización exitosa de todas las tareas anteriores.  

2. `all_failed` 

   📌 Se ejecuta solo si **todas** las tareas upstream han fallado.  
   ✅ Ejemplo: Útil para manejar errores, como enviar alertas cuando todas las tareas previas fallan.  

3. `all_done`

   📌 Se ejecuta cuando **todas** las tareas upstream han finalizado, sin importar si fueron exitosas o fallidas.  
   ✅ Ejemplo: Para tareas de limpieza o notificaciones al final del flujo.  

4. `one_success`

   📌 Se ejecuta si **al menos una** tarea upstream fue exitosa.  
   ✅ Ejemplo: Útil en escenarios donde hay múltiples fuentes de datos y basta con que una funcione.  

5. `one_failed`

   📌 Se ejecuta si **al menos una** tarea upstream ha fallado.  
   ✅ Ejemplo: Puede activarse para registrar logs o realizar compensaciones cuando una de varias tareas falla.  

6. `none_failed`

   📌 Se ejecuta si **ninguna** tarea upstream ha fallado (puede incluir tareas exitosas o en estado skipped).  
   ✅ Ejemplo: Para flujos donde solo se quiere ejecutar si todo ha ido bien o ha sido omitido.  

7. `none_failed_or_skipped`

   📌 Se ejecuta si **ninguna** tarea upstream ha fallado o ha sido saltada (`skipped`).  
   ✅ Ejemplo: Para asegurar que todas las tareas anteriores realmente se ejecutaron y fueron exitosas.  

8. `none_skipped`

   📌 Se ejecuta si **ninguna** tarea upstream fue `skipped`.  
   ✅ Ejemplo: Puede ser útil cuando quieres garantizar que todas las tareas anteriores **intentaron ejecutarse**.  

9. `dummy`

   📌 Se ejecuta **siempre**, sin importar el estado de las tareas anteriores.  
   ✅ Ejemplo: Puede ser útil para pruebas o cuando necesitas un placeholder en el DAG.  

---

**Sensores**

Los sensores son un tipo especial de operador diseñado para esperar a que algo ocurra, desde eventos basados en el tiempo, archivos en una carpeta o eventos externos, como la finalización de otro DAG.

- airflow.sensors.bash
- airflow.sensors.date_time
- airflow.sensors.external_task
- airflow.sensors.filesystem
- airflow.sensors.python
- airflow.sensors.time_delta
- airflow.sensors.time_sensor
- airflow.sensors.weekday
- airflow.sensors.base

---

**Jinja Templates**

Los [templates con Jinja](https://airflow.apache.org/docs/apache-airflow/stable/templates-ref.html) son un mecanismo que permite generar contenido dinámico en aplicaciones y scripts utilizando el motor de plantillas Jinja2. Jinja2 es un motor de plantillas para Python ampliamente utilizado en herramientas como Flask, Django, y también en frameworks como Apache Airflow para crear configuraciones y comandos dinámicos.

Conceptos básicos:
Un template es un archivo (generalmente texto o HTML) con marcadores de posición que pueden ser reemplazados dinámicamente por valores. Jinja2 permite utilizar variables, control de flujo (bucles y condicionales), y filtros para construir plantillas complejas.

---

**Xcoms**

Permite enviar y recibir un valor obtenido por una tarea hacia otra. No está diseñado para pushear, pullear gran cantidad de datos. Más bien está diseñado para pequeños valores.

---

**Python Branch Operator**

El operador BranchPythonOperator en Apache Airflow permite la creación de flujos de trabajo dinámicos al seleccionar la rama de ejecución en función de una condición evaluada en tiempo de ejecución. Es ideal cuando necesitas tomar decisiones basadas en datos o lógica dentro de un DAG.