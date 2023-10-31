#Error
#1)Syntax error 2)logical error 
#3)Run time error 
#Division by zero : Zero division error
try :
    numerator =10
    denominator = 0
    result = numerator/denominator

    print (result)
except :
    print("Error : Denominator should not be zero")

#Index Error : list index out of the range
try :
    list=[2,3,6,8]
    print(list[6])
except :
    print("Index out of the range")