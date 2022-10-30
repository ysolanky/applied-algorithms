# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 13:44:43 2021

@author: yashp
"""
class BinarySearch:
    
    def search(self, A, key):
        return BinarySearch().binarySearchHelper(key, A, 0, len(A)-1)
    
    def binarySearchHelper(self,key,A,start,end):
        if start>end:
            return -1
        mid=(start + end) // 2
        if key == A[mid]:
            return mid
        elif key > A[mid]:
            return self.binarySearchHelper(key, A, mid+1, end)
        else:
            return self.binarySearchHelper(key, A, start, mid -1)

 