
import FCFS
import SJF
import RoundRobin


enter_file = open("Processes.txt","r")
lines = enter_file.readlines()
lines = lines[1:]
n = len(lines)

tmp = []

# All of the processes
list_process_fcfs = [] 
list_process_sjf = []
list_process_rr = []


for a in lines:
    
    tmp = a.split("\t\t")
    for b in range (1,5):
        tmp[b] = int(tmp[b])
    id = int(tmp[0][1:])
    
    p_fcfs = FCFS.Process(id, tmp[1], tmp[2], tmp[3], tmp[4]) #creating object
    p_sjf = SJF.Process(id, tmp[1], tmp[2], tmp[3], tmp[4]) #creating object
    p_rr = RoundRobin.Process(id, tmp[1], tmp[2], tmp[3], tmp[4]) #creating object
    
    list_process_fcfs.append(p_fcfs)
    list_process_sjf.append(p_sjf)
    list_process_rr.append(p_rr)


list_process_fcfs.sort(key=lambda x: x.arrival) #sorting list_process according to process.arrival
list_process_sjf.sort(key=lambda x: x.current_cpu)
list_process_sjf.sort(key=lambda x: x.arrival) #sorting list_process according to process.arrival
list_process_rr.sort(key=lambda x: x.arrival) #sorting list_process according to process.arrival

    
FCFS.fcfs(list_process_fcfs, n)
SJF.sjf(list_process_sjf, n)
RoundRobin.round_robin(list_process_rr, n)

