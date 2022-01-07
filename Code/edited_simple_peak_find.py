import glob
import numpy as np
import matplotlib.pyplot as plt
import peakutils
import os

# Frequency spacing (spacing of x-axis)
dw=4.18879e+11

#Initialise Array to store frequency values with dataset names
frequencies = []
dsname = []
dat_dir_name = r'''C:\Users\Daniel\Desktop\Physics\Year 4\Project for Physicists\Data'''

# Files to analyse
datafile_names = [i for i in os.listdir(dat_dir_name) if i.endswith(".dat")]
print(datafile_names)
datafile_names.sort()
print(datafile_names)
print("")

#load files
for i in datafile_names:

    filepath = os.path.join(dat_dir_name, i)
    print(filepath)
        
    #Read the y data for this k-point
    ydat=np.loadtxt(filepath,usecols=1)
    #Read the frequencies (x-axis)
    xdat=np.loadtxt(filepath,usecols=0)

    #Find the maximum of the ydata
    maxy=max(ydat)

    #Divide all elements of the y-array to make the largest peak at 1
    ydat/=maxy
    print("Max Y value for this file:",maxy)
    
        
    # Find the indices of the peaks
    indices = peakutils.indexes(ydat, thres=0.025/max(ydat), min_dist=300)
    
    # Print out the frequencies of the peaks
    for J in range(0,len(indices)):
        peakfreq = indices[J]*dw
        print("Peak Found at frequency: ",peakfreq)
        print("")

        frequencies.append(peakfreq)
        dsname.append(i)
        outputdata = list(zip(dsname,frequencies))
 
    

        # Declare an array to plot points where the peaks have been found on the PSD graph
        ypeak=np.ndarray(shape=len(indices),dtype=float)

        # For each peak found, look up the index and then find the y axis value and store it
        for J in range(0,len(indices)):
            ypeak[J]=ydat[indices[J]]


            # Plot the input x and y data and the locations of the found peaks.
            plt.plot(xdat,ydat,'b--')
            plt.plot(indices*dw,ypeak,'rx')
            plt.show()

print(outputdata)
