# Margaret and Sagunya
# 8/8/22
# This program generates ptm psm visuals for 
# 4 ptms based on percentage certainty.

import pandas as pd
import matplotlib.pyplot as plt

# x-axis. Ranges for all plots
ranges = ["P<0.01", "0.01<=P<0.05", "0.05<=P<0.20", "0.20<=P<0.80", "0.80<=P<0.95", "0.95<=P<0.99", "P>=0.99", "no-choice"]

# generates labels of y values on bar charts
def add_labels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha = 'center')

# generates plots for any psm
def generate_plots(ptm_type, plot_index):
    # file with all nuclear sites for a ptm
    df = pd.read_csv(f"C:\\Users\\jli\\plantproteomes\\SeqComparison\\proteomes\\arabidopsis\\{ptm_type}_nuclear.txt", sep="\t")

    # stores sums for the ranges
    values = []
    # get all column names
    col_names = list(df.columns.values)
    # find the "bins" columns and get their sums.
    # store in values
    for i in range(7, 15):
        values.append(df[col_names[i]].astype(int).sum())
    
    #plt.subplot(2,2,plot_index)

    ## plotting ##
    plt.bar(ranges, values)
    add_labels(ranges, values)

    plt.title(f"Distribution of {ptm_type} Nuclear PSMs")
    plt.xlabel('PTMProphet Probability')
    plt.ylabel('Number of PSMs')

    #if plot_index == 4:
        #plt.show()

    plt.show()

# generating plots
generate_plots("phospho", 1)
generate_plots("acetyl", 2)
generate_plots("gly", 3)
generate_plots("gg", 4)