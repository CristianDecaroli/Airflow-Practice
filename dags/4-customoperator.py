from airflow import DAG
from datetime import datetime
from hellooperator import HelloOperator # creado en el archivo 4.1

with DAG(
    dag_id = 'customoperator',
    description='Creando un custom operator',
    start_date=datetime(2025, 3, 11)
    ) as dag:

    t1 = HelloOperator(task_id='hello',
                       name='cristian')