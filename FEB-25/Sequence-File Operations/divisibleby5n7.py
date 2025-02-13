import random
numbers=[x for x in range(1,1001) if x % 5 ==0 and x % 7 == 0]
random_numbers = random.sample(numbers,5)
print ("random numbers which are divisible by 5 and 7:", random_numbers)