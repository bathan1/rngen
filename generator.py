import random

print("Welcome to random number generator!")
done = False
while not done:
    lower_bound = int(input("Enter desired lower bound of your randomly generated number: "))
    upper_bound = int(input("Enter desired upper (exclusive) bound of your randomly generated number: "))
    random_num = random.randrange(lower_bound, upper_bound)
    print("Your random number is", random_num)

    prompt = False
    while not prompt:
        loop = input("Need another number? (y/n) ")
        loop = loop.lower()
        if loop == 'y':
            prompt = True
            continue
        if loop == 'n':
            done = True
            break
        else:
            print("You need to enter a valid answer!")
