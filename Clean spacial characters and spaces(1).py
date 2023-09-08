#!/usr/bin/env python
# coding: utf-8

# In[31]:


import re
from os import devnull
import pandas as pd
import xlrd
import numpy as np


# Function to clean a string (remove special characters and spaces at the beginning)
def clean_string(input_str):
    return re.sub(r'^[^a-zA-Z]+', '', input_str)

# Function to check if a string contains Arabic characters
def contains_arabic(text):
    arabic_pattern = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]+')
    return bool(arabic_pattern.search(text))


# Specify the input and output file names (Excel format)
input_excel_file = 'function77.xls'
output_excel_file = 'output77.xlsx'

# Define the specific column where you want to drop null values
column_to_check = 'NAME_LINE1'

# Read the Excel file into a DataFrame
wb = xlrd.open_workbook(input_excel_file, logfile=open(devnull, 'w'))
df = pd.read_excel(wb, engine='xlrd')

# Clean the data in each cell of each row
df[column_to_check] = df[column_to_check].apply(clean_string)

# Drop rows with null values in the specified column
df[column_to_check] = df[column_to_check].replace('',np.nan)
df.dropna(subset=[column_to_check], inplace=True,axis=0)

# Remove rows containing Arabic characters in the specified column
df = df[~df[column_to_check].apply(contains_arabic)]


# Save the cleaned DataFrame to an Excel file
df.to_excel(output_excel_file, index=False)

print("Cleaning and removing null values from the specific column completed.")


# In[32]:


df.isnull().sum()


# In[29]:


df


# In[ ]:




