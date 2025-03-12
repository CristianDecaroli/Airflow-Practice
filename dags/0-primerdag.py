from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

with DAG('primerdag',
         description='Nuestro primer dag',
         start_date=datetime(2025, 3, 11),
         schedule_interval='@once') as dag:
    
    t1 = EmptyOperator(task_id="dummy")