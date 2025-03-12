from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.models.xcom import XCom # Importamos Xcom

default_args = {"depends_on_past": True}

# Ejemplo de función
def myfunction(**context): # Es necesario pasar el 'contexto' para acceder a los valores pusheados
    print(int(context["ti"].xcom_pull(task_ids='tarea_2')) - 24)

with DAG(dag_id="9-XCom",
    description="Probando los XCom",
    schedule_interval="@daily",
    start_date=datetime(2022, 1, 1),
	default_args=default_args,
    max_active_runs=1
) as dag:

    t1 = BashOperator(task_id="tarea_1",
					  bash_command="sleep 5 && echo $((3 * 8))") # Se emite un resultado 

    t2 = BashOperator(task_id="tarea_2",
					  bash_command="sleep 3 && echo {{ ti.xcom_pull(task_ids='tarea_1') }}") # Obtiene el resultado de la tarea 1

    t3 = PythonOperator(task_id="tarea_3", 
                        python_callable=myfunction) # Toma el resultado de la tarea anterior (printeará '0' debido a que 24 - 24 = 0)
    
    t1 >> t2 >> t3

