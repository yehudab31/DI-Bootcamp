
"""
Challenge 1: Letter Index Dictionary

Goal:
Create a dictionary that stores the indices (positions) of each letter
in a word provided by the user.

Instructions:
1. Ask the user to enter a word and store it in a variable.
2. Iterate through each character of the word using a loop.
3. Check if the character is already a key in the dictionary.
   - If it is, append the current index to the existing list.
   - If it is not, create a new key with a list containing the index.
4. Ensure dictionary keys are strings and values are lists.
5. Print the completed dictionary.

Examples:
"dodo" -> {"d": [0, 2], "o": [1, 3]}
"froggy" -> {"f": [0], "r": [1], "o": [2], "g": [3, 4], "y": [5]}
"grapes" -> {"g": [0], "r": [1], "a": [2], "p": [3], "e": [4], "s": [5]}
"""

word = input("Enter a word: ")

letter_indices = {}

for index, letter in enumerate(word):
    if letter in letter_indices:
        letter_indices[letter].append(index)
    else:
        letter_indices[letter] = [index]

print(letter_indices)


"""
Challenge 2: Affordable Items

Goal:
Create a program that prints a list of items that can be purchased
with a given amount of money.

Instructions:
1. Use a dictionary called items_purchase containing item names
   and prices as strings with dollar signs.
2. Use a string called wallet representing the available money.
3. Remove dollar signs and commas from prices and wallet.
4. Create a list called basket.
5. Go through the items in dictionary order (priority order).
6. If an item is affordable, add it to basket and subtract its
   price from the remaining wallet.
7. If basket is empty, print "Nothing".
8. Otherwise, print basket in alphabetical order.
"""

items_purchase = {
    "Water": "$1",
    "Bread": "$3",
    "TV": "$1,000",
    "Fertilizer": "$20"
}

wallet = "$300"

# Convert wallet from a string to an integer
wallet = int(wallet.replace("$", "").replace(",", ""))

basket = []

# Check items in priority order
for item, price in items_purchase.items():
    price = int(price.replace("$", "").replace(",", ""))

    if price <= wallet:
        basket.append(item)
        wallet -= price

# Print the final result
if basket:
    print(sorted(basket))
else:
    print("Nothing")
