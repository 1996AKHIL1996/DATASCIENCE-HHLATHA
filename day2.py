# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 10:02:00 2021

@author: Akhil
"""

country ='india'
print(country)

a = 45

'''
other programming languages
int a ;
a =50 
'''

a =10
b=20
print('the value of a is',a,'and value of b is ',b)
print('the value of a is {} and b is {}'.format(a,b))

country =input('enter your name-->')
country

a =int(input('enter the number:'))
type(a)

#integer 2,3,65,100
#float 5.6 ,8.0001
#string 'akhil','bad2020'

f =3.5
f_i = int(f)
print(f_i)

print('print float'+str(f))
i_f =float(a)
print(i_f)
s ='marks 10'
print(int(s[6:]))

s ='10 '

print(float(s))

chr(100)
chr(64)

s ='a'
ord(s) #gives the value of ascii

ch =input('Enter a character:')
if (ord(ch)>=97 and ord(ch)<=122):
    print('ok')
else:
    print('not ok')
    
    
    
#MATHEMATICAL OPERATIONS ON BASIC DATA
x =13
print(x//2)

#BOOLEAN 

T =True
f =False

a =True
if (a ==True):
    print('OK')
    
a ==10
a>10
a>=23
a<34
a<=45
b =a!=34 # b = a not equal to 34

for i in range(1,100):
    print(i)
    
''' AND
X Y O
0 0 0
1 0 0
1 1 1'''

#Marks >75 and course ='HR'

'''
OR 
X Y O
0 0 0
0 1 1
1 0 1
1 1 1'''

#marks>75 or course ='hr'

'''NOT
x  O
0  1
1  0
 '''
a = False

print(not(a))

Fname ='vikas'
Lname ='kumar'
Lname =Fname +Lname

h ='hello'
w ='world'
h.capitalize()
h.upper()
    

h.ljust(10)

h.center(10)    

h ='java is an easy PL'
h.replace('java','python')

name =input('enter your name:-->')
print(name)    
    
name =name.strip()   
    
# list ,set,dictionary,tuple

#heterogeneous  (we can enter different datatypes
# in a data structure)

#ordered eg..set

#unique eg..set

#mutable (change is possible) Tupel is immutable


l1 =[1,2,3,4,5,6]# list
    # non ordered data type
    
print(l1)
    
l1[0]

r1 =list(range(1,101,5))
print(r1)
l3 =list(r1)

l4 =list(range(0,1000))

for i in l4:
    print(i)

#MUTABLE

l1[0] ='akhil'
l1    

l1.append('kumar')    
l1

l1.pop()
l1

l1.insert(1,34)
l1

l1.remove(34)

l1 =list(range(1,10000))
l1.reverse()
l1

l2 =[1,2,3,4,5,7,1,2,9,7,4]
l2.count(1)

l2.clear()
l2

del l2

l6 =list(range(100,120))

l6[0]

l6[0:6]

l6[:6]

l6[4:]

l6[-1]
l6[-5:-1]

fruits=['apple','banana','cherry']

for i in fruits:
    print(i)
x =iter(fruits)
x

next(x)
next(x)

#SET

# MUTABLE,ORDERED,HETEROGENEOUS,UNIQUE
S1 ={0,1,2,3,4,5,1,9,5}

S1

S1[1]#NOT INDEXED

S1.pop()
#set popping from beginning

S1.add(43)
S1

S1.add(6)
S1

S1.remove(6)
S1

S1.update([12,45,67])#adding multiple elements
S1

s2=S1.copy()

for i in s2:
    print(i)

x =iter(s2)
next(x)

#integer 4 bytes
l1 =list(range(1,100))
l2 =l1

l2[4]=6

l3 =l1.copy()
l1[2] =33
l3[3]=99


teamA ={'india','australia','pakistan'}
teamB ={'Bangladesh','india'}
teamA.union(teamB)
teamA.difference(teamB)#elements in team A which are not present in team B

#DICTIONARY

#Not indexed,#key:value pair,

d1 ={}
d1 ={'roll':2,'name':'vikas'}

car ={'brand':'honda','model':'jazz','year':2021}
car['brand']
#not indexed(we have to use key to fetch the value)
car.get('model')
car['colour']='black'

#mutable
car['colour']='red'
car.keys()
car.values()

for i in car.items():
    print(i)

car.pop('colour')

car.popitem()

car.clear()

del car    


#tuples 
#unmutable,collection,ordered,round brackets
t =()

t=(0,4,2,8,5)#not ordered

t[0]

t[0]=22#not mutable

t.count(8)
#heterogenous
t1 =('akhil',12,3.5,True)
t1[0]='reddy'




