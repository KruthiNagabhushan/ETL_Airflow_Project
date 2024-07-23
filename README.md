# ETL Data Engineering Project

This project demonstrates an end-to-end ETL (Extract, Transform, Load) process using Apache Airflow, Python, and Amazon S3. The project extracts data from the Random User Generator API, transforms it, and loads it into an S3 bucket. The workflow is managed by Airflow and runs on an EC2 instance.


## Project Overview
The main goal of this project is to:
1. Extract data from the Random User Generator API.
2. Transform the data using Python.
3. Load the transformed data into an S3 bucket.
4. Orchestrate the workflow using Apache Airflow.

## Prerequisites
- Python 3.8 or higher
- Apache Airflow
- Amazon Web Services (AWS) account
  - S3 bucket
  - IAM role with S3 access
- An EC2 instance with Airflow installed

## Files
- t_etl.py: This file contains the ETL logic:
  - Extract data from the Random User Generator API.
  - Transform the data.
  - Load the data into an S3 bucket.


- t_dag.py: This file defines the Airflow DAG that orchestrates the ETL process.
### Clone the Repository
```bash
git clone https://github.com/KruthiNagabhushan/ETL_Airflow_Project.git
cd etl_airflow_project
```

## Configure Airflow
Ensure that your Airflow instance is running and configured correctly. Place the DAG file in the dags directory of your Airflow setup.
Configure Airflow
1. Connect to EC2 Instance: 
Connect to your EC2 instance using SSH:

```bash
ssh -i /path/to/your-key.pem ec2-user@your-ec2-public-dns
```

2. Install Apache Airflow: Update the package list and install Apache Airflow:
```bash
sudo apt-get update
sudo apt-get install -y python3-pip
pip install apache-airflow
pip install pandas
pip install s3fs
```

3. Configure Airflow
  - Initialize the Airflow database:
    ```bash
    airflow db init
    ```
  - Create a directory for your Airflow DAGs (if it doesn't already exist):
    ```bash
    mkdir -p ~/airflow/dags
    ```
  - Copy your DAG file (t_dag.py) to the dags directory:
    ```bash
    cp dags/t_dag.py ~/airflow/dags/
     ```

  - Edit the airflow.cfg file to set the dags_folder path (if necessary):
    ```bash
    sudo nano ~/airflow/airflow.cfg
    ```
  - Update the dags_folder path to point to your DAGs directory:
    ```bash
    dags_folder = /home/your-username/airflow/dags
    ```
  - Start the Airflow web server:
    ```bash
    airflow webserver --port 8080
    ```





