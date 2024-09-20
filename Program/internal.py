#!/usr/bin/env python
# coding: utf-8

# ## 10.  Create table cricketer(cid, cname, match, run) and insert 8 players records. Print player records with average.  and write this data into player.csv file. Do all this task from python.
# 

# In[1]:


import sqlite3 as sq


# In[2]:


con=sq.connect("C:\sqlite3\player.db")


# In[3]:


c=con.cursor()


# ## create table

# In[5]:


c.execute("create table if not exists cricketer(cid int primary key,cname text,match,run)")


# In[7]:


c.execute("insert into cricketer values(101,'virat kohli',5,300)")


# In[8]:


c.execute("insert into cricketer values(102,'MS dhoni',4,300)")


# In[9]:


c.execute("insert into cricketer values(103,'krish gel',5,350)")


# In[10]:


c.execute("insert into cricketer values(104,'mesi',5,300)")


# In[11]:


c.execute("insert into cricketer values(105,'sachin',5,300)")


# In[12]:


c.execute("insert into cricketer values(106,'rohit sharma',5,300)")


# In[13]:


c.execute("insert into cricketer values(107,'aman',5,300)")


# In[14]:


c.execute("insert into cricketer values(108,'krish',5,350)")


# In[16]:


c.execute("select * from cricketer")
rec=c.fetchall()
print(rec)


# ## avgerage

# In[19]:


c.execute("select cname, match, run, (run * 1.0 / match) as average from cricketer")
rec=c.fetchall()
print(rec)


# In[20]:


query ="select cname, match, run, (run * 1.0 / match) as average from cricketer"


# In[21]:


c.execute(query)


# In[22]:


rec=c.fetchall()
print(rec)


# In[23]:


import pandas as pd


# ## read the data into a pandas DataFrame

# In[25]:


df = pd.read_sql_query(query, con)


# In[26]:


print(df)


# ## Write the dataframe to csv file

# In[28]:


df.to_csv('player.csv', index=False)


# In[29]:


con.close()


# In[ ]:




