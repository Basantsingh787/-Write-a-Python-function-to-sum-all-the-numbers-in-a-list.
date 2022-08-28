#!/usr/bin/env python
# coding: utf-8

# # Write a Python program to reverse a string.
# 
# #Sample String : "1234abcd"
# #Expected Output : "dcba4321"

# In[1]:


x=input("enter string ")
def reverse(x):
    for i in x:
        x=x[::-1]
        return x
print("after reversing string = ",reverse(x))


# In[ ]:




