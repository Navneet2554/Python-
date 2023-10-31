''''''' W.A.P in python to calculate the sum of the positive integers of n+(n-1)+(n-2)+...+0  '''''''
n=int(input("enter the number :"))
sum=0
for i in range(n,0,-1):
    sum=sum+i
print("sum =",sum)