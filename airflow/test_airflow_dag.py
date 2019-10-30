'''
This is demonstration for airflow dag
'''

import random

import airflow
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import BranchPythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner' : 'ddc',
    'start_date' : datetime(2019, 10, 31),
}

dag = DAG('ddc_dag', default_args=default_args, schedule_interval=timedelta(days=1))

A = DummyOperator(
    task_id='A',
    dag=dag,
)

B = BashOperator(
    task_id='B',
    bash_command='echo "This is B bash operator"',
    dag=dag
)

options = ['D', 'E']

C = BranchPythonOperator(
    task_id='C',
    python_callable=lambda: random.choice(options),
    dag=dag,
)


D = BashOperator(
    task_id='D',
    bash_command='echo "This is D bash operator"',
    dag=dag
)


E = BashOperator(
    task_id='E',
    bash_command='echo "This is E bash operator"',
    dag=dag
)
A >> B >> C >> [D, E]
