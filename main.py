# -------------------------------------------------
# Problem Solving I
# -------------------------------------------------

# Reverse a string
# Start at the right of a string and add it to a new string until done
# move the indexes in and keep switching until they meet
def reverse_string(string_to_reverse):
    reversed_string = ""
    for index in range(len(string_to_reverse) - 1, -1, -1):
        reversed_string += string_to_reverse[index]
    return reversed_string

test_one = "Hello"
test_two = "Antidisestablishmentarianism"
test_three = ""
print(reverse_string(test_one))
print(reverse_string(test_two))
print(reverse_string(test_three))



# Capitalize a Letter
# Start by capitalizing the first letter in the string
# In this instance, it is safe to assume that after every space there will be a letter that needs capitalizing
# and that there will only be one space and the string will not be empty
# build a new sring and when you hit a space, capitalize the next letter
def capitalize_first_letters(string_to_cap):
    new_string = string_to_cap[0].upper()
    index = 1
    while(index < len(string_to_cap)):
        if string_to_cap[index] == ' ':
            new_string += string_to_cap[index]
            index += 1
            new_string += string_to_cap[index].upper()
        else:
            new_string += string_to_cap[index]
        index += 1
    return new_string

test_one = "hello world"
test_two = "Hello World"
test_three = "hello"
print(capitalize_first_letters(test_one))
print(capitalize_first_letters(test_two))
print(capitalize_first_letters(test_three))



# Determine if a word is a palindrome
# Have a right index and a left index
# Move the left one right one and move the right one left one
# If they ever don't match, it's not a palindrome
# continue checking until the indexes meet
# it is safe to assume there are no spaces in this instance
def is_a_palindrome(string_to_check):
    left = 0
    right = len(string_to_check) - 1
    while left < right:
        if(not string_to_check[left] == string_to_check[right]):
            return False
        left += 1
        right -= 1
    return True

test_one = "madam"
test_two = "Hello World"
test_three = "noon"
print(is_a_palindrome(test_one))
print(is_a_palindrome(test_two))
print(is_a_palindrome(test_three))



# Compress a string of characters
# It is ok to assume the string will not be empty
# save a count of the number of recurring letters
# save which letter we are looking on
# go through the string, and if it's the same as the number we are looking at, add to the count 
# if it does not match the letter we are working on, add the letter count and the letter we were working on to the string to be returned
# and change the letter that we are working on
# at the end, we will have to make sure the last step completes because we will get to the end of the string before adding the last letter
def compress_string(string_to_compress):
    index = 1
    letter_compressing = string_to_compress[0]
    number_found = 1
    reverse_string = ''
    while index < len(string_to_compress):
        if(string_to_compress[index] == letter_compressing):
            number_found += 1
        else:
            reverse_string += str(number_found) + letter_compressing
            letter_compressing = string_to_compress[index]
            number_found = 1
        index += 1
    reverse_string += str(number_found) + letter_compressing
    return reverse_string

test_one = "aaabbbbbccccaacccbbbaaabbbaaa"
test_two = "aaaa"
test_three = "abcdefg"
print(compress_string(test_one))
print(compress_string(test_two))
print(compress_string(test_three))


# -------------------------------------------------
# Problem Solving I
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
# With the above descriptions, 1 is a special case, it's automatically prime
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