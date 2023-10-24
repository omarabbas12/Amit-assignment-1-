#!/usr/bin/env python
# coding: utf-8

# In[81]:


#1
class Rectangle:
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def perimeter(self):
        per=2*self.l+2*self.w
        return per
    def area(self):
        return self.l*self.w
    def display(self):
        return self.l,self.w , Rectangle.perimeter(self),Rectangle.area(self)

class Parallelepipede(Rectangle):
    def __init__(self,l,w,v):
        super().__init__( l, w)
        self.v=v
    def Volume(self):
        return self.l * self.w * self.v
    
r1=Rectangle(5,125)
p1=Parallelepipede(5,2,3)
p1.Volume()


# In[1]:


#2
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        return self.name , self.age
    
class Student(Person):
    def __init__(self,name,age,section):
        super().__init__(name,age)
        self.section=section
    def displaystudent(self):
        return self.name,self.age,self.section
p1=Person("omar",15)
s1=Student("mo",20,5)
s1.displaystudent()


# In[11]:


#3
import math
class Computation:
    def __init__(self):
        pass
    def factorial(self,n):
        return math.factorial(n)
    def Sum(self,n):
        sum=0
        for i in range(1,n+1):
            if(i!=n+1):
                sum=sum+i
        return sum
    def testPrim(self,n):
        j=0
        for i in range (1, n + 1):
            if (n% i == 0):
                j = j + 1
            if (j == 2):
                return True
            else:
                return False
    def testPrims(self):
        pass
    def tableMult(self,n):
        for i in range(0,10):
            print (i*n)
    def alltableMult(self):
        for i in range(0,10):
            print("table",i)
            for j in range(0,10):
                print(i*j)
    def listDiv(self,n):
        mylist=[]
        for i in range(1,n):
            if n%i==0:
                mylist.append(i)
        print(mylist)
    def listDivPrim(self,n):
        mylist=[]
        for i in range(1,n):
            if n%i==0 and self.testPrim(i):
                mylist.append(i)
        return mylist
        


# In[12]:


c1=Computation()
c1.listDivPrim(14)


# In[21]:


#4
x="hello my name is omar"
y="hello my name is mohamed"
count=0
for i in range(min(len(x),len(y))):
    if x[i]==y[i]:
        print(x[i])


# In[ ]:




