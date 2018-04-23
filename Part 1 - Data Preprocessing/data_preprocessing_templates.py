# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

# Data Preprocessing

#Import the Libraries

import  numpy as np
import pandas as pd
import  matplotlib as mp

#Importing the dataset

dataset = pd.read_csv('50Startups.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,4].values

#Encoding categorical data
#Encoding the independent variable
