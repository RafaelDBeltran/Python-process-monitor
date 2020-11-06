import psutil as psu
from datetime import datetime

def get_time(process):
    try:
        return datetime.fromtimestamp(psu.boot_time())
    except OSError:
        print('Error on {}'.format(__name__))

for process in psu.process_iter():
    with process.oneshot():
        #take process name
        name = process.name()
        create_time = get_time(process)
