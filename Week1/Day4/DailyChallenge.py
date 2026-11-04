
"""
Challenge 1: Multiples of a Number

Instructions:
- Ask the user for two integers: a number and a length.
- Generate a list of multiples of the given number.
- The list should contain the amount of numbers specified by the length.
- Print the final list.

Example:
Number: 7
Length: 5
Output: [7, 14, 21, 28, 35]
"""

number = int(input("Enter a number: "))
length = int(input("Enter a length: "))

multiples = []

for i in range(1, length + 1):
    multiples.append(number * i)

print(multiples)


"""
Challenge 2: Remove Consecutive Duplicate Letters

Instructions:
- Ask the user to enter a string.
- Remove consecutive duplicate letters from the string.
- Keep non-consecutive duplicate letters.
- Print the modified string.

Examples:
"ppoeemm" -> "poem"
"wiiiinnnnd" -> "wind"
"ttiiitllleeee" -> "title"
"cccccaaarrrbbonnnnn" -> "carbon"
"""

user_word = input("Enter a word: ")

new_word = ""

for letter in user_word:
    if not new_word or letter != new_word[-1]:
        new_word += letter

print(new_word)
