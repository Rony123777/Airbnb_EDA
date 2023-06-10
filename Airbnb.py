#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# In[2]:


data=pd.read_csv('Airbnb Dataset 19.csv')
data.shape


# In[3]:


data.dtypes


# In[4]:


data.head(3)


# In[5]:


data.describe()


# In[6]:


data.id.count()


# In[7]:


data.isnull().sum()


# In[8]:


data.dtypes


# In[9]:


data.columns


# In[10]:


plt.rcParams['figure.figsize'] = (10, 6)
sns.countplot(data.neighbourhood_group)


# In[11]:


# new_data=data['last_review']
# new_data


# In[12]:


sns.countplot(data.room_type)


# In[13]:


sns.boxenplot(data.price)


# In[14]:


sns.boxenplot(data.number_of_reviews)


# In[15]:


data.head()


# In[16]:


sns.countplot(data.calculated_host_listings_count)


# In[17]:


sns.countplot(data.minimum_nights)


# In[74]:


data.dtypes


# In[18]:


plt.figure(figsize=(12,8))
sns.scatterplot(x=data.longitude,y=data.latitude,hue=data.neighbourhood_group)
plt.show()


# Room Types and Neighbourhood Group
# 
# We will first check the distribution of the room type by grouping the data. From the below its clear the Apartment and Private data is more than that of shared rooms. In general, Shared rooms costs less and can be very useful for travellers who moves from one city to another city quite frequently. Though the shared rooms data is less, we will still try to uncover as much details as we can.

# In[19]:


data['room_type'].value_counts().plot(kind='bar',color=['r','b','y'])
plt.show()


# *Exploration of Neighbourhood Group
# 
# Let's explore the neighbourhood group now to see the data distribution. From the below it looks like Manhattan and Brooklyn has more number of listing that the Queens,Bronx and Staten island.

# In[21]:


data['neighbourhood_group'].value_counts().plot(kind='bar',color=['r','b','y','g','m'])
plt.show()


# Location and Review Score
# 
# Review is the one of the important criteria with online activity these days. This gives a lot of insights to a particular place for tourist and they can swing mood when it comes to online booking. A cheap place with bad review can drive a tourist for not booking and an expensive place with nicest review can shell a tourist more than what he have thought initially. So we will try to figure out the review , how each neighbourhood is doing in respect to review. Since there is a limited data with review we will try to figure out as much as we can.
# 
# First criteria of our review is we will consider only those who have a review more than 50, so that we can have an insight of the data.
# 
# So according to the below plot, Brooklyn got most review in comparison to Manhattan and that is an interesting find. Also Staten Island which is cheaper has less review than the other neighbourhood group. We cannot proceed further to understand why is that case since we have a limited data.

# In[22]:


fig = plt.figure(figsize=(12,4))
review_50 = data[data['number_of_reviews']>=50]
df2 = review_50['neighbourhood_group'].value_counts()
df2.plot(kind='bar',color=['r','b','g','y','m'])
plt.title('Location and Review Score(Min of 50)')
plt.ylabel('Number of Review')
plt.xlabel('Neighbourhood Group')
plt.show()
print(' Count of Review v/s neighbourhood group')
pd.DataFrame(df2)


# In[ ]:




