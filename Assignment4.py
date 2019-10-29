#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


#Open data
fileName='/Users/Devon/Google Drive/2019 Q1 Spring/data/running/race.csv'
raceData=pd.read_csv(fileName)


# In[3]:


raceData.head()


# In[4]:


#Function to categorize data
def ageToCategory(age):
    
    if(age >= 0 and age <=19):
        return '0-19'
    elif(age >= 20 and age <= 29):
        return '20-29'
    elif(age >= 30 and age <= 39):
        return '30-39'
    elif(age >= 40 and age <= 49):
        return '40-49'
    elif(age >= 50 and age <= 59):
        return '50-59'
    elif(age >= 60 and age <= 69):
        return '60-69'
    elif(age >= 70 and age <= 79):
        return '70-79'
    elif(age >= 80):
        return '80+'
    


# In[5]:


#map data to new column
raceData['ageGroup']= raceData['age'].map(ageToCategory)
raceData.head()


# In[6]:


#Function to convert time
def convertTimeToSeconds(timeString):
    
    timeSplit = timeString.split(':')
    
    if(len(timeSplit) == 2):
        seconds=int(timeSplit[0])*60+int(timeSplit[1])
    elif(len(timeSplit) == 3):
        seconds=int(timeSplit[0])*3600+int(timeSplit[1])*60+int(timeSplit[2])
    
    return seconds


# In[7]:


#map data to new column
raceData['timeInSecs']= raceData['time'].map(convertTimeToSeconds)
raceData.head()


# In[8]:


#Create Bar Graph for Average Time of Each Age Group

ageGroup=raceData.groupby('ageGroup')
means=ageGroup.mean()

means['timeInSecs'].plot.bar()

plt.title('Average Time of Each Age Group')
plt.xlabel('Age Group')
plt.ylabel('Total Time')


plt.show()


# In[10]:


raceData.to_csv('raceDataFromPython.csv')


# In[ ]:




