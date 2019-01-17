#!/usr/bin/env python
# coding: utf-8

# # Segmenting and Clustering Neighborhoods in Toronto
#  Assignment: To scrape the given Wikipedia page and create the following Dataframe:
# 
# ![alt text](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/7JXaz3NNEeiMwApe4i-fLg_40e690ae0e927abda2d4bde7d94ed133_Screen-Shot-2018-06-18-at-7.17.57-PM.png?expiry=1547769600000&hmac=1eEHmCBfuyV9Ad-7aOVRNz9_y-IQBA0ZIxcRSwsURxA)

# In[50]:


#Import Libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[51]:


#download url data from internet
url= "https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M"
source= requests.get(url).text

#using beautiful soup to parse the html code
Canada_data= BeautifulSoup(source, "lxml")


# In[83]:


# creat a new Dataframe
column_names = ["PostalCode","Borough","Neighborhood"]
toronto = pd.DataFrame(columns = column_names)

# loop through to find postcode, borough, neighborhood 
content = Canada_data
table = content.tbody
postcode = 0
borough = 0
neighborhood = 0

for tr in table.find_all('tr'):
    i = 0
    for td in tr.find_all('td'):
        if i == 0:
            postcode = td.text
            i = i + 1
        elif i == 1:
            borough = td.text
            i = i + 1
        elif i == 2: 
            neighborhood = td.text.strip('\n')
    toronto = toronto.append({'PostalCode': postcode,'Borough': borough,'Neighborhood': neighborhood},ignore_index=True)

# clean dataframe 
toronto = toronto[toronto.Borough!='Not assigned'] #clean rows that contain "Not assigned" within column "Borough"
toronto = toronto[toronto.Borough!= 0] #clean rows that contain "0" within column "Borough"
i = 0
for i in range(0,toronto.shape[0]):
    if toronto.iloc[i][2] == 'Not assigned':
        toronto.iloc[i][2] = toronto.iloc[i][1] #if a cell has a borough but a Not assigned neighborhood, then the neighborhood will be the same as the borough
        i = i+1
#combine Neighborhoods where Postcode and Borough are the same into one row with the neighborhoods separated with a comma                                 
df = toronto.groupby(['PostalCode','Borough'])['Neighborhood'].apply(', '.join).reset_index()

df


# In[53]:


df.shape


# In[ ]:




