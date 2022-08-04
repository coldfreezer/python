num = input("Enter the number/string to check whether it is palindrome: ")
if num == num[::-1]:
    print("Number is Palindrome")
else:
    print("Number is Not Palindrome")
