#Print the following pattern
n=int(input("enter: "))
for i in range(n):
    for j in range(i+1):
        print(i+1,end=" ")
    print()