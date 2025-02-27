#Write a Python program to count how many times each 
#character appears in a string.

user_input = input("Enter a string: ")

char_count = {}

for char in user_input:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("Character counts:")
for char, count in char_count.items():
    print(f"'{char}': {count}")
