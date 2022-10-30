class MergeSort:
    def merge(self, A, p, q, r):
        n = A[p:q+1]
        m = A[q+1:r+1]
        i = j = 0
        k = p
        
        while (i < len(n) and j< len(m)):
            if n[i] < m[j]:
                A[k] = n[i]
                i = i+1
            else:
                A[k]= m[j]
                j = j+1
            k = k+1
        
        while(i < len(n)):
            A[k] = n[i]
            i= i+1
            k=k+1
            
        while(j < len(m)):
            A[k] = m[j]
            j= j+1
            k=k+1
        
    def sort(self, A, p, r):
        if p<r:
            q = (p + r)//2
            self.sort(A,p,q)
            self.sort(A,q+1,r)
            self.merge(A,p,q,r)

A = [54,26,93,17,77,31,44,55,20]            
print(MergeSort().sort(A,0,len(A)))
print(A)
            