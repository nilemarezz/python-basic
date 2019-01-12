#!/usr/bin/env python
# coding: utf-8

# # Function
#     เหมือน Java อีกแล้ว มี Main ไปเรียกใช้ function
#     

# In[3]:


# Function
def showName():
    print('Matas Paosriwong')

# Function
def sumOfNum(x,y):
    z = x+y
    return z

#Main
showName()
x ,y = 10, 20
sumOfNum(x, y)


# In[17]:


# 
def cal(x):
    y = x*0.1 + x 
    return y

list = [100,200,300]
for i in list:
    print(cal(i))


# # Return หลายค่า 
#     ค่าที่ได้จะเป็น tuple 

# In[18]:


def plusFive(x):
    plus = x + 5
    return x,plus

print(plusFive(4))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




