def find_even_digit_numbers():
    even_numbers = []
    for num in range(1000, 3001):
        if all(int(digit) % 2 == 0 for digit in str(num)):
            even_numbers.append(str(num))
    print(", ".join(even_numbers))

# Run the function
find_even_digit_numbers()