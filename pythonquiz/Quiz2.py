#2210356066
#Zeynep Nisa Karatas
#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
try:

    twopoints = int(sys.argv[1])
    threepoints = int(sys.argv[2])
    singlethrows = int(sys.argv[3])
    total_score = twopoints*2 + threepoints*3 + singlethrows
    print(total_score)
except:
    pass

def healthStatus(height,mass):
    
    bmı = mass / height ** 2 
    if bmı>=30:
        return("obese")
    elif bmı>=24.9:
        return("overweight")
    elif bmı>=18.5:
        return("healthy")
    else:
        return("underweight")