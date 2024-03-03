a=[]
n=int(input())
sum=0
for i in range(n):
    s=int(input())
    a.append(s)
    if(s%2==0):
        sum+=s
print(a)
print(sum)
