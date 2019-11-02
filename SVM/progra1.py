#!/usr/bin/env python
# coding: utf-8

# In[5]:


try:
    from pyspark.sql import SparkSession
except:
    import findspark
    findspark.init()
    from pyspark.sql import SparkSession
    


# In[6]:


spark=SparkSession.builder    .master("local[4]")    .appName("Seminario de Estadistica")     .getOrCreate()


# In[11]:


data=spark.read.csv("titanic_eval.csv",sep=",",header=True)
print(type(data))


# In[12]:


#data.write.parquet("tinatinic.parquet")


# In[13]:


data=spark.read.parquet("tinatinic.parquet")


# In[14]:


data.show(2)

