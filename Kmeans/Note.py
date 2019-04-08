import sys
import time
import random
import math

'''
import from Kmeans import Kmeans

def out():
	print("out!")

name = "Peter"
age = 32
print("Hello Im",name, " , " , age ,"years old")
array = [15,5,9]
print(array[2])
print(type(age) , type(name))


arr = [x for x in range(10) if x % 3 == 0]

for i in range(0,10,int(sys.argv[1])):
    print(i)

for i in arr :
    print(i)

y = [0 for x in range(5)] # 1D array initialization
for i in range( len(y) ) :print(y[i])

arr1 = []
s = time.time()# count time
for i in range(int(1e+6)):
    arr1.append(i)
print('took {} secs'.format(round(time.time() - s, 3)))

s = time.time()
arr2 = [i for i in range(int(1e+6))]
print('took {} secs'.format(round(time.time() - s, 3)))

n = 3
m = 4
a = []
for i in range(n) : #initialization
    a.append([0] * m)
for row in a :
    for temp in row :
        print (temp , end=" ")
    print()

F = open( "iris.txt" , mode = 'r')
n = 150
m = 5
a = []

for i in range(n) : #initialization
    a.append([0.0] * m)
for j in range(n) :
    t = F.readline()
    if t=='': break
    now = t.split()
    for x in range(1,5) :
        a[j][x-1]=float(now[x])
F.close()



for i in range(n) :
    for j in range(m) :
        print(a[i][j],end =" ")
    print()

'''

class Ant:
    def __init__(self , index):
        self.index = index

ants = [ Ant(x) for x in range(10) ]
for ant in ants:
    print(ant.index , end=" ")
    