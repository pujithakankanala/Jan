'''def is_palindrome():
    num = input("Enter a number: ")
    if num == num[::-1]:
        print(f"{num} is a Palindrome number.")
    else:
        print(f"{num} is not a Palindrome number.")

# Run the function
is_palindrome()

'''

def is_palindrome():
    num = input("Enter a number: ")
    if str(num).casefold() == str(num)[::-1].casefold():
        print(f"{num} is a Palindrome number.")
    else:
        print(f"{num} is not a Palindrome number.")

# Run the function
is_palindrome()