n=int(input())
a=[]
encountered=set()
for i in range(n):
    m=int(input())
    a.append(m)
for i in range(n):
    count=0
    for j in range(n):
        if a[i] not in encountered:
           encountered.add(a[i])
print("Unique elements in an array:\n")
print(encountered)
            
        
