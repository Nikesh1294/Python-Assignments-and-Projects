# ==========================================
# EXCEPTION HANDLING ASSIGNMENT
# ==========================================

# 1. Handle a ZeroDivisionError exception [cite: 49]
def divide_numbers(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: You cannot divide by zero!")


print("--- Question 1 ---")
divide_numbers(10, 0)


# 2. Prompt for an integer and handle ValueError
def get_integer():
    try:
        user_input = input("Enter an integer: ")
        number = int(user_input)
        print(f"You entered the integer: {number}")
     except ValueError:
        print("Error: That is not a valid integer!")


print("\n--- Question 2 ---")


 get_integer():
# Uncomment to test with live input


# 3. Open a file and handle FileNotFoundError [cite: 51]
def open_file(filename):
    try:
        with open(filename, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")


print("\n--- Question 3 ---")
open_file("missing_file.txt")


# 4. Prompt for two numbers and handle TypeError [cite: 52]
def check_numeric_input():
    # We use a helper to manually raise TypeError if inputs aren't digits
    # to demonstrate the specific exception handling requested
    try:
        val1 = input("Enter first number: ")
        val2 = input("Enter second number: ")

        if not (val1.replace('.', '', 1).isdigit() and val2.replace('.', '', 1).isdigit()):
            raise TypeError("Inputs must be numerical values.")

        print(f"Sum: {float(val1) + float(val2)}")
    except TypeError as e:
        print(f"Error: {e}")


print("\n--- Question 4 ---")


# check_numeric_input() # Uncomment to test


# 5. Open a file and handle PermissionError [cite: 53]
def check_permission(filename):
    try:
        with open(filename, 'w') as file:
            file.write("Testing permissions.")
    except PermissionError:
        print(f"Error: You do not have permission to write to '{filename}'.")


print("\n--- Question 5 ---")
# On many systems, trying to write to a system file triggers this
check_permission("/root/test.txt")


# 6. Execute list operation and handle IndexError [cite: 54]
def access_list_element(my_list, index):
    try:
        print(f"Element at index {index}: {my_list[index]}")
    except IndexError:
        print(f"Error: Index {index} is out of range for the list.")


print("\n--- Question 6 ---")
sample_list = [10, 20, 30]
access_list_element(sample_list, 5)


# 7. Execute division and handle ArithmeticError [cite: 55]
def arithmetic_check(a, b):
    try:
        # ArithmeticError is a base class for ZeroDivisionError
        result = a / b
        print(f"Result: {result}")
    except ArithmeticError:
        print("Error: An arithmetic error occurred (Division by zero).")


print("\n--- Question 7 ---")
arithmetic_check(5, 0)


# ==========================================
# FUNCTION ASSIGNMENT
# ==========================================

# 1. Find the maximum of three numbers [cite: 1]
def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


print("\n--- Function Q1 ---")
print(f"Max of 10, 25, 15: {find_max(10, 25, 15)}")


# 2. Sum all numbers in a list [cite: 2, 3]
def sum_numbers(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total


print("\n--- Function Q2 ---")
print(f"Sum of (8, 2, 3, 0, 7): {sum_numbers([8, 2, 3, 0, 7])}")


# 3. Multiply all numbers in a list [cite: 4]
def multiply_numbers(numbers):
    result = 1
    for num in numbers:
        result = result * num
    return result


print("\n--- Function Q3 ---")
print(f"Product of (8, 2, 3, -1, 7): {multiply_numbers([8, 2, 3, -1, 7])}")


# 4. Reverse a string [cite: 5]
def reverse_string(text):
    return text[::-1]


print("\n--- Function Q4 ---")
print(f"Reverse of '1234abcd': {reverse_string('1234abcd')}")


# 5. Check if a number falls within a range [cite: 5]
def is_in_range(num, start, end):
    if num >= start and num <= end:
        return True
    else:
        return False


print("\n--- Function Q5 ---")
print(f"Is 5 in range 1-10? {is_in_range(5, 1, 10)}")


# 6. Count upper and lower case letters [cite: 6, 7]
def count_upper_lower(text):
    upper_count = 0
    lower_count = 0
    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    print(f"No. of Upper case characters : {upper_count}")
    print(f"No. of Lower case Characters : {lower_count}")


print("\n--- Function Q6 ---")
count_upper_lower('The quick Brow Fox')


# 7. Return new list with distinct elements [cite: 8]
def get_unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


print("\n--- Function Q7 ---")
print(f"Unique elements of [1,2,3,3,3,3,4,5]: {get_unique_elements([1, 2, 3, 3, 3, 3, 4, 5])}")


# 8. Check if string is a palindrome [cite: 8, 9]
def is_palindrome(text):
    # Remove spaces and make lowercase for phrases
    clean_text = text.replace(" ", "").lower()
    return clean_text == clean_text[::-1]


print("\n--- Function Q8 ---")
print(f"Is 'nurses run' a palindrome? {is_palindrome('nurses run')}")


# 9. Sort hyphen-separated sequence alphabetically [cite: 10, 11]
def sort_hyphenated_words(sequence):
    word_list = sequence.split('-')
    word_list.sort()
    return "-".join(word_list)


print("\n--- Function Q9 ---")
print(f"Sorted sequence: {sort_hyphenated_words('green-red-yellow-black-white')}")


# 10. Detect number of local variables in a function [cite: 11]
def test_locals():
    var1 = "Hello"
    var2 = 25
    var3 = [1, 2]


print("\n--- Function Q10 ---")
print(f"Number of local variables in 'test_locals': {test_locals.__code__.co_nlocals}")

# 11. Lambda functions for addition and multiplication [cite: 12, 13]
add_15 = lambda x: x + 15
multiply_xy = lambda x, y: x * y

print("\n--- Function Q11 ---")
print(f"10 + 15 = {add_15(10)}")
print(f"12 * 4 = {multiply_xy(12, 4)}")


# 12. Function that returns a multiplier [cite: 13, 14]
def multiplier_builder(n):
    return lambda x: x * n


double = multiplier_builder(2)
triple = multiplier_builder(3)

print("\n--- Function Q12 ---")
print(f"Double the number 15 = {double(15)}")
print(f"Triple the number 15 = {triple(15)}")

# 13. Sort a list of tuples using Lambda [cite: 14, 15]
tuple_list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
tuple_list.sort(key=lambda x: x[1])

print("\n--- Function Q13 ---")
print(f"Sorted Tuples: {tuple_list}")

# 14. Sort a list of dictionaries using Lambda [cite: 15, 16]
dicts = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]
# Sorting by color as indicated in sample
sorted_dicts = sorted(dicts, key=lambda x: x['color'])

print("\n--- Function Q14 ---")
print(f"Sorted Dictionaries: {sorted_dicts}")

# 15. Filter integers using Lambda [cite: 16, 17]
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, nums))
odds = list(filter(lambda x: x % 2 != 0, nums))

print("\n--- Function Q15 ---")
print(f"Evens: {evens}")
print(f"Odds: {odds}")

# 16. Square and cube every number using Lambda [cite: 17, 18]
nums_q16 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = list(map(lambda x: x ** 2, nums_q16))
cubes = list(map(lambda x: x ** 3, nums_q16))

print("\n--- Function Q16 ---")
print(f"Squares: {squares}")
print(f"Cubes: {cubes}")

# 18. Check if string starts with character using Lambda [cite: 18]
starts_with = lambda text, char: text.startswith(char)

print("\n--- Function Q18 ---")
print(f"Does 'Python' start with 'P'? {starts_with('Python', 'P')}")

# 19. Rearrange positive and negative numbers using Lambda [cite: 19, 20]
arr = [-1, 2, -3, 5, 7, 8, 9, -10]
# We sort by checking if the number is negative
rearranged = sorted(arr, key=lambda x: x < 0)

print("\n--- Function Q19 ---")
print(f"Rearranged array: {rearranged}")

# 20. Count even and odd numbers using Lambda [cite: 20, 21]
arr_q20 = [1, 2, 3, 5, 7, 8, 9, 10]
even_count = len(list(filter(lambda x: x % 2 == 0, arr_q20)))
odd_count = len(list(filter(lambda x: x % 2 != 0, arr_q20)))

print("\n--- Function Q20 ---")
print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")

# 21. Find numbers divisible by 19 or 13 using Lambda [cite: 21, 22]
list_q21 = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
divisible = list(filter(lambda x: x % 19 == 0 or x % 13 == 0, list_q21))

print("\n--- Function Q21 ---")
print(f"Divisible by 19 or 13: {divisible}")

# 22. Check string complexity using Lambda [cite: 22]
check_complexity = lambda s: any(c.isupper() for c in s) and \
                             any(c.islower() for c in s) and \
                             any(c.isdigit() for c in s) and \
                             len(s) >= 8

print("\n--- Function Q22 ---")
print(f"Is 'Python123' complex? {check_complexity('Python123')}")