# -*- coding: utf-8 -*-
"""data structures(tuple,list)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TUV_4JKMzv0wqRwYSUnnldEH87eRstca
"""

# tuple and its methods
x=tuple((11,22,33,44,55,"no","true","false",1.1,2.2,3.3))
y=["asdf","lkj","qwert","poiuy"]

x[0]
y[1]

for i in x:
  if type(i)== int or type(i)==float:
    print(i,"is a decimal")
  elif type(i)==str:
    print(i,"is a string")

x.count(22)

x.index(1.1)

# list and its methods
a=list(("police","criminal","judge","lawyer",201,306,9.99))
b=["tiny tots","elementary","middle","high"]

a.append(1234567890)

a

a.insert(4,"jailor")

a

a.pop()

a

a.remove(9.99)

a

a.extend(b)

a

a.clear()

b.clear()

