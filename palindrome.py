name = input("Enter a name:").lower()
reverse = name[::-1]
if name == reverse:
    print("Yah,  It's a Palindrome")
else:
    print("It's  not a Palindrome")
