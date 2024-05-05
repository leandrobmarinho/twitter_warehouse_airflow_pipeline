"""
### Tutorial Documentation
Documentation that goes along with the Airflow tutorial located
[here](https://airflow.apache.org/tutorial.html)
"""
from __future__ import annotations

# [START tutorial]
# [START import_module]
import textwrap
from datetime import datetime, timedelta

# The DAG object; we'll need this to instantiate a DAG
from airflow.models.dag import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator, BranchPythonOperator
import pandas as pd
import requests
import json
# [END import_module]


def captura_conta_dados():
    url = "https://data.cityofnewyork.us/resource/rc75-m7u3.json"
    repos = requests.get(url)
    df = pd.DataFrame(json.loads(repos.content))
    qtd = len(df.index)
    return qtd

def e_valida(ti):
    qtd = ti.xcom_pull(task_ids='captura_conta_dados')
    if qtd >= 1000:
        return 'valido'
    else:
        return 'nvalido'    


# [START instantiate_dag]
with DAG(
    "tutorial_dag",
    # [START default_args]
    # These args will get passed on to each operator
    # You can override them on a per-task basis during operator initialization
    # default_args={
    #     "depends_on_past": False,
    #     "email": ["airflow@example.com"],
    #     "email_on_failure": False,
    #     "email_on_retry": False,
    #     "retries": 1,
    #     "retry_delay": timedelta(minutes=5),
    #     # 'queue': 'bash_queue',
    #     # 'pool': 'backfill',
    #     # 'priority_weight': 10,
    #     # 'end_date': datetime(2016, 1, 1),
    #     # 'wait_for_downstream': False,
    #     # 'sla': timedelta(hours=2),
    #     # 'execution_timeout': timedelta(seconds=300),
    #     # 'on_failure_callback': some_function, # or list of functions
    #     # 'on_success_callback': some_other_function, # or list of functions
    #     # 'on_retry_callback': another_function, # or list of functions
    #     # 'sla_miss_callback': yet_another_function, # or list of functions
    #     # 'on_skipped_callback': another_function, #or list of functions
    #     # 'trigger_rule': 'all_success'
    # },
    # [END default_args]
    description="A simple tutorial DAG",
    # schedule_interval='30 * * * *',
    schedule=timedelta(days=1),
    start_date=datetime(2021, 1, 1),
    catchup=False,
    # tags=["example"],
) as dag:
    # [END instantiate_dag]


    captura_conta_dados = PythonOperator(
        task_id="captura_conta_dados",
        python_callable=captura_conta_dados,
    )

    e_valida = BranchPythonOperator(
        task_id="e_valida",
        python_callable=e_valida,
        provide_context=True,
    )

    valido = BashOperator(
        task_id="valido",
        bash_command="echo 'Quantidade OK'",
    )

    nvalido = BashOperator(
        task_id="nvalido",
        bash_command="echo 'Quantidade errada'",
    )


    captura_conta_dados >> e_valida >> [valido, nvalido]

    # # t1, t2 and t3 are examples of tasks created by instantiating operators
    # # [START basic_task]
    # t1 = BashOperator(
    #     task_id="print_date",
    #     bash_command="date",
    # )

    # t2 = BashOperator(
    #     task_id="sleep",
    #     depends_on_past=False,
    #     bash_command="sleep 5",
    #     retries=3,
    # )
    # # [END basic_task]

    # # [START documentation]
    # t1.doc_md = textwrap.dedent(
    #     """\
    # #### Task Documentation
    # You can document your task using the attributes `doc_md` (markdown),
    # `doc` (plain text), `doc_rst`, `doc_json`, `doc_yaml` which gets
    # rendered in the UI's Task Instance Details page.
    # ![img](https://imgs.xkcd.com/comics/fixing_problems.png)
    # **Image Credit:** Randall Munroe, [XKCD](https://xkcd.com/license.html)
    # """
    # )

    # dag.doc_md = __doc__  # providing that you have a docstring at the beginning of the DAG; OR
    # dag.doc_md = """
    # This is a documentation placed anywhere
    # """  # otherwise, type it like this
    # # [END documentation]

    # # [START jinja_template]
    # templated_command = textwrap.dedent(
    #     """
    # {% for i in range(5) %}
    #     echo "{{ ds }}"
    #     echo "{{ macros.ds_add(ds, 7)}}"
    # {% endfor %}
    # """
    # )

    # t3 = BashOperator(
    #     task_id="templated",
    #     depends_on_past=False,
    #     bash_command=templated_command,
    # )
    # # [END jinja_template]

    # t1 >> [t2, t3]
# [END tutorial]