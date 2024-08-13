
#program to check if a string is a palindrome


str = input("Enter a string: ")

if str == str[::-1]:
    print("Palindrome.")
else:
    print("Not a Palindrome.")