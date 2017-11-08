import numpy as np
import pandas as pd
from seaborn import distplot
from matplotlib import pyplot as plt
from scipy.stats import boxcox, probplot
from sklearn.preprocessing import minmax_scale

def pd_boxcox(x, y, plots=False, scale_ = False):
    # HAS to be a Pandas Series - doing one variable at a time for transformation
    ary_x = x.as_matrix() # convert to np.array
    x_tran, lambda_ = boxcox(x, lmbda = None) # boxcox transform - lambda is
    print('For:',y,'lambda=', lambda_) 
    if scale_ == True:
        x_tran = minmax_scale(x_tran,feature_range=(0, 1), axis=0, copy=True)
    x_ret = pd.Series(x_tran, name = y) # convert back to Pandas Series
    # Plotting it to compare distribution
    if plots == True:
        plt.figure(figsize = (12,5))
        plt.subplot(1, 4, 1)
        distplot(x)
        plt.title('Original ' + y)
        plt.subplot(1, 4, 2)
        distplot(x_ret)
        plt.title('BoxCox Transform ' +y)
        plt.subplot(1, 4, 3)
        probplot(x, plot=plt)
        plt.title('Original ' + y)
        plt.subplot(1, 4, 4)
        probplot(x_ret, plot=plt)
        plt.title('BoxCox Transform ' +y)
        plt.show()
    return(x_ret, lambda_)