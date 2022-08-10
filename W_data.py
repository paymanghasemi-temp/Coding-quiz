# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 17:43:55 2022

@author: saghandp
"""


import pandas as pd
import numpy as np
from io import StringIO


def main():
    # reading file and removing unnecessary characters
    file = open('w_data.dat').read()
    file = file.replace("*", "")
    file = file.replace("<pre>", "")
    file = file.replace("</pre>", "")

    # removing empty lines
    file = [x for x in file.split("\n") if x]
    # calculating median length of lines
    median_len = np.median([len(x) for x in file])
    # finding the first line with length > median to assure the first line is the column headers
    for idx, val in enumerate(file):
        if len(val) >= median_len:
            break
    file = ''.join([str(x) + '\n' for x in file[idx:]])
    lst = pd.read_fwf(StringIO(file))
    # remove rows that are not reflecting a day number
    if lst['Dy'].dtype == 'object':
        lst = lst.loc[lst['Dy'].apply(lambda x: x.isnumeric())]
    # creating a new column called 'Diff' showing MxT - MnT
    lst['Diff'] = lst['MxT'].astype(float) - lst['MnT'].astype(float)
    # printing the name of the day with the smallest Diff
    print(lst['Dy'].iloc[lst['Diff'].idxmin()])


if __name__ == '__main__':
    main()
