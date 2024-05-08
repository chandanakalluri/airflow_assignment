from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args={
    'owner':'coder2j',
    'retries':5,
    'retry_delay':timedelta(minutes=2)

}

with DAG(
    dag_id='dependency_task_dag_v4',
    default_args=default_args,
    description='creating first dag',
    start_date=datetime(2024, 5, 7, 2),
    schedule_interval='@daily'
)as dag:
   task1=BashOperator(
    task_id='first_task',
    bash_command="echo helloworld, this is the first task!"
   )
   task2=BashOperator(
    task_id='sec_task',
    bash_command="echo this is second task!!"
   )
   task3=BashOperator(
    task_id='third_task',
    bash_command="echo this is third task and run with second"
   )
#task1.set_downstream(task2)
# task1.set_downstream(task3)
task1>>task2
task1>>task3
task2>>task3
#task1>>[task2,task3]


