s = input('Enter the input number elements: ')
l1 = s.split()
for i in range(len(l1)):
    l1[i] = int(l1[i])
flag= l1[0]
l1[0]=l1[len(l1)-1]
l1[len(lt1)-1]=flag
print(l1)