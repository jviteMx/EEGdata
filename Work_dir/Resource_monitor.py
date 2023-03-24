import psutil
import sys
import time



if __name__ == '__main__':
    start=time.time()
    endtime=900
    i=0
    while i<endtime:
        sys.stdout = open("Data/resourceMonitor/monitor"+".csv", "a")
        measure=time.time()
        print(psutil.cpu_percent(interval=0.5),",",measure-start)
        i=measure-start