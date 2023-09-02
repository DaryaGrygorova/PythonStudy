"""
Task 1
Make a program that has some sentence (a string) on input
and returns a dict containing all unique words as keys and the number
of occurrences as values.
"""

print(
    "This program has some sentence (a string) on input "
    "and returns a dict containing all unique words as keys \n"
    "and the number of occurrences as values"
)

# Create a string from user input without duplicate spaces
USER_STR = " ".join(input("Please enter a some sentence: ").split())

word_list = USER_STR.lower().split(" ")
new_dict = {}

for word in word_list:
    # Loop optimization. Prevents multiple reassignment of dict key value
    if word in new_dict:
        continue
    new_dict[word] = word_list.count(word)

print(new_dict)
