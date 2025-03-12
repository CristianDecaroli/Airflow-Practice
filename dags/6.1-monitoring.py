from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

def myfunction():
    raise Exception # levanta un error y corta con error la ejecución de las tasks


with DAG(dag_id='6.1-orquestation',
         description='Monitoreo y prueba de errores en DAG',
         schedule_interval='@daily', # diariamente
         start_date=datetime(2025, 2, 11),
         end_date=datetime(2025, 3, 11)) as dag:
    
    t1 = BashOperator(task_id='tarea1',
                      bash_command="sleep 2 && echo 'primera tarea!'")
    
    t2 = BashOperator(task_id='tarea2',
                      bash_command="sleep 2 && echo 'segunda tarea!") # va a fallar porque le falta una comilla
     
    t3 = BashOperator(task_id='tarea3',
                      bash_command="sleep 2 && echo 'tercera tarea!'")
    
    t4 = PythonOperator(task_id='tarea4',
                        python_callable=myfunction) # dará error

    t5 = BashOperator(task_id='tarea5',
                      bash_command="sleep 2 && echo 'cuarta tarea!'")
    
    t1 >> t2 >> t3 >> t4 >> t5