# input dataframe with timepoints
# return calculations for each row
import pandas as pd
import numpy as np

def pkr_functional_score(df):
    # fill missing timepoints with 0
    timepoints = ['0hr','12hr','16hr','20hr']
    df[timepoints] = df[timepoints].fillna(0)

    # normalize read count
    timepoints = ['0hr','12hr','16hr','20hr']
    for tp in timepoints:
        df[f'{tp}_norm'] = df[tp]/df[tp].sum()

    # -log2(fold change) from 0hr
    df[f'{timepoints[0]}_-log2fc'] = np.log2(1)
    for tp1 in timepoints[1:]:
        tp0 = timepoints[0]
        df[f'{tp1}_-log2fc'] = -np.log2(df[f'{tp1}_norm'] / df[f'{tp0}_norm'])

    # manage infinite values to max -log2fc per timepoint
    for tp in timepoints[1:]:
        col = f'{tp}_-log2fc'
        max_val = df.query(f'`{col}` != `{np.inf}`')[col].max()
        df[col].replace(np.inf, max_val, inplace=True)

    # AUC
    def calculate_auc(row):
        """calculate AUC across timepoints"""
        timepoints = ['0hr','12hr','16hr','20hr']
        col_list = [tp + '_-log2fc' for tp in timepoints]
        values = row[col_list].values
        auc_value = np.trapz(values,dx=1)
        return auc_value
    df['auc'] = df.apply(calculate_auc, axis=1)

    return df
