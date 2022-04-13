import numpy as np
import matplotlib 
import matplotlib as mpl
import astropy
import os
#from tabulate import tabulate 

from astropy.timeseries import LombScargle
from astropy.table import Table

with open('/Users/calinperez/Desktop/PHYS3080/Untitled/U07/xrfdata.txt', 'r') as f:

    xray = f.read()
    #print(tabulate(xray, headers=['x', 'y', 'z']))
    print(xray)
    matplotlib.pyplot.scatter(xray)