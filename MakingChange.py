# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 13:54:05 2021

@author: yashp
"""

class MakingChange:
    def minimumCoins(self, money, coins):
        if money == 0 or coins ==0:
            return 0
        total = [money+1] * (money + 1)
        total[0]= 0
        print(total)
        
        for j in range (len(coins)):
            for i in range(1, money+1):
                coin = coins[j]
                if i >= coin:
                    total[i] = min(total[i],total[i-coin]+1)
        print(total)
        return -1 if total[money] == money+1 else total[money]
    
A = 7
B = [3,5]
print(MakingChange().minimumCoins(A, B))