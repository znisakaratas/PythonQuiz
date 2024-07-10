#!/usr/bin/env python
# coding: utf-8

# In[1]:


year = int(input("Please enter a year"))
if year % 400 == 0:
    print("The year you entered is a leap year")
elif year % 4 == 0 and year % 100 != 0:
    print("The year you entered is a leap year")
else:
    print("The year you entered is not a leap year")


# In[ ]:




