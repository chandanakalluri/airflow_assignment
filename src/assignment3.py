from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
default_args={
    'owener':'chandude',
    'retries':5,
    'retray_delay':timedelta(minutes=5)
}
def greet(name):
    print(f"happy birtday{name}")

def get_name():
    return 'chandu'

with DAG(
    default_args=default_args,
    dag_id='coder',
    description="created dag with python operator",
    start_date=datetime(2024, 5, 7,1)
)as dag:
    task1=PythonOperator(
    task_id="first_v1",
    python_callable=greet,
    op_kwargs={'name':'chandu'}
    )
    task2=PythonOperator(
    task_id="get_name",
    python_callable=get_name
)
task2 >> task1