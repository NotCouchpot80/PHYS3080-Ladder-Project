# import required libraries
import os
import numpy as np
import scipy as sp
import matplotlib as mpl
from astropy.table import Table
import glob

# import data from Data directory
allPointsFiles = glob.glob('../Data/*/*/points.txt')
allFuzzyFiles = glob.glob('../Data/*/*/fuzzy.txt')
closePoints = []

# take all close points as reference
fig = plt.figure()
for j, pointsFile in enumerate(allPointsFiles):
    try:
        this = Table.read(pointsFile,format='ascii')

        thispar = this['par']
        thism0, thism1, thism2 = (np.log10(this['flux1']), 
                                  np.log10(this['flux2']), 
                                  np.log10(this['flux3']))
        thiscolour = thism2-thism0
        dist = 1/thispar
        abs_mag = thism1 + 2*np.log10(dist)
        
        for point in this:
            if point['par'] > 0.05:
                closePoints.append(point)
        
        h = plt.scatter(thiscolour[mm],abs_mag[mm],color=colours[1])
    except:
        pass

s = plt.scatter(colour,m1,color=colours[0])

plt.ylabel('Log Flux 1')
plt.xlabel('Log Flux 2 - Log Flux 0')

plt.legend([h,s],['Benchmark','Cluster'])