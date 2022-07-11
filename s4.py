#Write a program to find how many times substring “Hi” appears in the given string.
str1=input("enter your string: ")
n=0
for i in range(len(str1)-1):
    if "Hi"==str1[i:i+2]:
        n=n+1
print(n)