class Fibonacci:
    def fibonacci(self, n : int) -> int:
        a=0
        b=1
        if n<0:
            print("Invalid")
        elif n==0:
            return 0
        elif n==1:
            return 1
        else:
            #return self.fibonacci(n-1) + self.fibonacci(n-2)
            for i in range (1,n):
                c = a+b
                a = b
                b = c
            return b 