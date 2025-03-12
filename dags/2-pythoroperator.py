from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello():
    print('hello gente de platzi')

with DAG('python_operator',
         description='DAG con Python Operator',
         schedule_interval='@once',
         start_date=datetime(2025, 3, 11)) as DAG:
    t1 = PythonOperator(task_id='hello_with_python',
                        python_callable=hello)