import sys
import time
import random
import math
import numpy
# -*- coding: utf-8 -*-
'''
index data0 data1 ...
structure of data.txt must be :
0     1.5   3.6   1.8
1     2.8   7.4   5.5
'''
class Kmeans:
    def __init__(self, filename, k, dim, data_num , iteration,rounds):
        self.__filename = filename
        self.__k = k
        self.__dim = dim
        self.__data_num = data_num
        self.iteration = iteration
        self.rounds = rounds
        self.__data = numpy.zeros( [ self.__data_num , self.__dim])
        self.__mean = []# position of k means(center)
        self.__trend = [ 0.0 for x in range(iteration) ]
        self.__solution = [0 for x in range(data_num)]
        for i in range(self.__k):
            self.__mean.append([0.0] * self.__dim)
       
        self.__SSE = 0.0
    def __read(self):
        F = open(self.__filename, mode='r')
        
        for j in range(self.__data_num):
            t = F.readline()
            if t == '':
                break
            now = t.split(",")
            if 'M' in now[0]:
                now[0] = '0'
            elif 'F' in now[0]:
                now[0] = "0.5"
            elif 'I' in now[0]:
                now[0] = '1'
            
            for x in range(0 , self.__dim ):
                self.__data[j][x] = float(now[x])
                
        F.close()
        if self.__filename == "abalone.data" :
            # data pre-processing
            data_max = numpy.amax(self.__data,0)
            data_min = numpy.amin(self.__data,0)
            
            for i in range(self.__data_num):
                for j in range(self.__dim):
                    self.__data[i][j] =( (  self.__data[i][j] - data_min[j] ) / (data_max[j]-data_min[j]) )
    def run(self):
        self.__read()   
        
        for x in range(self.rounds):         
            print("round: "+str(x)+" ...")
            for i in range(self.__data_num): #first random group 0~k
                self.__solution[i] = random.randint(0 , self.__k-1)
            for i in range(self.iteration):
                self.__find_center()
                self.__SSE=self.__sse()
                self.__trend[i] += self.__SSE 
                self.__update()
        for i in range(self.iteration):
            self.__trend[i] /= self.rounds
            print(self.__trend[i])
        self.write_file()
        
    def show_data(self):
        for i in range(self.__data_num):
            for j in range(self.__dim):
                print(self.__data[i][j] , end=" ")
            print()

    def __find_center(self):
        for i in range(self.__k):
            for j in range(self.__dim):
                self.__mean[i][j] = 0
        
        group_num = [ 0 for x in range(self.__k)]#restore num of each group
        
        for i in range(self.__data_num):
            group_num[ self.__solution[i] ] += 1

            for j in range(self.__dim):
                self.__mean[self.__solution[i] ][j] += ( self.__data[i,j] )

        for i in range(self.__k):
            if group_num[i] == 0 :  continue
            for j in range(self.__dim):
                self.__mean[i][j] /= (group_num[i])
        
        
    def __update(self):  
        dis = [ [0.0] for x in range(self.__k)]#store distance from each mean
        for i in range(self.__data_num):
            for j in range(self.__k):
                dis[j] = self.__count_length(self.__data[i],self.__mean[j] , 1) 
            self.__solution[i] = dis.index( min(dis) )

    def __count_length(self,arr=[],mean=[],mode = 0):
        length = 0.0 
        temp = 0.0
        for i in range(self.__dim):
            temp += ( (arr[i]-mean[i])**2 )
        if mode == 0 :
            length = math.sqrt(temp)
            return length
        else :
            return temp
    
    def __sse(self):
        temp = 0.0
        for i in range(self.__data_num):
            temp += self.__count_length( self.__data[i] , self.__mean[ self.__solution[i] ]  , 1)

        return temp
    def write_file(self):
        
        f = open("result.txt",mode = 'w')
        f.write("data: "+self.__filename+"\n")
        f.write("k: "+str(self.__k)+"\n")
        f.write("dim: "+str(self.__dim)+"\n")
        f.write("iter: "+str(self.iteration)+"\n")
        f.write("rounds: "+str(self.rounds)+"\n")
        f.write("datanum: "+str(self.__data_num)+"\n"+"\n")
        for i in range(self.iteration):
            f.write(str(i)+": "+str(self.__trend[i])+"\n")
        f.close()
        