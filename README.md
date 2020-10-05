# scheduling-algorithms-comparison
Process scheduling simulation that compares the scheduling algorithms, round robin, first come first serve, shortest process first, priority
Each algorithm has its own 'CPU' (created cpu class) and PCB_Table
Each cpu possesses access to a ready queue which holds all of the processes ready to be executed.
The algorithms are set up in a way that the cpu is always processing the first process in the queue (cpu.ready_Q[0]).
Thus if we want to load a new process into the 'cpu' we move the desired process to the first element in the array.
