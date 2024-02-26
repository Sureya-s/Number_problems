num = list(input("Enter the 3 digit number").split(" "))
smallest_num=int(num[0])
for i in range(len(num)):
    i = int(num [i])
    if (i < smallest_num):
        smallest_num = i
print(f"The smallest value among the given 3 numbers is {smallest_num}")