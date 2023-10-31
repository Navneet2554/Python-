''''' Perform recusive Binary Search on a given set of element and determine the time required to perform the same.
Plot  a graph of number of element verus time taken.Specify the time efficency class of this algorithm'''''
def bs(arr,low,high,x):
    if(high>=low):
        mid = high +low/2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return bs(arr,low,mid-1,x)
        elif arr[mid<x]:
            return bs(arr,mid+1,high,x)
    else:
        return -1
arr=[]
n=int(input("Enter size:"))
count=0
while(count !=n):
    num=int(input("enter any number:"))
    arr.append(num)
    count+=1
x=int(input("enter any number to serach :"))
result=bs(arr,0,len(arr)-1,x)
if result!=-1:
    print("Element is present at index",str(result))
else:
    print("Element is not present")