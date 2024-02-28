num = int(input("Enter a Number"))
if num % 2 != 0:
    sum = 0
    for i in range(1, num+2, 2):
        sum += i
    print(sum)
else:
    print(f"{num} not a iron number")