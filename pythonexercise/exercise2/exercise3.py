#!/usr/bin/env python
# coding: utf-8

# In[ ]:


b = int(input("Enter a number for b"))
c = int(input("Enter a number for c"))
squarerootdelta = (b**2-4*c)**0.5
root1 = (-b + squarerootdelta)/2
root2 = (-b - squarerootdelta)/2
print("First root is {} , second root is {}".format(root1,root2))

