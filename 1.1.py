''''''' W.A.P in python to calculate the sum of three given numbers,if the values are equal then return three times of their sum.'''''''
a=int(input("enter the first numbers="))
b=int(input("enter the second numbers="))
c=int(input("enter the third numbers="))
sum=(a+b+c)
if a==b==c:
    print(sum*3)
else:
    print(sum)