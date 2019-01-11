#!/usr/bin/env python
# coding: utf-8

# # Type of Varaible
# - ของ python เหมือน Java
# - ไม่ต้องประกาศตัวแปร เขียนได้เลยเช่น
# - x = 1+2
# - โดยวิธีปริ้นใช้ print(x)ค่าจะเป็น 3
# - type(x) จะได้ int และสามารถกำหนดได้หลายตัวพร้อมกัน
# - String สมารถ ดู length ได้โดยใช้ len()

# In[ ]:





# In[6]:


x = 1+3


# In[7]:


print(x)


# In[8]:


type(x)


# In[10]:


x,y = 1,3


# In[11]:


print(x)
print(y)


# In[14]:


z = 'My Name is Matas'


# In[16]:


print(z)
print(type(z))
print(len(z))


# In[17]:


#replace คำ ได้ด้วย 
z1 = z.replace('Name' , 'Hello')
print(z1)


# In[18]:


# ถ้จะเอา ตัวแปรกับString มาต่อกัน ต้อง cast intให้เป็น String ก่อน 
print(str(y)+z1)


# # Opperator
# มี + - * / % ปกติ แต่ ยกกำลังเป็น ** เช่น 2ยกกำลัง5 คือ 2**5
# round() -  ปัดเศษ 
# 1. เครื่องหมาย = คือการกำหนดค่า
# 2. เครื่องหมาย == คือการเช็คค่าว่าเท่ากันหรือไม่

# In[12]:


y = 2**4


# In[13]:


print(y)


# In[ ]:





# In[ ]:




