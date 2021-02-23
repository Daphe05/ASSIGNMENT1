#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector


# In[2]:


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Hebron2022",
  database="pop_for"
)


# In[3]:


mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)


# In[4]:


mycursor.execute("SELECT * FROM pop_for")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)


# In[5]:


import ipywidgets as wg


# In[6]:


from IPython.display import display


# In[7]:


STATE = wg.Text(value='STATE')
MALE = wg.IntSlider(description='MALE:')
display(STATE,MALE)


# In[ ]:




