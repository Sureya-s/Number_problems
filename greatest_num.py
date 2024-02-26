num = list(input("Enter the 3 digit number").split(" "))
greatest_num=int(num[0])
for i in range(len(num)):
    i = int(num [i])
    if (i > greatest_num):
        greatest_num = i
print(f"The greatest value among the given 3 numbers is {greatest_num}")