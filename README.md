for detailed description of the project refer this blog: https://medium.com/@devparmar967/a-quick-guide-for-building-datawarehouse-and-etl-pipelines-with-airflow-19cce17017bd


# STEPS TO START:

- conda create --name airflow_env python=3.9 -y
- pip install "apache-airflow[celery]==2.9.0" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.9.0/constraints-3.9.txt"