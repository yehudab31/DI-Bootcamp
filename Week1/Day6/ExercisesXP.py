
"""
Exercise 1: Favorite Numbers

Instructions:
- Create a set called my_fav_numbers and populate it with your favorite numbers.
- Add two new numbers to the set.
- Remove the last number you added to the set.
- Create another set called friend_fav_numbers and populate it with your friend's favorite numbers.
- Concatenate both sets to create our_fav_numbers.
- Sets are unordered and do not allow duplicates.
"""

my_fav_numbers = {7, 10, 18}

my_fav_numbers.add(25)
my_fav_numbers.add(30)

my_fav_numbers.remove(30)

friend_fav_numbers = {3, 7, 15, 20}

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print(our_fav_numbers)


"""
Exercise 2: Tuple

Instructions:
- Given a tuple of integers, try to add more integers to the tuple.
- Hint: Tuples are immutable, meaning they cannot be changed after creation.
- Think about why you can't add more integers to a tuple.
"""

my_tuple = (1, 2, 3, 4, 5)

# Tuples cannot be modified directly.
# However, we can create a new tuple by combining two tuples.

my_tuple = my_tuple + (6, 7)

print(my_tuple)


"""
Exercise 3: List Manipulation

Instructions:
- Create a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
- Remove "Banana" from the list.
- Remove "Blueberries" from the list.
- Add "Kiwi" to the end of the list.
- Add "Apples" to the beginning of the list.
- Count how many times "Apples" appear in the list.
- Empty the list.
- Print the final state of the list.
"""

basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana")
basket.remove("Blueberries")

basket.append("Kiwi")
basket.insert(0, "Apples")

print("Number of apples:", basket.count("Apples"))

basket.clear()

print("Final basket:", basket)


"""
Exercise 4: Floats

Instructions:
- Explain what a float is and how it differs from an integer.
- Create a list containing:
  1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5
- Avoid hard-coding each number manually.
- Generate the sequence using a loop or another method.

A float is a number with a decimal point (e.g., 2.5 or 3.0).
An integer is a whole number without a decimal point (e.g., 2 or 3).
"""

numbers = []

# Start at 3 because 3/2 = 1.5, and stop at 10 because 10/2 = 5.
# range(3, 11) includes 3 through 10.
for i in range(3, 11):
    number = i / 2

    if number.is_integer():
        numbers.append(int(number))
    else:
        numbers.append(number)

print(numbers)


"""
Exercise 5: For Loop

Instructions:
- Write a for loop to print all numbers from 1 to 20, inclusive.
- Write another for loop that prints every number from 1 to 20
  where the index is even.
"""

# Part 1: Print numbers from 1 to 20
for i in range(1, 21):
    print(i)

# Part 2: Print numbers at even indexes
for index, number in enumerate(range(1, 21)):
    if index % 2 == 0:
        print(number)


"""
Exercise 6: While Loop

Instructions:
- Ask the user to enter their name.
- Use a while True loop to check if the name is valid.
- The name must not contain digits and must be at least 3 letters long.
- Hint: Use the isdigit() method.
- If the input is incorrect, keep asking.
- If the input is correct, print "thank you" and break the loop.
"""

while True:
    name = input("Enter your name: ").strip()

    # isalpha() is stricter than isdigit() because it rejects
    # mixed letters and numbers, as well as other non-letter characters.
    if len(name) < 3 or not name.isalpha():
        print("Invalid name. Please enter at least 3 letters with no numbers.")
    else:
        print("thank you")
        break


"""
Exercise 7: Favorite Fruits

Instructions:
- Ask the user to input their favorite fruits, separated by spaces.
- Store these fruits in a list.
- Ask the user to input the name of any fruit.
- If the fruit is in their list, print:
  "You chose one of your favorite fruits! Enjoy!"
- If not, print:
  "You chose a new fruit. I hope you enjoy it!"
"""

favorite_fruits = input("Enter your favorite fruits separated by spaces: ").lower().split()

chosen_fruit = input("Enter any fruit: ").lower().strip()

if chosen_fruit in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")


"""
Exercise 8: Pizza Toppings

Instructions:
- Write a loop that asks the user to enter pizza toppings one by one.
- Stop the loop when the user types 'quit'.
- For each topping entered, print:
  "Adding [topping] to your pizza."
- After exiting the loop, print all the toppings and the total cost.
- Base price is $10, and each topping adds $2.50.
"""

toppings = []
base_price = 10
topping_price = 2.50

while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ").strip().lower()

    if topping == "quit":
        break

    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")

total_price = base_price + (len(toppings) * topping_price)

print("Your toppings:", ", ".join(toppings))
print(f"Total cost: ${total_price:.2f}")


"""
Exercise 9: Cinemax Tickets

Instructions:
- Ask for the age of each person in a family.
- Calculate the total ticket cost:
  - Under 3: Free
  - Ages 3 to 12: $10
  - Over 12: $15
- Print the total ticket cost.
"""

total_cost = 0

while True:
    age = input("Enter age (or 'quit' to finish): ")

    if age.lower() == "quit":
        break

    if not age.isdigit():
        print("Please enter a valid age.")
        continue

    age = int(age)

    if age < 3:
        total_cost += 0
    elif age <= 12:
        total_cost += 10
    else:
        total_cost += 15

print(f"Total ticket cost: ${total_cost}")


"""
Exercise 9 Bonus: Restricted Movie

Instructions:
- Ask for each person's age.
- Only people aged 16 to 21 are allowed to watch.
- Remove anyone who isn't allowed.
- Print the final list of attendees.
"""

ages = []

while True:
    age = input("Enter age (or 'quit' to finish): ")

    if age.lower() == "quit":
        break

    if not age.isdigit():
        print("Please enter a valid age.")
        continue

    ages.append(int(age))

ages = [age for age in ages if 16 <= age <= 21]

print("Final attendees:", ages)
