# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 17:16:40 2022

@author: saghandp
"""
import pandas as pd


def main():
    file = open('soccer.dat')
    lst = []
    # add a column 'number' to the line that has less columns
    lst += ['number']
    # this for loop removes the lines with less than 8 coloumns and adds elements of lines to a list
    for line in file:
        line = line.replace("-", "")
        if len(line.split()) > 7:
            lst += line.split()
    # reshaping list as pandas array with 9 columns
    lst = pd.array(lst).reshape(-1, 9)
    lst = pd.DataFrame(list(lst[1:]), columns=list(
        lst[0]))  # creating a pandas dataframe
    # creating a new column called 'Diff' showing abs(F - A)
    lst['Diff'] = abs(lst['F'].astype(int) - lst['A'].astype(int))
    # printing the name of the team with the smallest Diff
    print(lst['Team'].iloc[lst['Diff'].idxmin()])


if __name__ == '__main__':
    main()
