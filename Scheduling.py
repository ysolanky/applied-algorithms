# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 22:39:55 2021

@author: yashp
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 16:09:59 2021

@author: yashp
"""
class Scheduling:
    def schedule(self, A : [[int]]) -> int:
        A.sort(key = lambda x : x[1])
        print(A)
        count1 = 1
        start_prev = A[0][0]
        end_prev = A[0][1]
        
        for i in range(1,len(A)):
            next_job_start = A[i][0]
            next_job_end = A[i][1]
            if next_job_start > next_job_end:
                continue
            if end_prev <= next_job_start  and start_prev < end_prev:
                start_prev = A[i][0]
                end_prev = A[i][1]
                count1 = count1+1
            if start_prev > end_prev:
                if next_job_start >= end_prev and next_job_end <= start_prev:
                    count1 = count1+1
                    start_prev = start_prev
                    end_prev = A[i][1]
        return count1

#A = [[64800,21600], [75600,14400], [10800,50400], [46800, 68400]]                    
A = [[1,2],[3,5],[7,9],[9,11],[1,2],[3,2],[1,2]]
print(Scheduling().schedule(A))
