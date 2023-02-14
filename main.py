#Reverse a string
#Start at the right of a string and add it to a new string until done
#move the indexes in and keep switching until they meet
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