import glob
import numpy as np
import matplotlib.pyplot as plt
import peakutils
import os

# Frequency spacing (spacing of x-axis)
dw=4.18879e+11

# File to analyse
filename="kx0ky0kz1.dat"

# Simple check that the file exists
if(os.path.exists(filename)!=True):
    print("Error: file ",filename," does not exist")
    quit()
else:
    #Read the y data for this k-point
    ydat=np.loadtxt(filename,usecols=1)
    #Read the frequencies (x-axis)
    xdat=np.loadtxt(filename,usecols=0)

    #Find the maximum of the ydata
    maxy=max(ydat)

    #Divide all elements of the y-array to make the largest peak at 1
    ydat/=maxy

    # Find the indices of the peaks
    indices = peakutils.indexes(ydat, thres=0.025/max(ydat), min_dist=300)


# Print out the frequencies of the peaks
for i in range(0,len(indices)):
    print("Peak Found at frequency: ",indices[i]*dw)


# Declare an array to plot points where the peaks have been found on the PSD graph
ypeak=np.ndarray(shape=len(indices),dtype=float)

# For each peak found, look up the index and then find the y axis value and store it
for i in range(0,len(indices)):
    ypeak[i]=ydat[indices[i]]


# Plot the input x and y data and the locations of the found peaks.
plt.plot(xdat,ydat,'b--')
plt.plot(indices*dw,ypeak,'rx')
plt.show()
