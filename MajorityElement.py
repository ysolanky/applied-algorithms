# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 13:58:54 2021

@author: yashp

"""
class MajorityElement:
    def majority(self, A):
        left = 0
        right = len(A)
        return (self.helper(A,left,right))
    
    def helper(self,a, left, right):
        if len(a) == 1:
            return a[0]
        if left == right:
            return -1
        if left + 1 == right:
            return a[left]
        mid = (left+right)//2
        m = self.helper(a, left, mid)
        n = self.helper(a, mid, right)
        count1 = 0
        for i in range(left, right):
            if a[i] == m:
                count1 += 1
            if count1 > (right-left)//2:
                return m
        count2 = 0
        for i in range(left, right):
            if a[i] == n:
                count2 += 1
            if count2 > (right-left)//2:
                return n

        return -1
