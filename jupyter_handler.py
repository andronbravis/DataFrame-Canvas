import pandas as pd
from IPython import get_ipython
from inspector import inspect_namespace

shell = get_ipython()
namespace = shell.user_ns

def update_namespace(result):
    print(inspect_namespace(namespace))

def jupyter_register(update_namespace):
    shell.events.register('post_run_cell', update_namespace)
    