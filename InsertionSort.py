# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 13:45:09 2021

@author: yashp
"""

class InsertionSort:
    def insertionsort(self, a):
        for j in range(1,len(a)):
            key = a[j]
            i = j-1
            while i>=0 and a[i]>key:
                a[i+1] = a[i]
                i=i-1
            a[i+1] = key
        return a
    
    
print(InsertionSort().insertionsort(a = [4,2,1,3]))