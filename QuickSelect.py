# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 20:16:25 2021

@author: yashp
"""

class QuickSelect:
    def select(self, A: [int], k: int) -> int:
        r = len(A)
        l = 0
        k=k+1
        return self.kthSmallest(A,l,r-1,k)
        
    def kthSmallest(self,A, l, r, k):
        if (k > 0 and k <= r - l + 1):
            index = self.partition(A, l, r)
            #print(index) 
            if (index - l == k - 1):
                return A[index]	
            if (index - l > k - 1):
                return self.kthSmallest(A, l, index - 1, k)
            return self.kthSmallest(A, index + 1, r, k - index + l - 1)
        else:
            return A[0]

    def partition(self, A: [int], lo: int, hi: int) -> int:
        x = A[hi]
        i = lo
        for j in range(lo,hi):
            if A[j]<= x:
                A[i],A[j] = A[j],A[i]
                i = i+1
        A[i],A[hi] = A[hi],A[i]
        #print(A)
        return (i)
    
#A = [5,3]            
#print(QuickSelect().select(A, 1))