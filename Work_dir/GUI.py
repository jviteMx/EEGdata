import os
import time
import threading
import multiprocessing as mp
def main():
    os.system("python Work_dir\ReceiveData.py")
def monitor():
    os.system('python Work_dir\dataHandler_monitor.py')
def plot():
    os.system('python Work_dir\plot.py')
#def resources():
    #os.system('python Work_dir\Resource_monitor.py')


if __name__ == '__main__':

       
    x = threading.Thread(target=main)
    x.start()
    time.sleep(2)
    #t=threading.Thread(target=resources) 
    
    y = threading.Thread(target=monitor,daemon=True)
    #z = threading.Thread(target=plot)
    #t.start()    
    time.sleep(2)
    y.start()
    time.sleep(10)
    #z.start()

    """  mp.set_start_method('spawn')
    t=mp.Process(target=resources)    
    x = mp.Process(target=main)
    x.start()
    t.start()
    y = mp.Process(target=monitor,daemon=True)        
    time.sleep(2)
    y.start()
    time.sleep(1)
    #z = mp.Process(target=plot)
    #z.start() """
    
    
    

