numbers = input("Enter the numbers").split(" ")
for i in range(len(numbers) - 1):
    for j in range(i + 1, len(numbers) ):
        if (int(numbers[i]) > int(numbers[j])):
            num = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = num 
print(f"{numbers}")