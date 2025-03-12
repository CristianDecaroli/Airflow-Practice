from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

with DAG(dag_id='5.3-orquestation',
         description='Probando orquestacion',
         schedule_interval='@monthly', # mensualmente
         start_date=datetime(2025, 1, 11),
         end_date=datetime(2025, 3, 11)) as dag:
    
    t1 = EmptyOperator(task_id='tarea1')
    
    t2 = EmptyOperator(task_id='tarea2')
    
    t3 = EmptyOperator(task_id='tarea3')
    
    t4 = EmptyOperator(task_id='tarea4')
    
    t1 >> t2 >> [t3, t4]