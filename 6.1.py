import time
n=int(input("Enter n for n*n matrix: "))
m1=[]
m2=[]
m3=[]
#Reading A
for i in range(n):
        temp=[]
        for j in range(n):
                temp_input=int(input("Enter element for first matrix:-"))
                temp.append(temp_input)
        m1.append(temp)
print("First matrix...........")
for i in range(n):
        for j in range(n):
                print(m1[i][j],end="\t")
        print("")
print("-------------------------------------------------------------------------------------")
#Reading B
for i in range(n):
        temp=[]
        for j in range(n):
                temp_input=int(input("Enter element for second matrix:- "))
                temp.append(temp_input)
        m2.append(temp)
print("Second matrix...........")
for i in range(n):
        for j in range(n):
                print(m2[i][j],end="\t")
        print("")
print("-------------------------------------------------------------------------------------")
#Naive approach
start=time.time()
for i in range(n):
        temp=[]
        for j in range(n):
                temp_val=0
                for k in range(n):
                        temp_val+=m1[i][k] * m2[k][j]
                temp.append(temp_val)
        m3.append(temp)
print("Resultant matrix...........")
for i in range(n):
        for j in range(n):
                print(m3[i][j],end="\t")
        print("")
end=time.time()
print("-------------------------------------------------------------------------------------")
print("Execution time=",end-start)

