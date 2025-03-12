from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime


with DAG(dag_id="7.1-externalTaskSensor", # El onmbre de este DAG es el External Dag ID del archivo 7.2
    description="DAG principal",
    schedule_interval="@daily",
    start_date=datetime(2025, 3, 9),
    end_date=datetime(2025, 3, 11)
) as dag:

    t1 = BashOperator(task_id="tarea_1",
                      bash_command="sleep 10 && echo 'DAG finalizado!'",
                      depends_on_past=True)