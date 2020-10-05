#!/usr/bin/evn python3
# Lance Fletcher

# CPU Utilization: % of time that the CPU is busy
# Throughput: # of processes done in a unit of time
# Turnaround time: Time it takes to run a process from init to term., including all the waiting time
# Waiting time: The total amount of time that a process is in the ready queue
# Response time: The time between when a process is ready to run and its next I/O request
# Fairness!
# CPU SCHEDULER POLICIES
# Minimize response time
# Minimize variance of average response time
# Maximize throughput
# Minimize waiting time
# Scheduling algorithms reward I/O bound and penalize CPU bound patterns
# CPU SCHEDULER POLICIES
# Minimize response time
# Provide output to the user as quickly as possible and process their input as soon as it is received

import random as r
import time


class Process:
    def __init__(self):
        self.pid = r.randrange(100, 600)
        self.work_remaining = r.randrange(2, 20)  # process has a min max of 1 to 15 instructions
        self.priority = r.randrange(1, 10)  # 10 levels of priority
        self.started = False
        self.start_time = 0  # when process first started being processed
        self.end_time = 0  # when process has completely executed
        self.total_wait_time = 0  # for turnaround

    # copy constructor
    def copy(self):
        copy_process = Process()
        copy_process.pid = self.pid
        copy_process.work_remaining = self.work_remaining
        copy_process.priority = self.priority
        copy_process.started = self.started
        copy_process.start_time = self.start_time
        copy_process.start_time = self.end_time
        copy_process.total_wait_time = self.total_wait_time
        return copy_process

    def terminate_process(self):
        global TIMER
        self.end_time = TIMER

    def start_process(self):
        global TIMER
        self.start_time = TIMER


class CPU:
    def __init__(self, name):
        self.name = name
        self.total_completed_processes = 0
        self.current_process = None
        self.cpu_usage = 0
        self.ready_Q = []


def print_cpu_info(cpu1, cpu2, cpu3, cpu4):  # cpu should be cpu object
    print("Algorithm\t\tQueue Total\t\tCPU Usage %\t\tCurrent PID\t\tTotal Processes Completed")
    print(cpu1.name + "\t\t\t" + str(len(cpu1.ready_Q)) + "\t\t\t" + str(round((cpu1.cpu_usage/TIMER), 3)) + "\t\t\t\t" + str(cpu1.current_process) + "\t\t\t\t\t" + str(cpu1.total_completed_processes))
    print(cpu2.name + "\t\t\t\t" + str(len(cpu2.ready_Q)) + "\t\t\t" + str(round((cpu2.cpu_usage/TIMER), 3)) + "\t\t\t\t" + str(cpu2.current_process) + "\t\t\t\t\t" + str(cpu2.total_completed_processes))
    print(cpu3.name + "\t\t\t" + str(len(cpu3.ready_Q)) + "\t\t\t" + str(round((cpu3.cpu_usage/TIMER), 3)) + "\t\t\t\t" + str(cpu3.current_process) + "\t\t\t\t\t" + str(cpu3.total_completed_processes))
    print(cpu4.name + "\t\t\t" + str(len(cpu4.ready_Q)) + "\t\t\t" + str(round((cpu4.cpu_usage/TIMER), 3)) + "\t\t\t\t" + str(cpu4.current_process) + "\t\t\t\t\t" + str(cpu4.total_completed_processes))


def Round_Robin(cpu):
    print("Round Robin Ready Queue:", end = ' ')
    for process in cpu.ready_Q:
        print(process.work_remaining, end = ' ')
    print()
    # no processes in queue
    if len(cpu.ready_Q) == 0:
        return
    else:
        loaded_process = cpu.ready_Q[0]
        cpu.current_process = loaded_process.pid
        if not loaded_process.started:  # process is new to ready_Q
            loaded_process.start_process()
            loaded_process.started = True
        cpu.cpu_usage += 1
        loaded_process.work_remaining -= 1
    if loaded_process.work_remaining == 0:
        loaded_process.terminate_process()
        cpu.ready_Q.pop(0)
        cpu.total_completed_processes += 1
        # popped last process in ready Q
        if len(cpu.ready_Q) == 0:
            cpu.current_process = None
            return
    else: # send first process to back of list
        send_to_back = cpu.ready_Q.pop(0)
        cpu.ready_Q.append(send_to_back)


def FCFS(cpu):
    print("FCFS Ready Queue:", end = ' ')
    for process in cpu.ready_Q:
        print(process.work_remaining, end = ' ')
    print()
    # no processes in queue
    if len(cpu.ready_Q) == 0:
        return
    else:
        loaded_process = cpu.ready_Q[0]
        cpu.current_process = loaded_process.pid
        if not loaded_process.started:  # process is new to ready_Q
            loaded_process.start_process()
            loaded_process.started = True
        cpu.cpu_usage += 1
        loaded_process.work_remaining -= 1
    if loaded_process.work_remaining == 0:
        loaded_process.terminate_process()
        cpu.ready_Q.pop(0)
        cpu.total_completed_processes += 1
        # popped last process in ready Q
        if len(cpu.ready_Q) == 0:
            cpu.current_process = None
            return

