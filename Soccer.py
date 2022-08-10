# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 17:16:40 2022

@author: saghandp
"""
import pandas as pd
from io import StringIO


def main():
    # reading file and removing unnecessary characters
    file = open('soccer.dat').read()
    file = file.replace("-", "")
    file = file.replace("<pre>", "")
    file = file.replace("</pre>", "")
    # converting the remaining string to dataframe using fixed width
    lst = pd.read_fwf(StringIO(file))
    # creating a new column called 'Diff' showing abs(F - A)
    lst['Diff'] = abs(lst['F'].astype(int) - lst['A'].astype(int))
    # printing the name of the team with the smallest Diff
    print(lst['Team'].iloc[lst['Diff'].idxmin()])


if __name__ == '__main__':
    main()
