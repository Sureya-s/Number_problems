n=int(input())
a=[]
encountered=set()
for i in range(n):
    m=int(input())
    a.append(m)
print(a)
for i in range(n):
    count=0
    for j in range(n):
        if a[i] not in encountered:
            if(a[i]==a[j]):
                count+=1
    if a[i] not in encountered:
        print(f'the frequency of {a[i]} in the list {count}')
        encountered.add(a[i])
            
        
