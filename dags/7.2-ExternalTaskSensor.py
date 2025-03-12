from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.sensors.external_task import ExternalTaskSensor # Se importa sensor


with DAG(dag_id="7.2-externalTaskSensor",
    description="DAG Secundario",
    schedule_interval="@daily",
    start_date=datetime(2025, 3, 9),
    end_date=datetime(2025, 3, 11),
    max_active_runs=1
) as dag:
    
    # Definición del sensor (igual que un operador. 'Es otro operador')
    t1 = ExternalTaskSensor(task_id="waiting_dag",
							external_dag_id="7.1-externalTaskSensor", # Lee el nombre del dag del archivo 7.1
							external_task_id="tarea_1", # Lee el nombre de la tarea del archivo 7.1
							poke_interval=10 # Cada 10 segundos pregunta si ya termino la tarea
							)

    t2 = BashOperator(task_id="tarea_2",
					  bash_command="sleep 10 && echo 'DAG 2 finalizado!'",
					  depends_on_past=True)

    t1 >> t2