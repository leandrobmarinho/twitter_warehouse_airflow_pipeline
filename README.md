for detailed description of the project refer this blog: https://medium.com/@devparmar967/a-quick-guide-for-building-datawarehouse-and-etl-pipelines-with-airflow-19cce17017bd


# STEPS TO START:

- create virtual environment
  - conda create --name airflow_env python=3.9 -y
  - pip install "apache-airflow[celery]==2.9.0" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.9.0/constraints-3.9.txt"
- download dependencies
- set path variable `AIRFLOW_HOME` to this directory
- set environment variables for twitter credentials and DB details
- run `airflow db migrate` ~airflow db init~
- you probably don't hav any airflow user yet, so create one, run `airflow users create` and follow instructions
- open current directory in two terminal windows run `airflow schuduler` in one and `airflow webserver` in other
- go to `localhost:8080` and login with the user credentials you just created
- you should be able to see `twitter_wh_dag` there
