import psutil as psu
import pandas as pd
from datetime import datetime

def get_time(process):
    try:
        return datetime.fromtimestamp(psu.boot_time())
    except OSError:
        print('Error on {}'.format(get_time.__name__))

def get_cpu_usage(process):
    try:
        return len(process.cpu_affinity()), process.cpu_percent()
    except psu.AccessDenied:
        return 0, process.cpu_percent()

def get_process_piority(process):
    try:
        return int(process.nice())
    except psu.AccessDenied:
        return 0

def get_memory_use(process):
    try:
        return process.memory_full_info().uss
    except psu.AccessDenied:
        return 0

def bytes_behavior(process):
    try:
        io_counters = process.io_counters()
        return io_counters.read_bytes, io_counters.write_bytes
    except psu.AccessDenied:
        print('Error on {}'.format(bytes_behavior.__name__))
        return 0, 0

def get_threads(process):
    try:
        return process.num_threads()
    except OSError:
        print('Error on {}'.format(get_threads.__name__))

def get_process_name(process):
    try:
        return process.name()
    except psu.AccessDenied:
        return "Process not found"

def get_process_status(process):
    try:
        return process.status()
    except psu.AccessDenied:
        return "Status not found"


data = []

for process in psu.process_iter():
    with process.oneshot():
        data.append({
        'Name': get_process_name(process),
        'Create_time': get_time(process),
        'Cores': get_cpu_usage(process)[0],
        'Cpu_usage': get_cpu_usage(process)[1],
        'Status': get_process_status(process),
        'Priority': get_process_piority(process),
        'Memory_usage': get_memory_use(process),
        'Read_bytes': bytes_behavior(process)[0],
        'Write_Bytes': bytes_behavior(process)[1],
        'Threads_number': get_threads(process)
        })

for i in data:
    print(i)


if __name__ == "__main__":
    print('A')