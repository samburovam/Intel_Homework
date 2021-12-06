from time_namespace.get_time_package.get_time_module import time
from datetime import datetime

def pretty_time():
    formatted_time = datetime.fromtimestamp(time()).strftime("%Y-%m-%d %H:%M:%S")
    return formatted_time
def pretty_print():
    print(pretty_print())