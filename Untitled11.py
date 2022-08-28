#!/usr/bin/env python
# coding: utf-8

# # #Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# 
# 
# 
# #Sample String : 'The quick Brow Fox'
# 
# #Expected Output :
# 
# #No. of Upper case characters : 3
# 
# #No. of Lower case Characters : 12
# 

# In[1]:


x=input("enter string")

def count_upper_lower(x):
    upper=0
    lower=0
    for i in x:
        if i.isupper() is True:
            upper=upper+1
        elif i.islower() is True:
            lower=lower+1
    print("No. of Upper case characters :", upper)
    print("No. of Lower case Characters : ",lower)
   
    
count_upper_lower(x)


# In[ ]:




