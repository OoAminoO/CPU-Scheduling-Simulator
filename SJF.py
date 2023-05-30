#In the name of God

class Process:
    def __init__(self, id, arrival, cpu1, io, cpu2):
        self.id = id
        self.arrival = arrival
        self.cpu1 = cpu1
        self.io = io
        self.cpu2 = cpu2
        self.waiting = 0   # Can be calculated through ---> turnaround - cpu - io
        self.response = -1
        self.turnaround = 0
        self.current_arrival = arrival
        self.current_cpu = cpu1
        self.is_io_done = 0
        self.set_io_and_current_cpu()
        
    def set_io_and_current_cpu(self):
        if self.io == 0:
            self.is_io_done = 1
            self.current_cpu = self.cpu1 + self.cpu2        
        


def do_process(list_final_process,list_process,current_time,ready_queue,t,current_and_t): # current_time is total time
    # Brings process from ready queue.
    # After doing its cpu time, its io is also done
    #    and the ready queue gets updated
    
    if(len(ready_queue)==0): # Ready queue is empty
        current_process = list_process[0]
        current_init_process = list_process[0]
        ready_queue.append(current_process)
        t = 1
        if(current_process.is_io_done==1):
            del list_process[0]
            t = 0
        

        
        if(len(list_process)!=0):
            while(len(list_process)!=0 and t<len(list_process) and list_process[t].current_arrival <= (current_time+current_process.current_cpu)):
                ready_queue.append(list_process[t]) # Pushes the process to the queue
                # Deletes element from the list of processes (list_process), beacause it wont need any process after that (io is done)
                if(list_process[t].is_io_done==1):
                    del list_process[t]
                    t-=1
                t+=1
            
        current_time = current_process.current_arrival
        current_time += current_process.current_cpu
        
        ready_queue.pop(0) # The process is done, so it is removed from ready queue
        
        ready_queue.sort(key=lambda x: x.id)
        ready_queue.sort(key=lambda x: x.current_cpu)

        
    
    
    # Updates waiting time and turn around time and response time and current arrival
        if(current_process.is_io_done==0):  
            ######################################################################################################################################## pop
            current_process.response = current_time - current_process.cpu1 - current_process.arrival
            # completes io and pushes it to the list_process according to its current_arrival
            current_process.is_io_done = 1
            current_process.current_cpu = current_process.cpu2
            current_process.current_arrival = current_time + current_process.io
            
            if(len(list_process)>t): # There still exists at least one process that should be brought to the ready queue
                
                if(current_process.current_arrival < list_process[t].current_arrival):
                    list_process.pop(0)
                    t-=1
                    list_process.insert(t,current_process)
                elif(current_process.current_arrival == list_process[t].current_arrival):
                    temp_t = t
                    while(temp_t<len(list_process) and ((current_process.current_cpu>list_process[temp_t].current_cpu and current_process.current_arrival == list_process[temp_t].current_arrival) or (current_process.id > list_process[temp_t].id and current_process.current_cpu==list_process[temp_t].current_cpu and current_process.current_arrival == list_process[temp_t].current_arrival))):
                        temp_t+=1
                    list_process.pop(0)
                    temp_t-=1
                    t-=1
                    list_process.insert(temp_t,current_process)
                
                elif(current_process.current_arrival > list_process[t].current_arrival):
                    temp_t = t # The place that the current process should be placed in list_process after its io time
                    while(temp_t<len(list_process) and (current_process.current_arrival > list_process[temp_t].current_arrival or ((current_process.current_cpu>list_process[temp_t].current_cpu and current_process.current_arrival == list_process[temp_t].current_arrival) or (current_process.id > list_process[temp_t].id and current_process.current_cpu==list_process[temp_t].current_cpu and current_process.current_arrival == list_process[temp_t].current_arrival)))):
                        temp_t+=1
                    list_process.pop(0)
                    temp_t-=1
                    t-=1
                    list_process.insert(temp_t,current_process)
            else: # This process in not done yet and all other processes are in the ready queue
                list_process.pop(0)
                list_process.append(current_process)
                t-=1 # This process is the first process that can get into the ready queue
                
            
            
        elif(current_process.is_io_done==1):
            if current_process.response == -1 and current_process.io == 0:
                current_process.response = current_time - current_process.current_cpu - current_process.arrival
            current_process.turnaround = current_time-current_process.arrival
            list_final_process.append(current_process)
            current_and_t.append(current_time)
            current_and_t.append(t)
            return 1 # One process is done!
        
        current_and_t.append(current_time)
        current_and_t.append(t)
        return 0
            

        
    
    #done
    
    # Updates time_idle and time_processing and total_time and ready_queue

    else:
        
        current_process = ready_queue[0]
        current_init_process = current_process


        if(len(list_process)!=0):
            while(len(list_process)!=0 and t<len(list_process) and list_process[t].current_arrival <= (current_time+current_process.current_cpu)):
                ready_queue.append(list_process[t]) # Pushes the process to the ready queue
                # Deletes element from list of process (list_process) beacause it wont need any process after that (io is done)
                if(list_process[t].is_io_done==1):
                    del list_process[t]
                    t-=1
                t+=1
        if(current_process.is_io_done==0):
            index = list_process.index(current_process)
        
        current_time += current_process.current_cpu
        ready_queue.pop(0) # The process is done, so get removed from the ready queue
        
        ready_queue.sort(key=lambda x: x.id)
        ready_queue.sort(key=lambda x: x.current_cpu)
        
        
            # Update waiting time and turn around time and response time and current arrival
        if(current_process.is_io_done==0):
            ######################################################################################################################################## pop
            
            current_process.response = current_time - current_process.cpu1 - current_process.arrival
            # Completes io and pushes it to the list_process according to its current_arrival
            current_process.is_io_done = 1
            current_process.current_cpu = current_process.cpu2
            current_process.current_arrival = current_time + current_process.io
            
            if(len(list_process)>t):  # There still exists at least one process that should be brought to the ready queue
                
                if(current_process.current_arrival < list_process[t].current_arrival):
                    list_process.pop(index)
                    t-=1
                    list_process.insert(t,current_process)
                elif(current_process.current_arrival == list_process[t].current_arrival):
                    temp_t = t
                    while(temp_t<len(list_process) and ((current_process.current_cpu>list_process[temp_t].current_cpu and current_process.current_arrival == list_process[temp_t].current_arrival) or (current_process.id > list_process[temp_t].id and current_process.current_cpu==list_process[temp_t].current_cpu and current_process.current_arrival == list_process[temp_t].current_arrival))):
                        temp_t+=1
                    list_process.pop(index)
                    temp_t-=1
                    t-=1
                    list_process.insert(temp_t,current_process)
                
                elif(current_process.current_arrival > list_process[t].current_arrival):
                    temp_t = t  # The place that the current process should be placed in the list_process after the io time
                    while(temp_t<len(list_process) and (current_process.current_arrival > list_process[temp_t].current_arrival or ((current_process.current_cpu>list_process[temp_t].current_cpu and current_process.current_arrival == list_process[temp_t].current_arrival) or (current_process.id > list_process[temp_t].id and current_process.current_cpu==list_process[temp_t].current_cpu and current_process.current_arrival == list_process[temp_t].current_arrival)))):
                        temp_t+=1
                    list_process.pop(index)
                    temp_t-=1
                    t-=1
                    list_process.insert(temp_t,current_process)
            else:
                list_process.pop(index)
                list_process.append(current_process)
                t = t-1
            
        elif(current_process.is_io_done==1):
            if current_process.response == -1 and current_process.io == 0:
                current_process.response = current_time - current_process.current_cpu - current_process.arrival
            current_process.turnaround = current_time-current_process.arrival
            list_final_process.append(current_process)
            current_and_t.append(current_time)
            current_and_t.append(t)
            return 1 # One process is done!
        current_and_t.append(current_time)
        current_and_t.append(t)
        return 0


