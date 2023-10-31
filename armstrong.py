''''''' W.A.P in python to find Armstrong number '''''''
n=int(input("Enter the number:"))
sum=0
length = len(str(n))
temp=n
while temp>0:
    num=temp%10
    sum+=num**length
    temp=temp//10
if sum==n:
    print("Armstrong number")
else:
    print(" not a Armstrong ")