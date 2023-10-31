''''''' W.A.P in python to find Anagram'''''''
def check(str1,str2):
    if(sorted(str1) == sorted(str2)):
        print("The string are Anagram")
    else:
        print("Not an Anagram")
str1 = input("Enter the string:")
str2 = input("Enter the string:")
str1 = str1.upper()
str2 = str2.upper()
check(str1,str2)