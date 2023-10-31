#function with complete statement

#Python function Arguments
def add(a,b):
    return a + b
sum = add(2,3)
print(sum)

#Function Argument with default Values
def add(a=5,b=4):
   sum = a + b
   print("sum:",sum)
add(a=2)

#Pyhton Keyword Arguments
def display_info(first_name,last_name):
    print("first name :",first_name)
    print("Last name :",last_name)
display_info("Ram","Kumar")
