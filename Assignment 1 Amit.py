#!/usr/bin/env python
# coding: utf-8

# In[6]:


#1
z=input()
mytuple=('5','6')
x=list(mytuple)
x.append(z)
y=tuple(x)
print(y)


# In[7]:


#2
mylist=[1,5,4]
sum=0
for i in range(len(mylist)):
        sum=sum+mylist[i]
print(sum)


# In[8]:


#3
mylist=[2,5,4]
sum=1
for i in range(len(mylist)):
        sum=sum*mylist[i]
print(sum)


# In[9]:


#4
mylist=[2,5,4,0,3]
print(min(mylist))
    


# In[10]:


#5
mylist=[2,5,4,0,3]
print(max(mylist))
    


# In[11]:


#6
mylist=["hello","hi","bro"]
print(len(mylist))


# In[12]:


#7
mylist=["hello","hi","bro"]
mylist1=[]
for i in range(len(mylist)):
    mylist1.append(mylist[i])
print(mylist1)


# In[13]:


#8

myset={1,2,3,4,5,6}
myset.remove(5)
print(myset)


# In[14]:


#9
setA={1,2,3,4,5}
setB={1,2,3,4,5,6,7}
setC={8}
bool(setA.issubset(setB))


# In[15]:


#10
myset={1,2,3,4,5,6}
myset.clear()


# In[16]:


#11
myset={1,2,3,4,5,6}
print(min(myset),"is the minimum")
print(max(myset),"is the max")


# In[17]:


#12
mytuple=(1,2,3,4,5)
mytuple.index(4)


# In[18]:


#13
mytuple=((2,"d"),(5,"3"),(1,"e"))
dict(mytuple)


# In[19]:


#14
mylist=[(1,2,3),(4,5,6),(7,8,9)]
for i in range(len(mylist)):
    x=list(mylist[i])
    print(x)

    
    


# In[20]:


#15
mytuple=(1,2,3,4,5,6,7)
x=list(mytuple)
x.reverse()
tuple(x)


# In[21]:


#16
mylist=[(1,"a"),(2,"b"),(3,"c")]
dict(mylist)


# In[22]:


#17
mylist=[(10, 20, 40,50), (40, 50, 60), (70, 80, 90)]
for i in range(len(mylist)):
    z=list(mylist[i])
    z.pop()
    z.insert(len(z),100)
    print(z)


# In[23]:


#18
mytuple=(0.2,0.5,0.4,0.8,0.3)
set(mytuple)

    


# In[ ]:




