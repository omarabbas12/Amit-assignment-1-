#!/usr/bin/env python
# coding: utf-8

# In[4]:


#1
def fib(n1,n2):
    sum=n1+n2
    print(sum)
    if sum != 1346269:
        fib(n1=n2,n2=sum)
    else:
        return 1
    
        
fib(0,1)


# In[5]:


#2
mylist=["hello omar", "hello omar","hello boody","hello omar"]
#x=mylist[0].split(" ")
#print(x[1])
count=0
for i in range(len(mylist)):
    x=mylist[i].split(" ")
    for j in range(len(x)):
        if(x[j]=="omar"):
            count+=1
freq=float(len(mylist))/float(count)
freq


# In[6]:


#3
mylist=[1,2,3,4,5,6]
x=int(input())
for i in range(len(mylist)):
    for j in  range(len(mylist)):
        if(mylist[i]+mylist[j]==x):
            print(mylist[i],mylist[j])


# In[7]:


#4
mylist=[1,600,15,50,4,5,61]
y=list(set(mylist))
print(y[len(mylist)-1],y[len(mylist)-2])


# In[8]:


#5
def check(num):
    count=0
    for i in range(1,100):
        
        if num % i ==0 :
            count=count+1
    
    
    if(count==2):
        return "prime"
    
check(9)


# In[11]:


#6
def even(mylist):
    
    for i in range(len(mylist)):
        if(mylist[i]%2==0):
            print(mylist[i])
mylist=[1,2,3,4,5,6,7,8,9,12]
even(mylist)


# In[13]:


#7
def rev(x):

    z=x.split(" ")
    a=[]
    for i in reversed(range(len(z))):
        a.append(z[i])
    return a
x="hello my name is omar and i play mma"    
rev(x)


# In[29]:


#8
def check(x):
    
    if(x==x[::-1]):
        return "Palindrome"
    else:
        return "Not Palindrome"


# In[33]:


#9
x=input()
check(x)


# In[35]:


#10
def sqr():
    a=[]
    for i in range(0,15):
        a.append(i**2)
    return a
sqr()


# In[1]:


#11
import itertools
print(list(itertools.permutations(["A","B","C"])))


# In[16]:


#12
def test(a):
        def mult(b):
                return a*b
        return mult
func= test(10)
print(func(9))


# In[ ]:




