n=int(input())
a=[]
for i in range(n):
    m=int(input())
    a.append(m)
print(a)
for i in range(n):
    if(i%2==0):
        print(a[i],end=" ")

