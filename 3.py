#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Librerias
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import pandas as pd
import bson
from bson.raw_bson import RawBSONDocument

#Variables
db_client = MongoClient()
my_db = db_client.juegos
my_posts = my_db.posts
    
def find_2nd(string, substring):
    return string.find(substring, string.find(substring) + 1)
def find_1st(string, substring):
    return string.find(substring, string.find(substring))


# In[2]:


response = requests.get('https://olympics.com/tokyo-2020/es/deportes/')
response2 = requests.get('https://resultados.as.com/resultados/juegos_olimpicos/medallero/')
soup = BeautifulSoup(response.content, "lxml")
soup2 = BeautifulSoup(response2.content, "lxml")

Sport=[]
Country=[]


#se escoge la etiqueta span
post_sports = soup.find_all("h2", class_="tk-disciplines__title")
post_countries = soup2.find_all("span", class_="team-inline")

#for para limpiar
for element in post_sports:
    #print(element)
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    #print (limpio)
    Sport.append(limpio.strip())
    
#for para limpiar
for element in post_countries:
    #print(element)
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    #print (limpio)
    Country.append(limpio.strip())


print(Sport)
print("==================================================================================================================")
print(Country)


# In[3]:


#Trasladar la lista a un dateframe
bd1=pd.DataFrame(Sport)
#Trasladar la lista a un dateframe
bd2=pd.DataFrame(Country)


# In[4]:


bd1


# In[5]:


bd2


# In[ ]:




