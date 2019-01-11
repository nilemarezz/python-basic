#!/usr/bin/env python
# coding: utf-8

# # List ก็ คือ Array นั้นแหละ
# - มี list ซ้อน list ได้ 
# - คำสั่งต่างๆมี append(ต่อข้อมูลท้ายList)
# -           insert(ต่อข้อมูลตาม index ที่ใส่)
# -           remove(ค่าทีจะลบ),del ตัวแปร[ตำแหน่ง]

# In[1]:


l = [1,2,3]
print(l) # [1, 2, 3]


# In[2]:


l.append('A')
print(l)  # [1, 2, 3, 'A']


# In[4]:


l.insert(1,'b')
print(l) # [1, 'b', 2, 3, 'A']


# In[5]:


l.remove('b')
print(l) # [1, 2, 3, 'A']


# In[10]:


del l[3]
print(l)


# # Tuple 
# - เหมือน list เต่เปลียนจาก [] เป็น () และ ###ไม่สามารถเปลี่ยนค่าได้ ###
# 

# In[16]:


point = (10,20)
print(point)
print(type(point))
'''' (10, 20)
<class 'tuple'>
'''


# In[ ]:




