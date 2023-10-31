def linear(arr,key):
    for i in arr:
        if(i==key):
            return i
    return -1

arr=[]
n=int(input("Enter the number of elements:"))
for i in range(0,n):
    temp=int(input("Enter the element:"))
    arr.append(temp)
key=int(input("enter the key:"))    
index=linear(arr,key)
if (index == -1):
    print("elkement not found")
else:
    print("the element is present at index ",index)