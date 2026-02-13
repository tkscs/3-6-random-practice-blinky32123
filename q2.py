# Make a random pet.
import random
# Choose:
# Type of animal (at least 3 choices, string)
animal = ["dog", "cat", "parrot"]#REPLACE THIS WITH YOUR CODE
animal=(random.choices(animal, k=1))
# Age (integer)
age = ["1", "5", "9"]#REPLACE THIS WITH YOUR CODE
age=(random.choices(age, k=1))
# Color (at least 3 choices, string)
#animal = None#REPLACE THIS WITH YOUR CODE
# Weight (float)
weight = ["10", "100", "1000"]#REPLACE THIS WITH YOUR CODE
weight=(random.choices(weight, k=1))

# Print a summary of your pet using an f-string
print(f"Your pet is a {animal} that weighs {weight} pounds and is {age} old")#REPLACE THIS WITH YOUR CODE