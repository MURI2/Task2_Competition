from __future__ import division
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mydir = os.path.expanduser("~/GitHub/Task2_Competition/")

def plot_data():
    df = pd.read_csv(mydir + 'data/2017-11-29-count.txt', sep = '\t')
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

def geometric():
	df = pd.read_csv(mydir + 'data/2017-11-29-count.txt', sep = '\t')
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
	#df_keep.WT_cfus_ml = np.log10(df_keep.WT_cfus_ml)
	#df_keep.spoA_cfus_ml = np.log10(df_keep.spoA_cfus_ml)
	
	def get_geometric(sizes):
		n_s = sizes.values
		def product(list):
			p = 1
			for i in list:
				p *= i
			return p
		prod = product(n_s)
		return prod **(1/len(n_s))
	
	wt_geom = df_keep['WT_cfus_ml'].groupby(df_keep['Flask']).apply(get_geometric)
	spo0A_geom = df_keep['spoA_cfus_ml'].groupby(df_keep['Flask']).apply(get_geometric)
	
	data_to_plot = [np.log10(wt_geom), np.log10(spo0A_geom)]
	
	# Create a figure instance
	fig = plt.figure(1, figsize=(9, 6))

	# Create an axes instance
	ax = fig.add_subplot(111)

	# Create the boxplot
	bp = ax.boxplot(data_to_plot)

	# Save the figure
	fig.savefig('fig1.png', bbox_inches='tight')
	
	## Custom x-axis labels
	ax.set_xticklabels(['WT', 'Spo0A'])
	## Remove top axes and right axes ticks
	ax.get_xaxis().tick_bottom()
	ax.get_yaxis().tick_left()
	ax.set_ylabel('Geometric fitness, log10',  fontsize=18)

	
	fig_name = mydir + 'figs/geom.png'
	fig.savefig(fig_name, bbox_inches = "tight", pad_inches = 0.4, dpi = 600)
	plt.close()
	
	
	
	
geometric()

#plot_data()
