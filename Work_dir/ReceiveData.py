

from pylsl import StreamInlet, resolve_stream
import sys
import time
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.integrate import simps

import os



def main(binTime,fileNumber):
    i=0
    # first resolve an EEG stream on the lab network    
    streams = resolve_stream('type', 'EEG')
    #start file system for recording.    
    inlet = StreamInlet(streams[0]) 
    sys.stdout = open("Data/data_streams/dataStreamA"+str(fileNumber)+".csv", "w")      
    start_time= time.time() 
    #------read from stream with time pased as argument-------        
    while i<2.58:
        # get a new sample (you can also omit the timestamp part if you're not
        # interested in it)
        offset = inlet.time_correction()
        #print('Offset: ' + str(offset))
        sample, timestamp = inlet.pull_sample()
        measureTime=time.time()
        print(sample,measureTime-start_time)
        #print(sample)
        #print(timestamp-offset)
        i=measureTime-start_time            

                
if __name__ == '__main__':
    """Study time is just how long will the loop keep going untill the bin collection stops"""
    studyTime=20000
    """Bin time is the seconds the bin is going to last
    bin size will depend on the sampling frequency of the device/simulator. this will work with sf in dataHandler_linear
    to provide the size of the bin for calculation the higher the number, the more samples collected, the longer it takes to proces
    the final computed file(short for speed, long for accuracy)"""
    binTime=5
    #created the data array to work online in a faster method
    #full_Data=np.empty(0,5)    
    for i in range(studyTime):               
        main(binTime,i)               
        
    """dont plot on the same script, ploting requires different tread, otherwise samples are droped with pause."""
        
        

       

