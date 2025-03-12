from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

with DAG(dag_id='5.2-orquestation',
         description='Probando orquestacion',
         schedule_interval='0 7 * * 1', # CRON -> Todos los Lunes a las 7am
         start_date=datetime(2025, 2, 11),
         end_date=datetime(2025, 3, 11)) as dag:
    
    t1 = EmptyOperator(task_id='tarea1')
    
    t2 = EmptyOperator(task_id='tarea2')
    
    t3 = EmptyOperator(task_id='tarea3')
    
    t4 = EmptyOperator(task_id='tarea4')
    
    t1 >> t2 >> [t3, t4]