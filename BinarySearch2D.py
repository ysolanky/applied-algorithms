# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 20:10:57 2021

@author: yashp
"""
class BinarySearch2D:
    def search(self, M: [[int]], q: int) -> [int, int]:
        if len(M) == 0:
            return [-1,-1]
        row_len = len(M)
        col_len = len(M[0])
    
        low = 0
        high = row_len * col_len
    
        while low < high:
            mid = (low + high) // 2
            if M[mid // col_len][mid % col_len] == q:
                return [(mid // col_len),(mid % col_len)]
            elif M[mid // col_len][mid % col_len] < q:
                low = mid + 1
            elif M[mid // col_len][mid % col_len] > q:
                high = mid
        else:
            return [-1,-1]