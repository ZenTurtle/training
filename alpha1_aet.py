#!/usr/bin/env python3
'''
--------------------------------------------------------------------------------
Module Name:    alpha1_aet.py
Author:         Marco Soldano marco@zenturtle.net
Date:           2021_01_01
Description:    alpha1 aerobic threshold plotter

--------------------------------------------------------------------------------
Notes:
--------------------------------------------------------------------------------
                      Copyright 2021, ZenTurtle Inc
--------------------------------------------------------------------------------
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import argparse
import sys

DATAPATH = '/data/'  # relative location for storing plots and output

def main():
    parser = argparse.ArgumentParser(description='Alpha1-AeT visualizer')
    parser.add_argument('-f', '--file', dest='filename', action='store', help='features.csv file from HRV Logger', required=True)
    args = parser.parse_args()
    datafile = args.filename

    print ("Scanning {}".format(datafile))
    try:
        with open(datafile, 'rb') as f:
            df = pd.read_csv(f, sep=",", skipinitialspace=True)

    except IOError:
        print ('Could not read file {}'.format(datafile))
        return

    print (df.head())
    df.plot.scatter(x='alpha1', y='heart_rate')
    plt.title(datafile)
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
    plt.xlim([0.4, 1.4])
    plt.axvline(x=.75)

    # Trendline
    x = df['alpha1']
    y = df['heart_rate']
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    plt.plot(x,p(x),"r--")
    print('AeT={:.1f}bpm'.format(p(0.75)))
    aet=p(0.75) 
    plt.text(0.8,aet+5,'AeT={:.1f}bpm'.format(p(0.75)))
    plt.show()


"""

with open('2021-3-19_Features_.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)
"""

if __name__ == '__main__':
    main()
