''''''' W.A.P in pyhton to generate Fibonacci sequence using recursion '''''''
def recur_fibo(n):
    if n<=1:
        return n
    else:
        return(recur_fibo(n-1)+recur_fibo(n-2))
nterms =int(input("Enter any numbers="))
if nterms<=0:
    print("enter a positive number")
else:
    print("Fibonacci sequence :\n")
    for i in range(nterms):
            print(recur_fibo(i)) 