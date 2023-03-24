"""Example program to demonstrate how to send a multi-channel time series to
LSL."""

import random
import time

from pylsl import StreamInfo, StreamOutlet


info = StreamInfo('BioSemi', 'EEG', 16, 100, 'float32', 'myuid34234')


outlet = StreamOutlet(info)

print("now sending data...")
while True:

    #8ch
    """ mysample = [random.random(), random.random(), random.random(), random.random(),
                random.random(), random.random(), random.random(), random.random()] """
    #16ch
    mysample = [random.random(), random.random(), random.random(), random.random(),
                random.random(), random.random(), random.random(), random.random(),
                random.random(), random.random(), random.random(), random.random(),
                random.random(), random.random(), random.random(), random.random()]
    #32ch
    """ mysample = [random.random(), random.random(), random.random(), random.random(),
                random.random(), random.random(), random.random(), random.random(),
                random.random(), random.random(), random.random(), random.random(),
                random.random(), random.random(), random.random(), random.random(),
                random.random(), random.random(), random.random(), random.random(),
                random.random(), random.random(), random.random(), random.random(),
                random.random(), random.random(), random.random(), random.random(),
                random.random(), random.random(), random.random(), random.random()] """
    #send it and wait for a bit
    outlet.push_sample(mysample)
    time.sleep(0.007)