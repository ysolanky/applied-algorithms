import random
class QuickSort:
    def randomp(self,A,p,r):
        x = random.randint(p, r)
        A[x],A[r] = A[r],A[x]
        return self.partition(A,p,r)
    
    def partition(self, A, p, r):
        x = A[r]
        i = p-1
        for j in range(p,r):
            if A[j]<= x:
                i = i+1
                A[i],A[j] = A[j],A[i]
        A[i+1],A[r] = A[r],A[i+1]
        return (i+1)

    def sort(self, A, p, r):
        r = r-1
        if p<r:
            q = self.randomp(A,p,r)
            self.sort(A,p,q)
            self.sort(A,q+1,r+1) 
            
A = [4,7,6,3,2,8,10,9,1]
print(QuickSort().sort(A,0,(len(A))))
print(A)