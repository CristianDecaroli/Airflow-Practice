from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(dag_id='bashoperator',
         description='utilizando bash operator',
         start_date=datetime(2025, 3, 11)) as DAG:
    t1 = BashOperator(task_id='hello_with_dag',
                      bash_command='echo "Hello"')