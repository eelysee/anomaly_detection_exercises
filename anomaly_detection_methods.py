import pandas as pd
import numpy as np


def get_lower_and_upper_bounds(ser):
    '''
    takes in an series/array/df.column
    outputs two series 
    first series is mild outliers 1.5*iqr
    second series is extreme outliers 3*iqr
    
    '''
    q1 = ser.quantile(0.25)
    q3 = ser.quantile(0.75)
    iqr = q3 - q1
    lower_inner_fence = q1 - (1.5*iqr)
    upper_inner_fence = q3 + (1.5*iqr)
    lower_outer_fence = q1 - (3*iqr)
    upper_outer_fence = q3 + (3*iqr)
    
    # Create masks for each segment
    extreme_outliers = ser[(ser < lower_outer_fence) | (ser > upper_outer_fence)]
    mild_outliers = ser[(ser < lower_inner_fence) | (ser > upper_inner_fence)]   
    # Create DataFrame with original data and its segment
    inner_fence = pd.DataFrame({
        'inner_fence': mild_outliers
                               })
    
    outer_fence = pd.DataFrame({
        'outer_fence': extreme_outliers
                                })
    
    return inner_fence, outer_fence
    

'''
def zscore_anom(array):
    
    
def 

'''