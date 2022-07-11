#removing characters in the sring value:
characters1=input("please enter the sentence:")
n=int(input("enter the number of characters to be removed:"))
characters2=characters1.replace(characters1[0:n],"")
print(characters2)