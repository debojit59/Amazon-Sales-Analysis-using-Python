#!/usr/bin/env python
# coding: utf-8

# # Amazon Sales Analysis Using Python

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv(r"C:\Users\hp\Desktop\2023 data analytics\python project data set\amazon sales\Amazon Sale Report.csv",encoding='unicode_escape')


# In[3]:


df.head()


# In[4]:


df.shape


# ## Data Cleaning 

# In[5]:


df.info()


# In[6]:


df.drop(['New','PendingS'],axis=1,inplace=True)


# In[7]:


df.describe()


# In[8]:


df.isnull().sum()


# In[9]:


df.shape


# In[10]:


df.dropna(inplace=True)


# In[11]:


#change Data Type
df['ship-postal-code']=df['ship-postal-code'].astype(int)


# In[12]:


df['ship-postal-code'].dtype


# In[13]:


#change data type of date
df['Date']=pd.to_datetime(df['Date'])


# In[14]:


#rename column
df.rename(columns={'Qty':'Quantity'})


# In[15]:


df.describe()


# ## Exploratory Data Analysis

# In[16]:


df.columns


# In[17]:


plt.figure(figsize=(10,7))
ax=sns.countplot(x='Size',data=df)
for i in ax.containers:
    ax.bar_label(i)


# In[18]:


S_Qty=df.groupby(['Size'],as_index=False)['Qty'].sum().sort_values(by='Qty',ascending=False)


# In[19]:


plt.figure(figsize=(10,7))
s_ax=sns.barplot(x='Size',y='Qty',data=S_Qty)
for i in s_ax.containers:
    s_ax.bar_label(i)


# ## NOTE: Based on the depicted graph, it's evident that M-Size accounts for the majority of quantity purchases in the sales data 

# In[20]:


plt.figure(figsize=(12,8))
a=sns.countplot(data=df,x='Courier Status',hue='Status')
for i in a.containers:
    a.bar_label(i)
plt.show()


# ## from the above graph it is evident that most of the orders are shipped through courier/

# In[21]:


df['Category']=df['Category'].astype(str)
data=df['Category']
plt.figure(figsize=(12,7))
plt.hist(data,bins=10,edgecolor='Black')
plt.xticks(rotation=90)
plt.show


# ## Most of the sold items are T-shirt

# In[22]:


# Calculate counts of True and False values in the 'B2B' column separately
true_count = (df['B2B'] == True).sum()
false_count = (df['B2B'] == False).sum()

# Create a pie chart
labels = ['True', 'False']
sizes = [true_count, false_count]
plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of B2B Values')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.show()


# ## only 0.8% sales comes from B2B sales

# In[23]:


plt.figure(figsize=(15,10))
sns.countplot(data=df,x='ship-state')
plt.xlabel('ship-state')
plt.ylabel('count')
plt.title('Distribution of state')
plt.xticks(rotation=90)
plt.show()


# In[44]:


state_sale= df['ship-state'].value_counts().reset_index()
state_sale.columns = ['ship-state', 'Count']
state_sale.head(10)


# In[45]:


plt.figure(figsize=(15, 10))
sns.barplot(data=state_sale.head(10), x='ship-state', y='Count')
plt.xlabel('ship-state')
plt.ylabel('Count')
plt.title('Top 10 Ship States by Count')
plt.xticks(rotation=45)
plt.show()


# ## From the graph it is observed that Maharastra, Karnataka and Uttarpradesh have the highest number of sales

# In[ ]:




