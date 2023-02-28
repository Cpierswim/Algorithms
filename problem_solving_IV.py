from problem_solving_I import reverse_string

# -------------------------------------------------
# Problem Solving IV
# -------------------------------------------------
# Task 1 - two numbers in a list will add up to a given number, find them
# go through each number and test every other number and see if they add up to the given number
# skip the case where you're testing a number against itself
# if they add up, return the indexes in another list

def get_indexes(list_to_check, target_number) -> list:
    for i in range(0, len(list_to_check)):
        for j in range(0, len(list_to_check)):
            if i != j:
                if (list_to_check[i] + list_to_check[j]) == target_number:
                    return_list = [i, j]
                    return return_list
test_one = [5, 17, 77, 50]
print(get_indexes(test_one, 55)) # should return [0,3]
test_two = [3, 4, 1, 5, 7, 10, 22, 49, 99, 29]
print(get_indexes(test_two, 148)) # should return [7, 8]
test_three = [0, 2]
print(get_indexes(test_three, 2)) # should return [0, 1]


# Task 2 - palindrome but allow multi-words and punctuation
# do everything the same as before, but if a non alpha character is found, skip it
def is_a_palindrome(string_to_check):
    string_to_check = string_to_check.lower()
    left = 0
    right = len(string_to_check) - 1
    while left < right:
        while not string_to_check[right].isalpha() and left < right:
            right -= 1
        while not string_to_check[left].isalpha() and left < right:
            left += 1
        if left < right and (not string_to_check[left] == string_to_check[right]):
            return False
        left += 1
        right -= 1
    return True

test_one = "madam"
test_two = "race $car...."
test_three = "noon jjd"
#print(is_a_palindrome(test_one))
#print(is_a_palindrome(test_two))
#print(is_a_palindrome(test_three))
print(is_a_palindrome("h"))

# Task 3 - determine if a sequence is made from the non sorted list provided
# Sort the list, then start at the second element of the list and see if the previous element is one less
# keep repeating until the end of the list

def is_sequence_possible(list_to_check) -> bool:
    list_to_check.sort()
    for i in range(1, len(list_to_check)):
        if list_to_check[i - 1] != (list_to_check[i] - 1):
            return False
    return True

print("")
test_one = [5, 7, 3, 8, 6]
test_two = [17, 15, 20, 19, 21, 16, 18]
test_three = [-3,-2, 0, -4, -1, 1]
print(is_sequence_possible(test_one)) # False
print(is_sequence_possible(test_two)) # True
print(is_sequence_possible(test_three)) # True

# Task 4 - count he positive and negative numbers
# Go through the list and if it's below 0, add one to the negative count, if it's above 0 add one to the positive count
# if it's 0, do nothing because 0 is neither negative or positive
def count_pos_and_neg(list_to_check) -> list:
    negative_numbers = 0
    positive_numbers = 0
    for num in list_to_check:
        if num < 0:
            negative_numbers += num
        elif num > 0:
            positive_numbers += 1
    return_list = [positive_numbers, negative_numbers]
    return return_list

test_one = [7, 9, -3, -32, 107, -1, 36, 95, -14, -99, 21]
test_two = [-1, -2, -3, 0]
test_three = [4]
print("")
print(count_pos_and_neg(test_one)) # [6, 5]
print(count_pos_and_neg(test_two)) # [0, 3]
print(count_pos_and_neg(test_three)) # [1, 0]

#Task 5 - return lowest and highest ints as a string from a list of strings
# Split the list several times at the space
# Change all the split strings into ints (safe to assume they will all sucessfully convert)
# sort the list
# return the beginning and end of the list as a new list
def remove_middle(string_to_check) -> str:
    separated_values = string_to_check.split(" ")
    separated_values_as_ints = []
    for string in separated_values:
        separated_values_as_ints.append(int(string))
    separated_values_as_ints.sort()
    return_list = [separated_values_as_ints[0], separated_values_as_ints[-1]]
    return return_list

print("")
test_one = "3 9 0 1 4 8 10 2"
test_two = '4 2 444 2 3 -1 99'
test_three = '4 3'
print(remove_middle(test_one))
print(remove_middle(test_two))
print(remove_middle(test_three))


# Task 6 = is an email valid
# First, there must be a @, so split the string on that. There can only be 1, so there can only be 2 substrings. If there aren't, it's not valid
# second, check the recepiant
#   - There is a limit of 1-64 characters. If it's not that, it's not vaild
#   - next, the first and last character can only be alphanumeric. If either aren't, it's not valid
#   - next, there are only certain non-alphanumeric characters that are acceptable, and they can't repeat themselves
#          if there are non acceptable carachters, or a non-alphanumeric character repeats itself, it's not valid
# next, check the domain
# there will be any number of periods breaking up the domain, split on the periods
# there has to be at least one period, so if there isn't, it's not valid
# for any split domain other than the last one, the only acceptable characters are alphanumeric or a hyphen, if it's not, it's not valid
# for the top level domain, only certain values are allowed. I did not code in an exhaustive list

def is_valid_email(string_to_check) -> bool:
    strings = string_to_check.split("@")
    if len(strings) != 2:
        return False
    if len(strings[0]) < 1 or len(strings[0]) > 64:
        return False
    if not strings[0][0].isalnum():
        return False
    if not strings[0][-1].isalnum():
        return False
    last_symbol = ''
    for char in strings[0]:
        if not char.isalnum():
            if is_valid_symbol(char):
                if last_symbol == char:
                    return False
                else:
                    last_symbol = char
            else:
                return False
        else:
            last_symbol = ''
    if strings[1].rfind('.') == -1:
        return False
    domain = strings[1].split('.')
    for index in range(0, len(domain) -1):
        for char in domain[index]:
            if not (char.isalnum() or char == "-"):
                return False
    
    if not is_acceptable_tld(domain[-1]):
        return False
    
    return True
                
def is_acceptable_tld(tld_to_check) -> bool:
    acceptable_tld = ["com", "org", "net", "mil", "int", "edu", "gov", "arpa"]
    for tld in acceptable_tld:
        if tld_to_check == tld:
            return True
    return False

def is_valid_symbol(char_to_check) -> bool:
    valid_symbols = ['!', '#', '$', '%',  '&', '\'', '*',  '+', '-', '/', '=', '?', '^', '_', '`', '{', '|', '.']
    for symbol in valid_symbols:
        if symbol == char_to_check:
            return True
    return False

print("")
test_one = 'mike1@gmail.com'
test_two = 'mi$$ke@gmail.com'
test_three = 'Cpier.swim+one@gmail.met'
print(is_valid_email(test_one))
print(is_valid_email(test_two))
print(is_valid_email(test_three))

# Task 7 - create a string of int values from a given string
# Using ASCII values gives an ordered number for letters, I just need them to be all upper or lower case, and subtract one less
# than the value of the ASCII value for A from everything. Ignore anything that's not numeric and build the string to return

def change_to_ints(string_to_change) -> str:
    return_string = ""
    for i in range(0, len(string_to_change)):
        if string_to_change[i].isalpha():
            return_string += str(ord(string_to_change[i].upper()) - 64)
            if i != len(string_to_change) - 1:
                return_string += " "
    return return_string

print("")
test_one = 'abc'
test_two = 'coding is fun'
test_three = "A4 Bc"
print(change_to_ints(test_one))
print(change_to_ints(test_two))
print(change_to_ints(test_three))

# Task 8 - briefcase lock movments
# get mod of the numbers by 10 to get the first digit
# the absolute value of the current digit minus the target digit will give you how many turns it takes to go directly to the target number
# 10 - the above will give you the number of turns it takes to go past 0
# take the fewer of the 2 and add it to a running number of rotations
# remove the first number of the number we are working on and repeat everything until finished
def fewest_lock_turns(current, target) -> int:
    rotation = 0
 
    # iterate till input and unlock
    # code become 0
    while (current > 0 or target > 0):
 
        # input and unlock last digit
        # as reminder
        current_digit = current % 10
        target_digit = target % 10
 
        # find min rotation
        rotation += min(abs(current_digit - target_digit), 10 - abs(current_digit - target_digit))
 
        # update code and input
        current = int(current / 10)
        target = int(target / 10)
 
    return rotation

print ("")
current_one = 3893 
target_one = 5296 
current_two = 3893 
target_two = 0000
current_three = 499204
target_three = 000000 
print(fewest_lock_turns(current_one, target_one))
print(fewest_lock_turns(current_two, target_two))
print(fewest_lock_turns(current_three, target_three))

# Task 9 - reciprocal of the reverse of the original number
# change the number to a string and use the reverse_string method I created above to reverse it
# if it is a negative number, remove the negative sign
# divide one by it, and if it was negative multiply by -1 to give the negative back
def return_reciprocal_of_reverse(number: int) -> float:
    if number > 0:
        return 1/int(reverse_string(str(number)))
    if number < 0:
        return 1/int(reverse_string(str(number)).removesuffix('-')) * -1

print("")
test_one = 17
test_two = -17
test_three = 2
print(return_reciprocal_of_reverse(test_one))
print(return_reciprocal_of_reverse(test_two))
print(return_reciprocal_of_reverse(test_three))
