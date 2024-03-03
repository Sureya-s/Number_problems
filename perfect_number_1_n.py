n=int(input())
print(f"The perfect numbers between 1 to {n}")
for i in range(1,n+1):
    count=0
    for j in range(1,i):
        if(i%j==0):
            count+=j
    if(count==i):
        print(count,end=" ")
