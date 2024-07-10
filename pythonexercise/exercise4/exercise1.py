#!/usr/bin/env python
# coding: utf-8

# In[11]:


N = int(input("Please enter a number"))
odd_result = 0
ave_even = 0
if N > 0 :
    for i in range (1,N+1,2):
        odd_result = odd_result + i
    if N % 2 == 0 :
        ave_even = ((N+2)/2)
    elif N > 1:
        ave_even = (N+1)/2
    else:
        ave_even = 0
print("The sum of odd numbers is", odd_result)
print("Average of even numbers is", ave_even)


# In[ ]:




