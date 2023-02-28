from problem_solving_IV import is_a_palindrome

#Task 1 - print next 20 leap years
#Go through a loop and check every year since the first year provided that a year is a leap year by
#first checking if it is divisible by 4, then if it is divisble by 400 it is a leap year, if it's
#divisible by 100 instead of 400, it isn't a leap year. Years not divisible by any of them are not 
#leap years. Continue until 20 leap years are found
def print_next_20_leap_years(beginning_year: int) -> None:
    '''Prints the next 20 leap years
    
    beginning_year -- The first year to check if it is a leap year

    Uses formula that years divisible by 4 are leap years, except if the year is also divisible by 100 it is not, except if it also is equal to 400 it is
    '''
    leap_years_found = 0
    while leap_years_found < 20:
        if beginning_year % 4 == 0:
            if beginning_year % 100 == 0: 
                if beginning_year % 400 == 0:
                    leap_years_found += 1
                    print(beginning_year)
            else:
                leap_years_found += 1
                print(beginning_year)
        beginning_year += 1

print("Task 1 - print next 20 leap years")
print_next_20_leap_years(1982)


#Task 2 - Longest palindromic substring
#Check if every possible string from the first 2 characters to the entire string is a palindrome, and if it is, check and see if
#it is longer than a longer previous one found. I'm not really sure how the function should handle
#punctuation. Right now if there is something like ": race car" it will return that as a longer palindrome than "race car"
#which I guess it technically is, but I'm not sure if it should be that way, but the question doesn't specify, so I'm going to 
#consider it done
def get_longest_palindrome(string: str) -> str:
    '''Returns the longest substring that is a palindrome that it can find

    string -- The string to check
    '''
    longest_palindrome = ""
    for left in range(0, len(string)):
        for right in range(left + 1, len(string) + 1):
            substring = string[left:right].strip()
            if substring == "race car":
                stop = 1
            if is_a_palindrome(substring) and len(substring) > len(longest_palindrome):
                longest_palindrome = substring
    return longest_palindrome

print("\n\n#Task 2 - Longest palindromic substring")
print(get_longest_palindrome("This sentence contains a palindrome of race car")) #race car
print(get_longest_palindrome("This one does not that I am aware of")) #am a
print(get_longest_palindrome("abcdefg")) #a
                

#Task 3 - Seconds to hours and minutes
#First remove the number of hours, then remove the number of minutes. The remaining seconds don't matter
#To display it, leading 0's before the hours part doesn't matter, but there needs to be a leading 0
#before the minutes part
def display_as_hours_and_minutes(seconds) -> None:
    '''Displays the seconds formatted as H:MM
    
    seconds -- Number of seconds to calculate from
    '''
    hours = seconds // (60 * 60)
    seconds = seconds - (hours * 60 * 60)
    minutes = seconds // 60
    print(f"{hours}:{minutes:02d}")

print("\n\nTask 3 - Seconds to hours and minutes")
display_as_hours_and_minutes(61)
display_as_hours_and_minutes(3655)
display_as_hours_and_minutes(43323)

#Task 4 - Difference from 13
#If the number is greater than or equal to 13, return double the difference
#If the number is less than, you'll need the absolute value to make sure that the negative numbers add to the 
#difference so it handles the move from positive numbers to negative correctly
def difference_from_thirteen(num) -> int:
    '''Returns the difference from 13 if the number is below 13, or double the difference if the number is above 13
    
    num -- The number to check versus 13
    '''
    if num >= 13:
        return (num - 13) * 2
    else:
        return abs(13 - num) 

print("\n\nTask 4 - Difference from 13")
print(difference_from_thirteen(20)) #14
print(difference_from_thirteen(-8)) #21
print(difference_from_thirteen(4)) #9
print(difference_from_thirteen(13)) #0


#Task 5 - Right digit check
#This might not be the way wanted, but I figure it's O(1), so whatever
#Change the numbers to string so the right digit can be checked, then checked them
def same_right_digit(num1: int, num2: int, num3: int) -> int:
    '''Returns 1 if the last digit of 2 of the numbers match, 2 if they all match, 0 if none match
    
    num1 -- The first number to check
    num2 -- The second number to check
    num3 -- The third number to check
    '''
    num1 = str(num1)
    num2 = str(num2)
    num3 = str(num3)
    matches = 0
    if num1[-1] == num2[-1] and num1[-1] == num3[-1]:
        return 2
    elif num1[-1] == num2[-1] or num1[-1] == num3[-1] or num2[-1] == num3[-1]:
        return 1
    else:
        return 0

print("\n\nTask 5 - Right digit check")
print(same_right_digit(243, 239, 2339))
print(same_right_digit(0, 40, 2000))
print(same_right_digit(422, 4, 6652))

