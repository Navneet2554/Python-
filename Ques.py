# Program to find the sum of  multiple  numbers
def find_sum(*num):
    result = 0

    for i in num:
        result = result + i
        
    print("sum :",result)

find_sum(1,2,3,4,5)  