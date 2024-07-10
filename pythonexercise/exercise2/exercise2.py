#!/usr/bin/env python
# coding: utf-8

# In[ ]:


number = int(input("Enter a number"))
word = ""
while number > 1:
    if(number %2 == 0):
        number=int(number/2)
        word="0"+word
    else:
        number=int(number/2)
        word="1"+word
word="1"+word
print(word)

