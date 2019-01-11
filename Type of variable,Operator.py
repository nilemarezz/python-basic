#!/usr/bin/env python
# coding: utf-8

# # Type of Varaible
# - ของ python เหมือน Java
# - ไม่ต้องประกาศตัวแปร เขียนได้เลยเช่น
# - x = 1+2
# - โดยวิธีปริ้นใช้ print(x)ค่าจะเป็น 3
# - type(x) จะได้ int และสามารถกำหนดได้หลายตัวพร้อมกัน
# - String สมารถ ดู length ได้โดยใช้ len()


x = 1+3
print(x)
type(x)

x,y = 1,3
print(x)
print(y)

z = 'My Name is Matas'
print(z)
print(type(z))
print(len(z))

#replace คำ ได้ด้วย 
z1 = z.replace('Name' , 'Hello')
print(z1)

# ถ้จะเอา ตัวแปรกับString มาต่อกัน ต้อง cast intให้เป็น String ก่อน 
print(str(y)+z1)
# # Opperator
# มี + - * / % ปกติ แต่ ยกกำลังเป็น ** เช่น 2ยกกำลัง5 คือ 2**5
# round() -  ปัดเศษ 
# 1. เครื่องหมาย = คือการกำหนดค่า
# 2. เครื่องหมาย == คือการเช็คค่าว่าเท่ากันหรือไม่

y = 2**4
print(y)

