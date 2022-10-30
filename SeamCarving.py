# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 21:44:15 2021

@author: yashp
"""
class SeamCarving:
    def carve_seam(self, disruption: [[int]]) -> [int]:
        row = len(disruption)
        col = len(disruption[0])
        DP = DP = [[0 for x in range(col)] for x in range(row)]
        for i in range(0,row):
            for j in range(col):
                if i ==0:
                    DP[i][j] = disruption[i][j]
                if j == 0:
                    DP[i][j] = disruption[i][j] + min(DP[i-1][j],DP[i-1][j+1])
                elif j == col - 1:
                    DP[i][j] = disruption[i][j] + min(DP[i-1][j-1],DP[i-1][j])
                else:
                    DP[i][j] = disruption[i][j] + min(DP[i-1][j-1],DP[i-1][j],DP[i-1][j+1])
                    
        #print(DP)
        
        cost = [0] * row
        cost[row-1] = DP[row-1].index(min(DP[row-1]))

        for i in range(row-2, -1, -1):
            j = cost[i+1]
            if j == 0:
                if DP[i][j] < DP[i][j+1]:
                    cost[i] = j
                else:
                    cost[i] = j+1
            elif j == col - 1:
                if DP[i][j-1] < DP[i][j]:
                    cost[i] =  j-1
                else:
                    cost[i] =  j
            else:
                if DP[i][j-1]<= DP[i][j] and DP[i][j-1] <= DP[i][j+1]:
                    cost[i] =  j-1
                elif DP[i][j]<= DP[i][j-1] and  DP[i][j] <= DP[i][j+1]:
                    cost[i] =  j
                else:
                    cost[i] =  j+1
        return cost
   
#disruption = [[1,2,8,3],[4,2,1,0],[1,2,3,9],[3,2,0,3]]

#print(SeamCarving().carve_seam(disruption))
