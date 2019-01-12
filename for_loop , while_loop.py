#!/usr/bin/env python
# coding: utf-8

# # forloop
# เหมือน Java แต่ syntax แตกต่างกัน

# In[2]:


for x in [1,2,3]:
    print(x)


# In[4]:


l = list(range(1,11))
print(l)


# In[5]:


for x in l:
    print(x)


# In[6]:


for x in l:
    if(x%2 != 0):
        print(x)
        '''
1
3
5
7
9
        '''


# In[12]:


# loop ค่าใน dict ออกมา
param = {'id' :1 ,
        'name': 'Lisa',
        'loan' : False}
for k, v in param.items():
    print(k + '=' + str(v ))


# In[13]:


# ปริ้น Index และค่าใน list 
o = [1,2,3,4,5]
for idx, x in enumerate(o):
    print(idx,x)


# In[16]:


# เอา x หลังจากที่loopค่า มา *2
list_1 = [x*2 for x in range(0,6)]
print(list_1)


# # While loop
#     ใช้เมื่อเราไม่รู้ว่าค่าที่จะ loop เลยใช้เป็น condition
#     

# In[17]:


i = 0
while(i<10):
    print(i)
    i = i+1
    


# In[19]:


check = False
loan = 5000
money = 10000
while(check == False):
    loan = loan - 1000
    money = money - 1000
    print('your loan = ' + str(loan))
    print('your MONEY = ' + str(money))
    if(loan == 0):
        check = True
print('END')        
print(money)        


# In[ ]:





# In[ ]:




