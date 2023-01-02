#!bin/env/python

"""This script is used to extract the links of the product from google;
The product name and the company name is used as the query"""

from bs4 import BeautifulSoup
import requests
import time
import random
from time import sleep
import pandas as pd

df1 = pd.read_csv('new_data.csv')
df1 = df1[0:1000].reset_index().drop(['index'], axis = 1)
df1['new_url'] = None

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")


USER_AGENTS = [
   #Chrome
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36']


count = 0
for i in range(len(df1['CompanyName'])):
    print(i)
    random_header = USER_AGENTS[random.randint(0,5)]
    try:
        for j in search("{}".format(df1['Target'][i]), tld="co.in", num=1, stop=1, pause=random.uniform(30,60)
                        ,lang='en',user_agent= random_header):
            print(random_header)
            print('{} - {}'.format(df1['Target'][i], j))       
            df1['new_url'][i] = j

    except Exception as e:
        print(e)
        df1['new_url'][i] = None
        sleep(5)
        continue
             
    count = count + 1
    if count > 20:
        sleep(20)
        count = 0
    else:
        pass    

df1.to_csv('res1.csv', index = False)
