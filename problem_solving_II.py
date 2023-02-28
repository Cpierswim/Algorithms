# -------------------------------------------------
# Problem Solving II
# -------------------------------------------------
# Deterimine if a number is a happy number
# If the sum of the squares of all the numbers in each place adds up to 1, then the number is happy
# If the sum of the squares is not 1, then we check and see if that number is happy
# If we already checked if a number is happy before, then the number is not happy
# So keep going through and checking numbers and we will either get a 1 (the number is happy)
# or we will have checked the number already, which means we would enter an endless loop, so it's sad
def is_number_happy(number_to_check):
    numbers_tried = []
    return check_recursively(number_to_check, numbers_tried)

def check_recursively(number_to_check, numbers_tried_list):
    if number_to_check in numbers_tried_list:
        return False
    else:
        number_as_string = str(number_to_check)
        new_number_to_check = 0
        for char in number_as_string:
            new_number_to_check += int(char) * int(char)
        if(new_number_to_check == 1):
            return True
        else:
            numbers_tried_list.append(number_to_check)
            return check_recursively(new_number_to_check, numbers_tried_list)

print(is_number_happy(19)) #should return True
print(is_number_happy(79)) #should return True
print(is_number_happy(88)) #should return False

# Determine if all numbers between 1 and 100 are prime
# If a number is not divisible by anything, then diving the number by all the numbers between 2 and one less than the 
# number will always return a remainder greater than 0
# It will take a long time, but we can brute force it by doing this for every number between 1 and 100
# With the above descriptions, 1 is a special case, it's automatically not prime
def is_prime(number):
    if number == 1:
        return False
    for index in range(2, number):
        if (number % index) == 0:
            return False
    return True

for i in range(1, 100):
    if is_prime(i):
        print(f"The number {i} is Prime")

# Create Fibonacci sequence
# if we use a list, it's pretty easy to create a fibonacci sequence. The first two numbers in the sequence will just 
# be the number to start both times, then we can just keep going over and over adding the last two numbers
# in the list. We'll have to have a number of times to stop at or it will go on forever
def create_fibonacci(starting_number, how_many_numbers):
    sequence = [starting_number, starting_number]
    while(len(sequence) <= how_many_numbers):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

print(create_fibonacci(1, 44))