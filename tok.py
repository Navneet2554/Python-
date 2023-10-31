""""  Tokenization
W.A.P to separte all the token in a given expression.The expression should be given at run time.
Token - collection of string(datatype,identifier). or the smallest individual elements in a program that is meaningful to the functioning of a compiler
"""
token=['+','-','/','*','=','!','^','%']
datatype=['int','float','char','double']
exp=input("enter any expression :")
token_sep=[]
exp_sep=[]
datatype_sep=[]
temp=" "
keys=exp.split()    #split-depend on space and ()
print(keys)
for elem in keys:
    if elem in datatype:
        datatype_sep.append(elem)   #append - last will add
    elif elem in token :
        token_sep.append(elem)
    else:
        exp_sep.append(elem) 
print("datatypes",datatype_sep)
print("token=",token_sep)           
print("identifiers=",exp_sep)