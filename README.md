


Real-Time Data Processing Pipeline
Description
This project implements a real-time data processing pipeline using Python, Apache Kafka, and Apache Airflow. The pipeline fetches data from an API, processes it using Kafka, orchestrates tasks with Airflow, and stores results in a database.

Features
Data Fetching: Retrieves data from a specified API.
Kafka Integration: Produces and consumes messages using Kafka.
Airflow DAGs: Manages and schedules data processing tasks.
Data Storage: Saves processed data into a PostgreSQL database.
Setup
Prerequisites
Python: Ensure Python is installed. You can install it using Homebrew:


brew install python (code for mac)
Apache Kafka: Install Kafka using Homebrew:


brew install kafka(code for Mac)
Apache Airflow: Install Airflow using pip. 

Installation
Clone the Repository:



git clone https://github.com/FuzailM10/Data-pipeline.git
cd Data-pipeline
Create and Activate a Virtual Environment:


python -m venv venv
source venv/bin/activate
Install Dependencies:


pip install -r requirements.txt
Configuration
Kafka: Ensure Kafka is running on localhost:9092.
Airflow: Set up and initialize the Airflow database:

airflow db init
Usage
Run Airflow:


airflow webserver --port 8080
airflow scheduler
Start Kafka:
kafka-server-start /usr/local/etc/kafka/server.properties
Run the Pipeline:

Ensure all services are running.
Trigger the Airflow DAG to start processing.
Testing
Run unit tests to ensure the functionality of the components:

python -m unittest discover -s tests
Deployment
For deployment, configure your production environment, including Kafka, Airflow, and database services. Follow best practices for deploying Python applications and manage your configurations securely.

Contributing
Fork the repository.
Create a new branch for your feature or bug fix:

git checkout -b feature/your-feature
Commit your changes:
git commit -m "Add your message"
Push to your fork:

git push origin feature/your-feature
Create a pull request.
License
Specify the license under which the project is distributed (e.g., MIT License).

Contact
For any inquiries or issues, contact [Muhammad Fuzail] at [fuzailm@student.wpunj.edu]

