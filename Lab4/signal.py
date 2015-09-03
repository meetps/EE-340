#Chirp.py: Generating wideband signal into .csv file
#Installing numpy: sudo apt-get install python-numpy
from math import *                              # Import Math Library
import csv                                      # For getting matrix in CSV file
import numpy                                    # For numerical and matrix operations

N = 1000                                    # N is total number of samples
w=2*pi*10/(N-1)                               # Digital Frequency
data=numpy.zeros(N)                             # Define Container array for samples 1xN
for n in range(1,N+1):         
    data[n-1] = cos(w*n*N) * ( 10*sin(w*n)/(w*n) + pow(sin(w*n)/(w*n),2) )              # Collect Samples in Data array
a = numpy.array([range(1,N+1), data])           # Matrix 2xN
b = a.transpose()                               # Output Matrix Nx2
numpy.savetxt("Wave_Normal.csv", b, delimiter=",")      # Save output in file "Wave.csv"

sinc_array =numpy.zeros(N)
piT_array = numpy.zeros(N)
for n in range(1,N+1):
    sinc_array[n-1] = pow(sin(w*n)/(w*n),2)
    piT_array[n-1] = 1/(pi*n)
   
convolved_sinc2_array = numpy.convolve(sinc_array,piT_array, 'same')

data_2=numpy.zeros(N)
for n in range(1,N+1):         
    data_2[n-1] = 10*((1-cos(w*n))/(w*n))              # Collect Samples in Data array
data_2 = cos(w*n*N) * (data_2 - convolved_sinc2_array) 
a = numpy.array([range(1,N+1), data_2])
b = a.transpose()                               # Output Matrix Nx2

numpy.savetxt("Wave_Hilbert.csv", b, delimiter=",")      # Save output in file "Wave.csv"


