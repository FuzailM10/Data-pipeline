# src/test_imports.py

import sys
import os
sys.path.insert(0, os.path.abspath('src'))

from api_client import fetch_data
from kafka_producer import produce_messages
from airflow_dag import fetch_and_produce
from data_storage import store_data

print("Imports successful:")
print("fetch_data:", fetch_data)
print("produce_messages:", produce_messages)
print("fetch_and_produce:", fetch_and_produce)
print("store_data:", store_data)
