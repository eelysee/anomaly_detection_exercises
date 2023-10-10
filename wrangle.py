import pandas as pd
import numpy as np

def get_continuous_cat_feats(df) -> (list, list):
    '''
    find all continuous and catagorical numerical features
    
    returns: 2 lists of column names
    
    changed continuous defition to > 10
    '''
    cont = []
    cat = []
    
    num_df = df.select_dtypes('number')
    for col in num_df:
        if num_df[col].nunique() > 10:
            cont.append(col)
        else:
            cat.append(col)
    return cont , cat