#Task 6 - Characters space check
#Start at the left of the string and if an a or b is found, switch the character we are looking for to the opposite one
#and look ahead 3 spots and see if it is the other character. Can stop 3 from the end because there can't be any
#matches after that, also we don't need to look back because a match would have already been found
def a_and_b_three_apart(string:str) -> bool:
    '''Returns true if the characters 'a' and 'b' are found 3 characters apart
    
    string -- The string to check
    '''
    string = string.lower()
    for i in range(0, len(string) - 3):
        look_for_char = None
        if string[i] == 'a':
            look_for_char = 'b'
        elif string[i] == 'b':
            look_for_char = 'a'
        if string[i + 3] == look_for_char:
            return True
    return False

print("\n\nTask 6 - Characters space check")
print(a_and_b_three_apart("abxaxxxxxxxab")) #False
print(a_and_b_three_apart("ad")) #False
print(a_and_b_three_apart("axxb")) #True
print(a_and_b_three_apart("xxxxxaxxbxxx")) #True
print(a_and_b_three_apart("xxxxxaxxaxxx")) #False



#Task 7 - p's and t's
#Go through all the characters in the string, change it to lowercase so that case can be ignored
#then add up the P's and the t's and return if the numbers are the same or not
def are_ps_and_ts_the_same(string: str) -> bool:
    '''Returns true if the string has the name number of the charachter 'p' as 't' ignoring case.
    
    string -- The string to check
    '''
    if string is None:
        return True
    p = 0
    t = 0
    for index in range(0, len(string)):
        if string[index].lower() == 'p':
            p += 1
        elif string[index].lower() == 't':
            t += 1
    return p == t

print("\n\nTask 7 - p's and t's")
print(are_ps_and_ts_the_same("pppttt")) #True
print(are_ps_and_ts_the_same('')) #True
print(are_ps_and_ts_the_same(None)) #True
print(are_ps_and_ts_the_same("This should return false")) #False

#Task 8 - Sum all digits
#Go through each character and if it is a number, convert it to an int and add it to the running sum
#The way I interpret the question, it should ignore the negative sign because a digit by itself can't be negative
def sum_digits_in_string(string: str) -> int:
    '''Returns the sum of all digits in the string, ignoring any negative signs
    
    string -- The string to check
    '''
    sum = 0
    for char in string:
        if char.isnumeric():
            sum += int(char)
    return sum

print("\n\nTask 8 - Sum all digits")
print(sum_digits_in_string("1234")) #10
print(sum_digits_in_string("1xasdf   -2asdf s!~#$$$@3ds4dddfff")) #10
print(sum_digits_in_string("asdklj;asdfs")) #0

#Task 9 - Proper or Improper
#According to what I found on the internet, a fraction is proper as long as the denominator is less than the numerator
#and the denominator does not determine if a fraction is negative or not, it's the numerator
#also, this should probably throw an error if the denominator is 0, but I'm not sure if that's wanted or not
def is_proper_fraction(numerator: int, denominator: int) -> bool:
    '''Returns true if the absolute value of the numerator is less than the denominator and the the denominator is not negative or 0
    
    numerator -- the numerator value
    denominator -- the denominator value, should not be 0 or negative if you want a proper fraction
    '''
    return abs(numerator) < denominator and denominator > 0

print("\n\nTask 9 - Proper or Improper")
print(is_proper_fraction(5, 3)) #False
print(is_proper_fraction(1, 9)) #True
print(is_proper_fraction(4, 0)) #False
print(is_proper_fraction(-8, 5)) #False
print(is_proper_fraction(-3, 9)) #True

#Task 10 - Pig Latin
#Split the list into words, then with each word, move the first character to the end, make it lowercase, and and an 'ay'
#Add it to a running string, then capitalize the string before returning it
def piglatinize(string:str) -> str:
    '''Returns a string that has been pig latin-ized
    
    string - The string to pig latin-ize
    '''
    words = string.split(" ")
    return_string = ""
    for i in range(0, len(words)):
        return_string += words[i][1:] + words[i][0].lower() + "ay"
        if i != len(words) - 1:
            return_string += " "
    
    return_string = return_string.capitalize()
    return return_string

print("\n\n#Task 10 - Pig Latin")
print(piglatinize("The quick brown fox"))
print(piglatinize("I think I am done if the I works"))

#Task 11 - Rotate list
def rotate_list(list_to_rotate: list, places:int) -> list:
    for i in range(places):
        first = list_to_rotate[0]
        for j in range(len(list_to_rotate) - 1):
            list_to_rotate[j] = list_to_rotate[j + 1]
        list_to_rotate[len(list_to_rotate) - 1] = first
    return list_to_rotate

print("\n\nTask 11 - Rotate list")
print(rotate_list([1, 2, 3, 4, 5, 6], 2))
print(rotate_list([1, 2, 3, 4, 5, 6], 8))

