
# coding: utf-8

# In[23]:

import os
import sys
import pandas as pd
import PRData

current_month = 'July 2016' #MOVE TO CONFIG

data = PRData.data_pull()
current_data = data[data['DATE'] == current_month]

urls = current_data[['URL']]['URL']

for url in urls:
    try:
        urls[url] = PRData.process_url(url)
    except:
        print "Could Not Process: %s" % url


#########################

current_month = config.current_month

data = PRData.data_pull()
current_data = data[data['DATE'] == current_month]


def naive_classification(dataframe, members, jurisdictions):
	"""This function takes in the data frame and two additional lists of tags we want to have identified 
	in the document. Each publication URL will have its text processed and checked to see if any in members or jurisdictions
	are in the web page."""


def watson_classification():
	pass
