#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

ran_num =random.randint(1,25)
number = int(input("Please enter a number between 1 and 25"))
while number != ran_num:
    if ran_num > number:
        number = int(input("Increase your number"))
    elif ran_num < number:
        number = int(input("Decrease your number"))
print("The number you entered is correct")


# In[ ]:




