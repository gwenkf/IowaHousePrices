# This function takes 3 arguments: data frame, list of column names, and # of neighbors
# It returns the original data frame with one extra column: 'distances'
# What does it do?
# 1. Calculates Euclidean distance for all observation pairs
# 2. For each observation it takes 'kneighbors' smallest distances and sums them up 
# 3. Puts those sums in a new column - 'distances'
# After it's done, we can inspect 'distances' column and toss those observations that have very high distances
# because high distances mean: This observation is very far even from its closest neighbors!

import sys
import pandas as pd
import numpy as np
import scipy
from scipy.spatial.distance import pdist, squareform

def outliers(data, nameslist, kneighbors = 40):
    dist = pdist(data[nameslist], metric='euclidean')   # calculate distances b/w rows
    dist = squareform(dist)                             # turn it into a squared numpy array (square matrix)
    nrows = data.shape[0]                               # number of rows in our data frame
    distances = pd.Series([0.0] * nrows)                # create placeholder for distances
    for i in range(nrows):
        myarray = dist[i]
        myarray = myarray[~np.isnan(myarray)]           # remove NANs
        myarray = np.sort(myarray)[0:(kneighbors + 1)]  # sort (ascending) and take only kneighbors distances
        distances[i] = np.sum(myarray)                  # sum up distances to kneighbors similar neighbors
    data['distances'] = distances                       # add 'distances' as a new column
    return data