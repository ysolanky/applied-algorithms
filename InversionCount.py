# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 14:35:43 2021

@author: yashp
"""

class InversionCount:
    def count(self, A: [int]) -> [int]:
        self.Acopy= A[0:]
        self.counts = [0] * len(A)
        self.sort(A, 0, len(A)-1)
        return self.counts
    
    def sort(self,A,p,r):
        if p<r:
            q = (p + r)//2
            self.sort(A,p,q)
            self.sort(A,q+1,r)
            self.merge(A,p,q,r)
            
    def merge(self, A, p, q, r):
        print(self.Acopy)
        L = A[p:q+1]
        print(L)
        R = A[q+1:r+1]
        print(R)
        i = len(L)-1 # indexing L
        j = len(R)-1 # indexing R
        for k in range(r,p-1,-1): 
            if (j < 0 or (i >= 0 and L[i] > R[j])):
                self.counts[self.Acopy.index(L[i])] += j+1
                A[k] = L[i]
                i = i-1
            else:
                A[k] = R[j]
                j = j-1
            print(self.counts)

        print(i, j)
        


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    '''    
        n = A[p:q+1]
        m = A[q+1:r+1]
        i = j = 0
        k = p
        C = [0] * len(A)
        use enumerate
        
        while (i < len(n) and j< len(m)):
            if n[i] < m[j]:
                A[k] = n[i]
                i = i+1
            else:
                A[k]= m[j]
                j = j+1
                C[k] =  a+1
            k = k+1
        
        while(i < len(n)):
            A[k] = n[i]
            i= i+1
            k=k+1
            
        while(j < len(m)):
            A[k] = m[j]
            j= j+1
            k=k+1
    '''    
        
'''class InversionCount:
    def count(self, A: [int]) -> [int]:
        C = [0] * len(A)
        for i in range(0,len(A)):
            for j in range(i +1,len(A)):
                if i < j and A[i] > A[j]:
                    C[i] = C[i] + 1
        return C
    ''''''
'''    

A = [6,4,2,1,3]
print(InversionCount().count(A))          