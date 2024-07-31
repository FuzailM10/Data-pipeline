from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime
from api_client import fetch_data
from kafka_producer import produce_messages

def fetch_and_produce():
    data = fetch_data('https://api.example.com/data')
    produce_messages('my_topic', data)

default_args = {'owner': 'airflow', 'start_date': datetime(2024, 1, 1)}
dag = DAG('data_pipeline', default_args=default_args, schedule_interval='@daily')

fetch_produce_task = PythonOperator(
    task_id='fetch_and_produce',
    python_callable=fetch_and_produce,
    dag=dag
)
