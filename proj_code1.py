# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 19:18:42 2020

@author: brahmkeshwar
"""
import scrapper_selenium as ss
import pandas as pd

path='C:/Users/brahmkeshwar/Documents/ds_proj/chromedriver/chromedriver.exe'

df=ss.get_jobs('data scientist',15,False,path,15)

df

#df.to_csv('data_jobs.csv',index=False)