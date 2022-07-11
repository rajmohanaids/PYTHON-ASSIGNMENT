
s = input("Enter the elements coresponding:" )
l1 = s.split()
for i in range(len(l1)):
    l1[i] = int(l1[i])
t= [[0]*2]*len(l1)
for i in range(len(l1)):
    t[i][0]=l1[i]
    t[i][1]=l1[i]**3
    t[i]=tuple(t[i])
print(tuple(t))