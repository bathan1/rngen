import random

print("Welcome to random number generator!")
lower_bound = int(input("Enter desired lower bound of your randomly generated number: "))
upper_bound = int(input("Enter desired upper (exclusive) bound of your randomly generated number: "))
random_num = random.randrange(lower_bound, upper_bound)
print("Your random number is", random_num)