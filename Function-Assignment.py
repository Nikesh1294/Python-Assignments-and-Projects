# --- Python Functions Assignment ---

# 1. Function to find the maximum of three numbers
def max_of_three(a, b, c):
    return max(a, b, c)

print(" Max of three (10, 25, 15):", max_of_three(10, 25, 15))


# 2. Function to sum all the numbers in a list
# Sample List : (8, 2, 3, 0, 7) -> Expected Output : 20
def sum_list(numbers):
    total = 0
    for x in numbers:
        total += x
    return total

print("Sum of list (8, 2, 3, 0, 7):", sum_list((8, 2, 3, 0, 7)))


# 3. Function to multiply all the numbers in a list
# Sample List : (8, 2, 3, -1, 7) -> Expected Output : -336
def multiply_list(numbers):
    result = 1
    for x in numbers:
        result *= x
    return result

print("Multiply list (8, 2, 3, -1, 7):", multiply_list((8, 2, 3, -1, 7)))


# 4. Function to reverse a string
# Sample String : "1234abcd" -> Expected Output : "dcba4321"
def reverse_string(text):
    return text[::-1]

print( reverse_string('1234abcd'))


# 5. Function to check whether a number falls within a given range
def in_range(n, start, end):
    return start <= n <= end

print("Is 5 in range 1-10?:", in_range(5, 1, 10))


# 6. Function to count upper and lower case letters
# Sample String : 'The quick Brow Fox'
def count_case(text):
    upper = sum(1 for char in text if char.isupper())
    lower = sum(1 for char in text if char.islower())
    return upper, lower

u, l = count_case('The quick Brow Fox')
print(f"  No. of Upper case characters : {u}")
print(f"  No. of Lower case Characters : {l}")


# 7. Function that returns a new list with distinct elements
# Sample List : [1,2,3,3,3,3,4,5] -> Unique List : [1, 2, 3, 4, 5]
def unique_list(items):
    return list(set(items))

print(" Unique elements:", unique_list([1,2,3,3,3,3,4,5]))


# 8. Function to check if a string is a palindrome
def is_palindrome(text):
    text = text.replace(" ", "").lower()
    return text == text[::-1]

print(" Is 'madam' a palindrome?:", is_palindrome("madam"))


# 9. Sort hyphen-separated sequence of words
# Sample: green-red-yellow-black-white
def sort_hyphenated(sequence):
    words = [w for w in sequence.split("-")]
    words.sort()
    return "-".join(words)

print(" Sorted hyphen sequence:", sort_hyphenated("green-red-yellow-black-white"))


# 10. Program to detect the number of local variables declared in a function
def local_var_test():
    a = 1
    b = 2
    str_val = "Gemini"

print(" Local variables in local_var_test():", local_var_test.__code__.co_nlocals)


# 11. Lambda to add 15 and multiply x with y
add_15 = lambda x: x + 15
multiply = lambda x, y: x * y
print(" Lambda add 15 to 10:", add_15(10))
print(" Lambda multiply 12 * 4:", multiply(12, 4))


# 12. Function that multiplies argument with an unknown given number
def multiplier_func(n):
    return lambda x: x * n

double = multiplier_func(2)
print(" Double the number 15:", double(15))


# 13. Sort a list of tuples using Lambda
tuples_list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
tuples_list.sort(key=lambda x: x[1])
print(" Sorted tuples by marks:", tuples_list)


# 14. Sort a list of dictionaries using Lambda
dicts_list = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
sorted_dicts = sorted(dicts_list, key=lambda x: x['color'])
print(" Sorted dictionaries by color:", sorted_dicts)


# 15. Filter list of integers using Lambda
int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums = list(filter(lambda x: x % 2 == 0, int_list))
odd_nums = list(filter(lambda x: x % 2 != 0, int_list))
print(" Even numbers:", even_nums)
print("    Odd numbers:", odd_nums)


# 16. Square and cube every number using Lambda
sq_cube_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = list(map(lambda x: x**2, sq_cube_list))
cubes = list(map(lambda x: x**3, sq_cube_list))
print(" Squares:", squares)
print("    Cubes:", cubes)


# 18. Check if string starts with character using Lambda
starts_with = lambda s, char: s.startswith(char)
print(" Does 'Python' start with 'P'?:", starts_with("Python", "P"))


# 19. Rearrange positive and negative numbers using Lambda
arr = [-1, 2, -3, 5, 7, 8, 9, -10]
rearranged = sorted(arr, key=lambda x: 0 if x >= 0 else 1)
print(" Rearranged array (positives first):", rearranged)


# 20. Count even and odd numbers in array using Lambda
count_arr = [1, 2, 3, 5, 7, 8, 9, 10]
evens = len(list(filter(lambda x: x % 2 == 0, count_arr)))
odds = len(list(filter(lambda x: x % 2 != 0, count_arr)))
print(f" Even count: {evens}, Odd count: {odds}")


# 21. Numbers divisible by 19 or 13 using Lambda
div_list = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
div_result = list(filter(lambda x: x % 19 == 0 or x % 13 == 0, div_list))
print(" Divisible by 19 or 13:", div_result)


# 22. Check string for Capital, Lower, Number and Min length using Lambda
complexity_check = lambda s: any(c.isupper() for c in s) and \
                             any(c.islower() for c in s) and \
                             any(c.isdigit() for c in s) and \
                             len(s) >= 8

print(" Is 'Python123' complex enough?:", complexity_check("Python123"))