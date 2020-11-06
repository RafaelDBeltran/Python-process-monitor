import psutil as psu
from datetime import datetime

def get_time(process):
    try:
        return datetime.fromtimestamp(psu.boot_time())
    except OSError:
        print('Error on {}'.format(__name__))

def get_cpu_usage(process):
    try:
        return len(process.cpu_affinity()), process.cpu_percent()
    except psu.AccessDenied:
        return 0, process.cpu_percent()

for process in psu.process_iter():
    with process.oneshot():
        #take process name
        name = process.name()
        create_time = get_time(process)
        cores, cpu_usage = get_cpu_usage(process)
        print(cpu_usage)
