#program to find the reciprocal of an even number 
try:
    num = int(input("enter a number :"))
    assert num%2 == 0   #asssert is a keyword which works as a If condition and we don't use ':'
except :
    print("Not an even number")
else :
    reciprocal = 1/num
    print(reciprocal)