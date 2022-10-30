# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 13:58:54 2021

@author: yashp
"""

def Abc(A):
    for i in range(0,len(A)):
        count1 = 0
        for j in range(0,len(A)):
            if A[i] == A[j]:
                count1 = count1 +1
                #print(count1)
        if count1 > len(A)/2:
            print("majority element is", A[i])
            break
                    
#A = [2,2,3,3,3,5,5,5,5,5,5]
#Abc(A)