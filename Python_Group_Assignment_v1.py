# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 15:18:11 2021

@author: Ivan.Polakovic
"""

import os
os.getcwd()
os.chdir('C:\\Users\\Ivan.Polakovic\\Desktop\\IE\\Term II\\Python\\Group Assignment')

dir()
import numpy as np
import pandas as pd


df = pd.read_excel('RBA_KYC_Accounts_ALL_Ids.xlsx')
df.head()

