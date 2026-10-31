import random

# Daily Challenge: String

# Ask the user for a string
user_string = input("Enter a 10-character string: ")

# Check the length of the string
if len(user_string) < 10:
    print("String not long enough.")

elif len(user_string) > 10:
    print("String too long.")

else:
    print("Perfect string")

    # Print the first and last characters
    print("First character:", user_string[0])
    print("Last character:", user_string[-1])

    # Build the string character by character
    built_string = ""

    for character in user_string:
        built_string += character
        print(built_string)

    # Bonus: Shuffle the string
    characters = list(user_string)
    random.shuffle(characters)
    shuffled_string = "".join(characters)

    print("Shuffled string:", shuffled_string)