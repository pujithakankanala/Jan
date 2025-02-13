# Function to find factors and their even/odd status 
def find_factors_and_even_odd(n): 
    print(f"Factors of {n} and their even/odd status:") 
    for i in range(1, n + 1): 
        if n % i == 0:  # Check if i is a factor of n 
            if i % 2 == 0:  # Check if the factor is even 
                print(f"{i} is a factor and it is even.") 
            else:  # If it's not even, it must be odd 
                print(f"{i} is a factor and it is odd.") 
 
 
number = int(input("Enter a number: ")) 
res=find_factors_and_even_odd(number) 
