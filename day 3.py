# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 18:57:15 2021

@author: Akhil
"""

# conditional statements
'''
if (condition-->True):
    do task
elif True:
    do task
else:
    do this task

'''
marks =int(input('enter the mrks-->:'))

if (marks>90):
    print('A')
elif (marks>80 and marks<=90):
    print('B')
else:
    print('F')


#LOOPING STATEMENTS
print('x'*5)
name =[]
for i in list(range(0,3)):
    n=input('Enter name-->:')
    name.append(n)
print(name)

for i in list(range(0,10,2)):
    print(i)
    
for i in range(1,11):
    print('2*{0}={1}'.format(i,2*i))
    
for i in range(0,11):
    for j in range(0,11):
        print('{0}*{1}={2}'.format(i,j,i*j),end ='\n')
    print('\n')

l2 =['name','rno','branch']
data =l2.copy()

for j in range(1,3):
    l3 =[]
    for i in range(0,3):
        l3.append(input('Enter detail {}:'.format(l2[i])))
    data.append(l3)
    
data

#while(anyvalue other than zero will acts as true):

#BREAK
teamA =['India','Pakistan','SA','Australia']

for i in teamA:
    if i=='SA':
        print(i ,'in condition')
        break
    print(i, 'outer condition')
# here we wil skip the true condition and it will execute the rest

#if we dont use break we will get everything as outer condition 
#to be inn condition we use break








#         FUNCTIONS
a =10;b =20
def oper():
    print(a+b)
    print(a-b)

oper()
 

def printn(name):
    print('hello'+name)
    
printn('akhil')

def dat(name,rno,branch='None'):
    print(name,rno,branch)
    
a =dat('akhil',22,'AI')
a
#None shold be at last,if you place in middle ERROR

#return 
#--->we can store the value with return but not with print

def dat(name,rno,branch='None'):
    return name,rno,branch

a =dat('akhil',22,'AI')

a

def maxi(lst):
    m=0
    for i in lst:
        if (m<i):
            m=i
    return (m)
lst=[4,5,6,1]

maxi(lst)

lst.sort()
lst

l1=[]
data=[]
def dat1():
    l1.append(input('enter name:'))
    l1.append(int(input('enter no:')))
    l1.append(input('enter branch'))
    return l1

dat1()

for i in range(0,5):
    l1 =dat1()
    data.append(l1)


#lambda

def f(x):
    return x**2

f1 =lambda x:x**2 
f1(10)

fl1 = lambda x,y:x+y
fl1(2,3)

fl1 =lambda x,y:(x+y,x-y)
fl1(2,3)

#MAP ,Filter ,reduce

li =[2,3,4,5,6,9,7,7]

finallist =list(map(f1,li))
print(finallist)


finallist =list(filter(lambda x:(x==7),li))
print(finallist)


finallist =list(filter(lambda x:x%2==0 ,li))
print(finallist)

#reduce
from functools import reduce

li =[5,8,10,20,50,100]

s1 =reduce(lambda x,y:x+y, li)
print(s1)


import random as rd
x =rd.randint(1,1234)
x

li=[1,3,4,5,6]
rd.choice(li)

rd.choices(li,k=2)

gender =['m','f']
lst =rd.choices(gender,k =100)
lst
