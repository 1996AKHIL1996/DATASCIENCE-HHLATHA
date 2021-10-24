# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 19:01:23 2021

@author: Akhil
"""

import pandas as pd
print(pd.__version__)

import pydataset

from pydataset import data
data('')
mt =data('mtcars')
type(mt)
mt

mt.to_csv('mtcars.csv')#conversion to csv

mt.to_csv('C:\\Users\\Akhil\\Documents\\GitHub\\mtcars.csv')

mt.head()

mt.tail(2)
 
import pandas as pd
adv =pd.read_csv('C:\\Users\\Akhil\\Documents\\GitHub\\DATASCIENCE-HH\\advertising.csv')
adv
ps1 =pd.Series([1,2,3,4,5])

ps1
ps1.values
ps1.index

a1 =adv.iloc[0:10]

a2 =adv.iloc[30:40]

a3 =pd.concat([a1,a2])
a3

a3.shape

a3.shape[1]#gives number of columns

ps2 =pd.Series(range(0,a3.shape[0]))
ps2


ps3 =pd.Series([1,2,33,44,55],index =['a','b','c','d','e'])
ps3
ps3['a']
ps3['a':'c']

ps3 =pd.Series([1,2,3,4,5],index=['a','b','b','c','d'])
ps3['b']
ps3.loc['b']
ps3.iloc[3]

import numpy as np

ps4 =pd.Series(np.random.randint(100,200,size=10))
ps4
ps4[ps4>150]

ps4[(ps4>150)&(ps4<180)]

import pandas as pd

course =pd.Series(['MBA','B.TECH','BBA','DOCTOR'])
strength =pd.Series([10,20,54,23])

fees =pd.Series([100,200,800,600])

d1 ={'course':course,'strength':strength,'fees':fees}
df1 =pd.DataFrame(d1)

df1

df1.iloc[0:2]

df1['course']

df1[['course','strength']]

df1

df1.count()
adv.columns

df1.describe()

df1.dtypes

df1[df1['course']=='BBA']

df1
df1.drop(3)
df2 =df1.drop('fees',axis=1)
df2


df1[df1['course']=='B.TECH']
df1[df1['course']=='B.TECH'].index
df1.drop(df1[df1['course']=='B.TECH'].index)


df1
df1.sum()
df1.max()
df1.std()
df1.mean()
df1.median()
df1.dtypes

df1 
placed =([None,np.nan ,100,None])
df1['placed']=placed

df1

df1.isnull()
df1.notnull()

df1.describe()

df1.count()
df1.dropna()
df1.dropna(axis =1)


adv =pd.read_csv('advertising.csv')
adv

adv.describe()

n1 =adv.isnull().values#nan values at each column
n1

sum(n1)

adv[adv['TV']==np.nan]
adv.isnull().index



adv[adv['TV'].isnull()].index.tolist()
len(adv[adv['TV'].isnull()].index.tolist())


adv.dropna(axis='rows')
adv.dropna(axis ='columns')
adv.dropna(axis ='columns',how ='all')
adv.dropna(axis ='columns',how ='any')

df1


pd4 =pd.DataFrame([['ak',50,'M',1000,None],['mk',None,"F",'None',1000]])
pd4
pd4.dropna(thresh=np.nan)

import numpy as np
ps4 =[None,np.nan,None,np.nan,np.nan]

ps4 =pd.Series([100,200,None,400,None,None,700])
ps4

ps4.fillna(method='ffill')

ps4
ps4.fillna(method ='bfill')
import pandas as pd

#if first value is NaN dont use forward fill
#lastvalue is NaN dont use backward fill
pd.concat([df1,df2])

grades1 ={'subject1':[1,2,3,4],'subject2':[2,3,4,5]}
f1=pd.DataFrame(grades1)
f1
grades2 ={'subject3':[4,3,5,6],'subject4':[7,4,5,6]}
f2 =pd.DataFrame(grades2)
f2
f3 =pd.concat([f1,f2],axis=1)
f3

#join 
pd.concat([f1,f2])

pd.concat([f1,f3])
pd.concat([f1,f2],axis =0)
pd.concat([f1,f2],axis=1)
pd.concat([f1,f3],axis=1)

pd.concat([f1,f2],ignore_index=True)
'''
df =pd.concat([f1,f2],keys =['x','y'])#adding keys to the table
df.index.levels[0]

df =pd.concat([f1,f2],keys=['x','y'],axis =0)
pd'''
#f1['subject1']='chutiya'
f1
f1

f1.iloc[:,:-1]
f1['subject1']
import pandas as pd

f1=df.rename(columns ={'subject1':'abc'})
f1
df1 =pd.concat([f1,f2],axis =1)
import pandas as pd

rollno =pd.Series(range(1,11))
name =[]
for i in range(1,11):
    name.append('student'+str(i))
name

name =['student'+str(i) for i in range(1,11)]
name

gender =['M','F']
import numpy as np
gender =np.random.choice(a =gender,size =10)
gender
mark1 =np.random.randint(0,100,size =10)
mark1

mark2 =np.random.randint(0,100,size =10)
mark2

pd5 =pd.DataFrame({'rolno':rollno,'name':name,
                   'gender':gender,'mark1':mark1,
                   'mark2':mark2})
pd5

pd5.to_csv('random_data1.csv',index =False)

course =np.random.choice(a =['BBA','MBA','B.tech'],size=10)
course
pd6 =pd.DataFrame({'rollno':rollno,
                   'course':course,
                   'mark1':mark1
                   ,'mark2':mark2
                   ,'gender':gender})

#fees =pd6.DataFrame
pd6 = pd.DataFrame({'rollno':rollno, 
                    'course':course,
                    'marks2':mark2})
pd6
fees = pd.DataFrame({'course':['BBA','MBA','BTECH', 'MTECH'],
                     'fees':[100000, 200000, 150000, 220000]})
fees
pd5
pd6
fees

pd7 =pd.merge(pd5,pd6)
pd7
#to merge the columns in two tables with commmon columns

pd8 =pd.merge(pd7,fees)
















