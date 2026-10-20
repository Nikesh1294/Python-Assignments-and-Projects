# --- Python Data Type Assignment (Alternative Methods) ---
import math

# 1. Add two lists index-wise using zip_longest (handles leftovers automatically)
from itertools import zip_longest


def add_lists_alternative(l1, l2):
    # zip_longest fills missing values with None; we filter them out
    return [[a, b] if b is not None else a for a, b in zip_longest(l1, l2)]


list1 = ["M", "na", "i", "Ra"]
list2 = ["y", "me", "s", "hul"]
print("1. Index-wise (Zip method):", add_lists_alternative(list1, list2))

# 2. Add item 7000 after 6000 using deep indexing
list1_q2 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# Using insert to be specific about placement after 6000
list1_q2[2][2].insert(list1_q2[2][2].index(6000) + 1, 7000)
print("2. Insert 7000:", list1_q2)

# 3. Show candy items using f-string joining
candy_list = ['Jelly Belly', 'Kit Kat', 'Double Bubble', 'Milky Way', 'Three Musketeers']
no_of_items = [10, 20, 34, 74, 32]
print("3. Candy List:")
print("\n".join([f"{c}-{n}" for c, n in zip(candy_list, no_of_items)]))

# 4. Running Sum using itertools.accumulate
from itertools import accumulate

list1_q4 = [1, 2, 3, 4, 5, 6]
print("4. Running Sum (Accumulate):", list(accumulate(list1_q4)))


# 5. List sum of elements >= itself using list comprehension
def sum_logic_alt(lst):
    return [sum(filter(lambda x: x >= val, lst)) for val in lst]


print("5. Greater/Equal Sum:", sum_logic_alt([2, 4, 6, 10, 1]))

# 6. Common unique items using set intersection operator &
num1 = [23, 45, 67, 78, 89, 34]
num2 = [34, 89, 55, 56, 39, 67]
print("6. Common items (Sorted Set):", sorted(list(set(num1) & set(num2))))


# 7. Sort Alphanumeric based on product using math.prod
def product_sorter(s):
    digits = [int(char) for char in s if char.isdigit()]
    return math.prod(digits) if digits else 1


data = ['1ac21', '23fg', '456', '098d', '1', 'kls']
print("7. Sorted by Product:", sorted(data, key=product_sorter, reverse=True))

# 8. Max of row using map and max
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("8. Matrix Row Max:", list(map(max, matrix)))


# 9. Shortlist Students using a list comprehension filter
def filter_students():
    # Record structure: (Name, Edu, Skill, Year)
    students = [('Manohar', 'B.Tech', 'Python', '2022'), ('Ponian', 'B.Sc.', 'C++', '2020')]
    criteria = ('Python', 'B.Tech', '2022')

    matches = [s for s in students if (s[2], s[1], s[3]) == criteria]
    print("9. Matches:", matches if matches else "No such candidate")


filter_students()

# 10. Common elements in three lists using set.intersection
ar1, ar2, ar3 = [1, 5, 10, 20, 40, 80], [6, 7, 20, 80, 100], [3, 4, 15, 20, 30, 70, 80, 120]
print("10. Intersection of 3:", list(set(ar1).intersection(ar2, ar3)))

# 11. Unique vowels count using set logic
str1 = "hands-on data science mentorship progrAm with live classes at affordable fee only on CampusX"
vowel_count = len({char for char in str1 if char in 'aeiouAEIOU'})
print("11. Unique Vowel Count:", vowel_count)

# 12. Intersection using list comprehension (no sets used)
lst1 = [4, 9, 1, 17, 11, 26, 28, 54, 69]
lst2 = [9, 9, 74, 21, 45, 11, 63, 28, 26]
# Removing duplicates while maintaining order from lst1
inter = list(dict.fromkeys([x for x in lst1 if x in lst2]))
print("12. List Comprehension Intersection:", inter)

# 13. List of Tuples to Dict using dict constructor
tuples_list = [("akash", 10), ("gaurav", 12), ("anand", 14)]
# Wrapping values in list to match required output format
dict_res = {k: [v] for k, v in tuples_list}
print("13. Dict Conversion:", dict_res)


# 14. Unique elements via Dictionary keys (Preserves order)
def unique_ordered(lst):
    return list(dict.fromkeys(lst))


print("14. Unique elements:", unique_ordered([1, 2, 3, 3, 3, 3, 4, 5]))

# 15. Even numbers using filter and lambda
sample_q15 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("15. Filtered Evens:", list(filter(lambda x: x % 2 == 0, sample_q15)))


# 16. Perfect Number check using list comprehension
def check_perfect_alt(n):
    return sum([i for i in range(1, n) if n % i == 0]) == n


print("16. Is 28 Perfect?:", check_perfect_alt(28))

# 17. Concatenate dicts using Dictionary Unpacking (**)
dic1, dic2, dic3 = {1: 10, 2: 20}, {3: 30, 4: 40}, {5: 50, 6: 60}
combined = {**dic1, **dic2, **dic3}
print("17. Unpacked Concatenation:", combined)


# 18. Histogram using a dictionary and floor division
def histogram_alt(nums):
    bins = {}
    for n in nums:
        # Find the bin range e.g. 13 -> 11-20
        start = ((n - 1) // 10 * 10) + 1
        end = start + 9
        label = f"{start}-{end}"
        bins[label] = bins.get(label, 0) + 1
    return dict(sorted(bins.items()))


print("18. Bin Histogram:", histogram_alt([13, 42, 15, 37, 22, 39, 41, 50]))