#!/usr/bin/env python
# coding: utf-8

# # Write a Python function to sum all the numbers in a list.
# #Sample List : (8, 2, 3, 0, 7)
# #Expected Output : 20

# In[1]:


list1=[int(x) for x in input("enter elements for list =").split()]
print("list is" , list1)
def sum(x):
    sum=0
    for i in list1:
        sum=sum+i
    return sum
z=sum(list1)
print("sum of elements in list" ,z)


# In[ ]:




