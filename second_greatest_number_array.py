n=int(input())
a=[]
for i in range(n):
    m=int(input())
    a.append(m)
print(a)
for i in range(n):
    for j in range(i+1,n):
        if (a[i]<a[j]):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print(a)
print(a[1])
