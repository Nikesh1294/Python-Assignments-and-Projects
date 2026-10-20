import os
import random

# --- STEP 1: Create a dummy file so the code has something to read ---
with open("test_io.txt", "w") as f:
    f.write("Apple\nBanana\nCherry\nDate\nElderberry\nFig\nGrape")

# ==========================================
# FILE IO ASSIGNMENT SOLUTIONS
# ==========================================

# 1. Read an entire text file [cite: 56]
def read_entire_file(filename):
    with open(filename, 'r') as f:
        print(f.read())

print("--- Q1: Read Entire File ---")
read_entire_file("test_io.txt")


# 2. Read first n lines of a file [cite: 57]
def read_first_n(filename, n):
    with open(filename, 'r') as f:
        for i in range(n):
            print(f.readline().strip())

print("\n--- Q2: Read First 3 Lines ---")
read_first_n("test_io.txt", 3)


# 3. Append text to a file and display the text [cite: 58]
def append_and_show(filename, text):
    with open(filename, 'a+') as f:
        f.write(text + "\n")
        f.seek(0) # Go back to start to read
        print(f.read())

print("\n--- Q3: Append 'Honey' and Show ---")
append_and_show("test_io.txt", "Honey")


# 4. Read last n lines of a file [cite: 59]
def read_last_n(filename, n):
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines[-n:]:
            print(line.strip())

print("\n--- Q4: Read Last 2 Lines ---")
read_last_n("test_io.txt", 2)


# 5. Read a file line by line and store it into a list [cite: 60]
def file_to_list(filename):
    with open(filename, 'r') as f:
        return f.readlines()

print("\n--- Q5: File to List ---")
print(file_to_list("test_io.txt"))


# 8. Count the number of lines in a text file [cite: 63]
def count_lines(filename):
    with open(filename, 'r') as f:
        return len(f.readlines())

print("\n--- Q8: Count Lines ---")
print("Total lines:", count_lines("test_io.txt"))


# 9. Count the frequency of words in a file [cite: 64]
def word_frequency(filename):
    with open(filename, 'r') as f:
        words = f.read().split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq

print("\n--- Q9: Word Frequency ---")
print(word_frequency("test_io.txt"))


# 10. Get the file size of a plain file [cite: 65]
def get_size(filename):
    return os.path.getsize(filename)

print("\n--- Q10: File Size ---")
print("Size in bytes:", get_size("test_io.txt"))


# 11. Write a list to a file [cite: 66]
def list_to_file(filename, my_list):
    with open(filename, 'w') as f:
        for item in my_list:
            f.write(item + "\n")
    print(f"List written to {filename}")

print("\n--- Q11: Write List to File ---")
list_to_file("output_list.txt", ["Red", "Green", "Blue"])


# 12. Copy the contents of a file to another file [cite: 67]
def copy_file(source, destination):
    with open(source, 'r') as f1, open(destination, 'w') as f2:
        f2.write(f1.read())
    print(f"Copied {source} to {destination}")

print("\n--- Q12: Copy File ---")
copy_file("test_io.txt", "copy_of_test.txt")


# 13. Read a random line from a file [cite: 68]
def random_line(filename):
    lines = open(filename).read().splitlines()
    return random.choice(lines)

print("\n--- Q13: Random Line ---")
print("Random pick:", random_line("test_io.txt"))


# 14. Assess if a file is closed or not [cite: 69]
def is_file_closed(filename):
    f = open(filename, 'r')
    print("Is closed initially?", f.closed)
    f.close()
    print("Is closed after .close()?", f.closed)

print("\n--- Q14: Check if Closed ---")
is_file_closed("test_io.txt")


# 15. Return the number of words of a given text file [cite: 70]
def count_words(filename):
    with open(filename, 'r') as f:
        data = f.read()
        return len(data.split())

print("\n--- Q15: Word Count ---")
print("Total words:", count_words("test_io.txt"))