from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(dag_id='5.1-orquestation',
         description='Probando orquestacion',
         schedule_interval='@daily',
         start_date=datetime(2025, 1, 11),
         end_date=datetime(2025, 3, 11),
         default_args={'depende_on_past': True},
         max_active_runs=1) as dag:
    
    t1 = BashOperator(task_id='tarea1',
                      bash_command="sleep 2 && echo 'Tarea1'")
    
    t2 = BashOperator(task_id='tarea2',
                      bash_command="sleep 2 && echo 'Tarea2'")
    
    t3 = BashOperator(task_id='tarea3',
                      bash_command="sleep 2 && echo 'Tarea3'")
    
    t4 = BashOperator(task_id='tarea4',
                      bash_command="sleep 2 && echo 'Tarea4'")
    
    t1 >> t2 >> [t3, t4]