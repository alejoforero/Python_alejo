# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 12:24:37 2020

@author: alejo
"""

import pandas as pd
from langdetect import detect 
from langdetect import detect_langs

import time

import multiprocessing
pool = multiprocessing.Pool(processes=2)
pool = multiprocessing.Pool()
pool.cpu_count()


cd "C:\\Users\\alejo\\OneDrive\Python"





stata215=pd.read_stata('c215_afternetwork_check.dta')

start_time = time.time()
stata215['language'] = pool.map(detect,stata215['china_second_part0'])
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
stata215['options']  =pool.map(detect_langs,stata215['china_second_part0'])
print("--- %s seconds ---" % (time.time() - start_time))


pool.close()

stata215['language'].value_counts()   

##




allnames=pd.read_stata('temp_COL_ALL_names.dta').loc[0:1000,['exportador']]



start_time = time.time()
allnames['language'] = pool.map(detect,allnames['exportador'])
print("--- %s seconds ---" % (time.time() - start_time))

allnames['language'] = map(detect,allnames['exportador'])




start_time = time.time()
stata215['options']  =pool.map(detect_langs,allnames['china_second_part0'])
print("--- %s seconds ---" % (time.time() - start_time))


pool.close()

stata215['language'].value_counts()   
    







    












 def myreplace(s):
    xx = detect(s)
    return xx


for index, row in stata215.iterrows():
    #print(row['exportador'],row['exportador1'])
    #stata215['language']=detect(stata215.exportador)
    print(index)
    print(detect(row['exportador']))
    row['language']=detect(row['exportador'])
    
    if index>100:
        break