def Shortest_Process(cpu):
    print("Shortest Process Ready Queue:", end = ' ')
    for process in cpu.ready_Q:
        print(process.work_remaining, end = ' ')
    print()
    if len(cpu.ready_Q) == 0:
        return
    elif not cpu.ready_Q[0].started:
        smallest = 100
        i = 0
        process_index = 0
        # find shortest process
        while i < len(cpu.ready_Q):
            if cpu.ready_Q[i].work_remaining < smallest:
                smallest = cpu.ready_Q[i].work_remaining
                loaded_process = cpu.ready_Q[i]
                process_index = i
            i += 1
        bring_to_front = cpu.ready_Q.pop(process_index)
        cpu.ready_Q.insert(0, bring_to_front)
        cpu.current_process = loaded_process.pid
        loaded_process.start_process()
        loaded_process.started = True
    else:
        loaded_process = cpu.ready_Q[0]
        cpu.current_process = loaded_process.pid
    cpu.cpu_usage += 1
    loaded_process.work_remaining -= 1
    if loaded_process.work_remaining == 0:
        loaded_process.terminate_process()
        cpu.ready_Q.pop(0)
        cpu.total_completed_processes += 1
        # popped last process in ready Q
        if len(cpu.ready_Q) == 0:
            cpu.current_process = None

def Priority(cpu):
    print("Priority Ready Queue:", end = ' ')
    for process in cpu.ready_Q:
        print(process.work_remaining, end = ' ')
    print()
    if len(cpu.ready_Q) == 0:
        return
    elif not cpu.ready_Q[0].started:
        priority = 0
        i = 0
        process_index = 0
        # find highest priority
        while i < len(cpu.ready_Q):
            if cpu.ready_Q[i].priority > priority:
                priority = cpu.ready_Q[i].priority
                loaded_process = cpu.ready_Q[i]
                process_index = i
            i += 1
        bring_to_front = cpu.ready_Q.pop(process_index)
        cpu.ready_Q.insert(0, bring_to_front)
        cpu.current_process = loaded_process.pid
        loaded_process.start_process()
        loaded_process.started = True
    else:
        loaded_process = cpu.ready_Q[0]
        cpu.current_process = loaded_process.pid
    cpu.cpu_usage += 1
    loaded_process.work_remaining -= 1
    if loaded_process.work_remaining == 0:
        loaded_process.terminate_process()
        cpu.ready_Q.pop(0)
        cpu.total_completed_processes += 1
        # popped last process in ready Q
        if len(cpu.ready_Q) == 0:
            cpu.current_process = None


TIMER = 0  # Global variable


def main():
    CPU_1 = CPU("Round Robin")
    CPU_2 = CPU("FCFS")
    CPU_3 = CPU("Shortest P")
    CPU_4 = CPU("Priority")
    PCB_Table1 = []
    PCB_Table2 = []
    PCB_Table3 = []
    PCB_Table4 = []
    total_processes = r.randrange(25, 30)
    # create PCB_Tables of random length between 15 and 20
    for i in range(total_processes):
        new_process = Process()
        PCB_Table1.append(new_process)
        PCB_Table2.append(new_process.copy())
        PCB_Table3.append(new_process.copy())
        PCB_Table4.append(new_process.copy())
    finished = False
    global TIMER
    random_key = 3
    while not finished:
        # load each ready queue with random process from PCB table
        if random_key == r.randrange(1, 5) and len(PCB_Table1) != 0:
            random_process = r.randrange(0, len(PCB_Table1))
            CPU_1.ready_Q.append(PCB_Table1.pop(random_process))
            CPU_2.ready_Q.append(PCB_Table2.pop(random_process))
            CPU_3.ready_Q.append(PCB_Table3.pop(random_process))
            CPU_4.ready_Q.append(PCB_Table4.pop(random_process))
        time.sleep(.25)
        TIMER += 1
        Round_Robin(CPU_1)
        FCFS(CPU_2)
        Shortest_Process(CPU_3)
        Priority(CPU_4)
        print_cpu_info(CPU_1, CPU_2, CPU_3, CPU_4)
        # check if all processes are done
        if len(PCB_Table1) == 0 and len(CPU_1.ready_Q) == 0 and len(PCB_Table2) == 0 and len(CPU_2.ready_Q) == 0 and len(PCB_Table3) == 0 and len(CPU_3.ready_Q) == 0 and len(PCB_Table4) == 0 and len(CPU_4.ready_Q) == 0:
            finished = True


if __name__ == "__main__":
    main()
