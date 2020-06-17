prschedule=[]
def w_t(i):
    su=0
    for _ in range(i):
        su+=float(prschedule[_][1])
    return su
def t_t(i):
    su=0
    for _ in range(i+1):
        su+=float(prschedule[_][1])
    return su
class process:
    def __init__(self,pid,bt):
        self.pid=pid
        self.bt=bt
print('Shortest Job First process scheduling : ')
n = int(input('Enter number of processes to be added : '))
for i in range(n):
    a=process(input('Enter process id'),input('Enter burst time'))
    prschedule.append((a.pid,a.bt))
    prschedule=sorted(prschedule,key=lambda x:x[1])
print('process id \t burst time \t waiting time \t turnaround time \t')
for i in range(len(prschedule)):
    print(prschedule[i][0] + '\t \t' + str(prschedule[i][1]) + '\t \t' + str(w_t(i))+'\t \t' + str(t_t(i)))

    
