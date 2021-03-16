import random

# assign a random number to a variable.
def assign_random_to_variable():
    number = random.random()
    print(number)

# print 3 random numbers
def print_three_random_numbers():
    for num in range(3):
        print(random.randint(0,10))

# create 100 random numbers and get frequency of each.
def create_100_randoms_get_freq_of_each():
    numbers = []
    for num in range(0,100):
        number = random.randint(0,100)
        numbers.append(number)

    number_freq = {}
    for number_key in numbers:
        if number_key in number_freq:
            number_freq[number_key] += 1
        else:
            number_freq[number_key] = 1

    print(number_freq)