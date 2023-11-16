"""Multiprocessing"""
import os
from multiprocessing import Process, freeze_support
import psutil


PROCESSES = []


def target_sub_process():
    current_process = psutil.Process()
    cpu_affinity = current_process.cpu_affinity()
    print('Process id: ', os.getpid())
    print('Parent: ', os.getppid())
    print('cpu_affinity: ', cpu_affinity)


for index in range(3):
    PROCESSES.append(Process(target=target_sub_process, name=f'process_{str(index).zfill(1)}'))


if __name__ == '__main__':
    freeze_support()
    for process in PROCESSES:
        process.start()
    for process in PROCESSES:
        process.join()
