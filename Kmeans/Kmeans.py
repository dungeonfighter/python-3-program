import sys
import time
import random
import math
# -*- coding: utf-8 -*-
'''
index data0 data1 ...
structure of data.txt must be :
0     1.5   3.6   1.8
1     2.8   7.4   5.5
'''
class Kmeans:
    def __init__(self, filename, k, dim, data_num , iteration):
        self.__filename = filename
        self.__k = k
        self.__dim = dim
        self.__data_num = data_num
        self.iteration = iteration
        self.__data = []
        self.__distance = []
        self.__mean = []# position of k means(center)
        for i in range(self.__k):
            self.__mean.append([0.0] * self.__dim)
        for i in range(data_num):  # initialization 2D array
            self.__data.append([0.0] * (dim+1))  # [data1][data2][group]
            self.__distance.append([0.0] * (data_num))
        self.__SSE = 0
    def __read(self):
        F = open(self.__filename, mode='r')
        for j in range(self.__data_num):
            t = F.readline()
            if t == '':
                break
            now = t.split()
            for x in range(1 , self.__dim + 1): # 0 is index of data , 1~dim+1 are data
                self.__data[j][x-1] = float(now[x])
        F.close()

    def run(self):
        self.__read()
        self.__create_distance_table()
        for i in range(self.__data_num): #first random group 0~k
            self.__data[i][self.__dim] = random.randint(0 , self.__k-1)
        for i in range(self.iteration):
            self.__find_center()
            print(self.__SSE)
            self.__update()
            
             
    def show_data(self):
        for i in range(self.__data_num):
            for j in range(self.__dim):
                print(self.__data[i][j] , end=" ")
            print()

    def __create_distance_table(self):
        for i in range(self.__data_num-1):#each point
            for j in range(i+1 ,self.__data_num):
                temp = 0.0
                for k in range(self.__dim):
                    temp += ( (self.__data[i][k]-self.__data[j][k])**2 ) # sum of square for all dim  
                self.__distance[i][j] = self.__distance[j][i] = math.sqrt(temp) #sqrt
    
    def __find_center(self):
        for i in range(self.__k):
            for j in range(self.__dim):
                self.__mean[i][j] = 0
        group_num = [ 0 for x in range(self.__k)]#restore num of each group
        for i in range(self.__data_num):
            group_num[ int(self.__data[i][self.__dim]) ] += 1 
        for i in range(self.__data_num):
            for j in range(self.__dim):
                self.__mean[ int(self.__data[i][self.__dim]) ][j]+= ( self.__data[i][j]/float(group_num[ int(self.__data[i][self.__dim]) ]) )
        self.__SSE=self.__sse()
        
    def __update(self):  
        dis = [ [0.0] for x in range(self.__k)]#store distance from each mean
        for i in range(self.__data_num):
            for j in range(self.__k):
                dis[j] = self.__count_length(self.__data[i],self.__mean[j]) 
            self.__data[i][self.__dim] = dis.index( min(dis) )

    def __count_length(self,arr=[],mean=[],mode = 0):
        length = 0.0 
        temp = 0.0
        for i in range(self.__dim):
            temp += ( (arr[i]-mean[i])**2 )
        if mode ==0 :
            length = math.sqrt(temp)
            return length
        else :
            return temp
    
    def __sse(self):
        temp = 0.0
        for i in range(self.__data_num):
            temp += self.__count_length( self.__data[i] , self.__mean[ int(self.__data[i][ self.__dim ]) ]  , 1)
        return temp