def sjf(list_pro, num_pro):
    done = 0 # The processes that are done
    time_idle = 0 # The time that cpu has been idle
    time_processing = 0 # The time that cpu has been busy
    current_time = 0 # Total time
    t = 0 # t is index of first place of list_process that a process shouldbe put in ready queue
    list_final_process = []
    ready_queue = []
    current_and_t =[]
    while(done!=num_pro):
        done_or_not = do_process(list_final_process,list_pro,current_time,ready_queue,t,current_and_t)
        current_time = current_and_t[0]
        t = current_and_t[1]
        current_and_t = []
        done += done_or_not
    
    list_final_process.sort(key=lambda x: x.id) #sorting list_process according to process.id
        
    file = open("SJF_Output.txt","w+")
    file.write(40*"=")
    file.write("\n")
    file.write(18*" ")
    file.write("SJF")
    file.write("\n")
    file.write(40*"=")
    t = "\n\n" + "\t" + "response time" + "\t\t" + "turnaround time" + "\t\t" + "waiting time" + "\n"
    file.write(t)
    
    resp = 0
    waiting = 0
    turnaroundtime = 0
    for a in list_final_process :
        resp += a.response
        t = "P" + str(a.id)
        file.write(t)
        t = "\t" + str(a.response)
        file.write(t)
        turnaroundtime += a.turnaround
        t = "\t\t\t" + str(a.turnaround)
        file.write(t)
        w = a.turnaround - a.cpu1 - a.cpu2 - a.io
        waiting += w
        t = "\t\t\t" + str(w)
        file.write(t)
        time_processing += a.cpu1 + a.cpu2
        file.write("\n")
        
    avr_resp = round(resp/num_pro,2)
    avr_wait = round(waiting/num_pro,2)
    avr_turn = round(turnaroundtime/num_pro,2)
    
    file.write(60 * "_")
    file.write("\n")
    file.write("Avr")
    t = "\t" + str(avr_resp) + "\t\t\t" + str(avr_turn) + "\t\t\t" + str(avr_wait)+"\n\n\n"
    file.write(t)
        
        
    t = "Total time      : " + str(current_time) + "\n"
    file.write(t)
    
    time_idle = current_time - time_processing
    t = "Idle time       : " + str(time_idle) + "\n"
    file.write(t)
    
    t = "Burst time      : " + str(current_time - time_idle) + "\n"
    file.write(t)
    
    
    util = round(time_processing/current_time, 2)
    t = "CPU Utilization : " + str(util) + "\n"
    file.write(t)
    thr = round(num_pro/current_time * 1000, 2)
    t = "Throughput      : " + str(thr) + "\n"
    file.write(t)

