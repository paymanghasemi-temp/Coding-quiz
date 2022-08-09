# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 17:43:55 2022

@author: saghandp
"""


import pandas as pd


def main():
    file = open('w_data.dat')
    lst = []
    # this for loop removes the lines with less than 8 coloumns
    # and add the first three elements of lines to a list
    for line in file:
        line = line.replace("*", "")
        if len(line.split()) > 7 and line.split()[0] != 'mo':
            lst += line.split()[:3]
    lst = pd.array(lst).reshape(-1, 3)
    lst = pd.DataFrame(list(lst[1:]), columns=list(
        lst[0]))  # creating a pandas dataframe
    # creating a new column called 'Diff' showing MxT - MnT
    lst['Diff'] = lst['MxT'].astype(float) - lst['MnT'].astype(float)
    # printing the name of the day with the smallest Diff
    print(lst['Dy'].iloc[lst['Diff'].idxmin()])


if __name__ == '__main__':
    main()
