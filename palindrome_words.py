a=input().strip().replace(".","").replace(","," ").lower().split(" ")

for i in range(len(a)):
    j=a[i][::-1]
    if(a[i]==j):
        print(a[i])
