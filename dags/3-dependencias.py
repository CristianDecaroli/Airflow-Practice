from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

def hello():
    print('hello gente de platzi')

with DAG('dependencias',
         description='Creando dependencias entre tareas',
         schedule_interval='@once',
         start_date=datetime(2025, 3, 11)) as DAG:
    
    t1 = PythonOperator(task_id='tarea1',
                        python_callable=hello)
    
    t2= BashOperator(task_id='tarea2',
                     bash_command="echo 'tarea2'")
    
    t3= BashOperator(task_id='tarea3',
                     bash_command="echo 'tarea3'")
    
    t4= BashOperator(task_id='tarea4',
                     bash_command="echo 'tarea4'")
    
    t1 >> t2 >> [t3, t4] # t3, y t4 corren en paralelo