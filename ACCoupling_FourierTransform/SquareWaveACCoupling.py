#Majid Reza Barghi
# Physics 141
# This code is meant to simulate a simple square with DC and AC Coupling Through Osciloscope
# Should try to model square wave with fourier series, to get a acurate effect on corners
# This is will probably improve the effect in simulation. 

import numpy as np
import matplotlib.pyplot as plotter
from scipy import signal

#Setting our Frequency
samplingFrequency   =.5 ; # in Hertz 
samplingInterval       = 6000 # in Hertz sampling 1000 times per second

#Start and End Time
beginTime           = 0;

endTime             = 4;

#Generating Square Wave

time = np.linspace(beginTime, endTime, samplingInterval, endpoint=True)
noise = np.random.normal(0,.1,samplingInterval)

squareWave = 2.5*(signal.square(2 * np.pi * samplingFrequency * time))+2.5
squareWave = squareWave + noise 
# Create subplot

figure, axis = plotter.subplots(4, 1)

plotter.subplots_adjust(hspace=1)

# Plot the Square Wave
axis[0].set_title(f'Square wave with a frequency of {samplingFrequency} Hz')

axis[0].plot(time, squareWave)

axis[0].set_xlabel('Time')

axis[0].set_ylabel('Amplitude')

# Frequency domain representation
print("Calculating Fourier Transform...")



fourierTransform = np.fft.fft(squareWave)           # Normalize amplitude

fourierTransform = fourierTransform[range(int(len(squareWave)/2))] # Exclude sampling frequency


tpCount     = len(squareWave)

timeInverse = np.linspace(beginTime, endTime, int(tpCount/2), endpoint=True)
values      = np.arange(int(tpCount/2))

timePeriod  = tpCount/samplingFrequency

frequencies = values/timePeriod

# Plot the Fourier Transform 
axis[1].set_title('Fourier transform depicting the frequency components')

axis[1].plot(frequencies, abs(fourierTransform))

axis[1].set_xlabel('Frequency')

axis[1].set_ylabel('Amplitude')

fourierTransform[0:2] = fourierTransform[0:2]*0.0001
fourierTransform[3:20] = fourierTransform[3:20]*0.001

itx = np.fft.ifft(fourierTransform)+2.5;

#Plot the Inverse of the Transform
axis[2].plot(timeInverse, itx)

axis[2].set_xlabel('Frequency')

axis[2].set_ylabel('Amplitude')

plotter.show()






