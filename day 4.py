# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 19:01:53 2021

@author: Akhil
"""

import numpy as np
np.array([1,2,3,4])

np.random.randint(0,100)

n1 =np.random.randint(0,100,size =5)
n1

type(n1)

n1.shape

x2 = np.random.randint(0,10,size =(2,3));x2

type(x2)

x3 =np.random.randint(0,10,size=(3,2,2));x3

np.ndim(x3)

x3.shape

#indexed

x1 =np.random.randint(0,100,size =10);x1
x1[-3]

x1[2:]


x2 =np.random.randint(0,10,size=(3,4))
x2
x2[1][2]

x2[0,:]#row fetching

x2[:,0]#column fetching

x2[:,:3]

x2[:2,:]

x2[:2,:2]

x2[-2:,-2:]# fetcing last two rows and columns

#3-dimensional array

x3 =np.random.randint(0,10,size=(3,3,4));x3
x3[0,:, :]

x3[1,-2:,-2:]

x4 =np.arange(20)
x4

x4.shape

x4.reshape(4,5)

x4.reshape(2,2,5)

x5=x4.reshape(-1,2)

type(x5)

x5.shape

a =np.zeros((2,4),dtype =int)
a

c =np.ones((2,4),dtype =int)
c

l1 =[]
l1.append([1,2])
l1


np.empty((2,4))

np.eye(3,3)

np.linspace(0,10,num =4)

#statistical operations

n1 =np.random.randint(0,100,size=10)
np.max(n1)
np.min(n1)
np.std(n1)
np.mean(n1)

n2 =np.random.randint(0,10000,size =100)
len(n2)
np.max(n2)
np.std(n2)

np.floor([1.2,1.3])

np.ceil([1.2,1.4])

np.ceil([-2.3,-1.3])

np.round([1.2,1.5])

np.trunc([1.2,1.6])
np.trunc([-1.2,-1.6])

np.trunc([-1.2,-1.6])
np.floor([-1.2,-1.6])

np.round([1.2345,3.4567422],3)


#concatination

n1 =np.random.randint(0,10,size =(3,4))

n2 =np.random.randint(0,10,size=(3,4))

n3 =np.concatenate([n1,n2],axis =0)
np.concatenate([n1,n2],axis =1)


np.split(n3,2,axis=1)


n1
n2
np.stack((n1,n2))

upper,lower =np.vsplit(n3,[2])
upper
lower

left,right =np.hsplit(n3,[3])
left
right

n3.min()
n3.max()


n3.min(axis=0)
n3
n3.max(axis =1)

np.median(n3)
np.sum(n3,axis =1)

np.equal(n3,4)

np.sum(np.equal(n3,4))
#it shows how many fours

np.greater(n3,4)

np.less(n3,4)
np.less_equal(n3,4)

n3<4


np.sort(n3)

n3

np.sort(n3,axis=0)

import matplotlib.pyplot as plt


n4 =np.random.normal(100,10,size =1000)#mean,standard deviation
n4
plt.hist(n4)

np.median(n4)
np.std(n4)



































