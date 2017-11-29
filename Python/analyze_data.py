from __future__ import division
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mydir = os.path.expanduser("~/GitHub/Task2_Competition/")

def plot_data():
    df = pd.read_csv(mydir + 'data/2017-11-14-count.txt', sep = '\t')
    rows_to_keep = []
    for index, row in df.iterrows():
        wt = row['WT']
        spo0a = row['spoA']
        if (wt == 'TMTC') or (spo0a == 'TMTC') :
            continue
        wt_spo0a = int(wt) + int(spo0a)
        if (wt_spo0a < 30):
            continue
        rows_to_keep.append(index)


    def cfus_ml(column, conc):
        return column * (10 ** (int(conc) * -1))

    df_keep = df.ix[rows_to_keep]
    df_keep.WT = df_keep.WT.astype(int)
    df_keep.spoA = df_keep.spoA.astype(int)

    df_keep['WT_cfus_ml'] = df_keep.apply(lambda x: cfus_ml(x.WT, x.Concentration), axis=1)
    df_keep['spoA_cfus_ml'] = df_keep.apply(lambda x: cfus_ml(x.spoA, x.Concentration), axis=1)


    df_keep = df_keep.drop(['Concentration', 'WT', 'spoA', 'Rep'], 1)
    df_keep = df_keep.groupby(['Day','Flask'], as_index=False).mean()
    df_keep.WT_cfus_ml = np.log10(df_keep.WT_cfus_ml)
    df_keep.spoA_cfus_ml = np.log10(df_keep.spoA_cfus_ml)

    df_keep_mean = df_keep.groupby(['Day'], as_index=False).mean()
    x = df_keep_mean['Day']
    y_wt = df_keep_mean['WT_cfus_ml']
    y_spoA = df_keep_mean['spoA_cfus_ml']
    df_keep_std = df_keep.groupby(['Day'], as_index=False).std()
    wt_std = df_keep_std['WT_cfus_ml']
    spoA_std = df_keep_std['spoA_cfus_ml']

    fig = plt.figure()
    plt.errorbar(x, y_wt, wt_std, linestyle='None', marker='^', label = 'WT')
    plt.errorbar(x, y_spoA, spoA_std, linestyle='None', marker='^', label = 'spo0A knockout')
    plt.legend()
    plt.xlabel('Days')
    plt.ylabel('CFUs/ ml, log10')

    fig_name = mydir + 'figs/test_fig.png'
    fig.savefig(fig_name, bbox_inches = "tight", pad_inches = 0.4, dpi = 600)
    plt.close()

plot_data()
