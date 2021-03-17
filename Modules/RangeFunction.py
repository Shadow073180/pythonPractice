import random

# create a list of 1000 numbers
def create_list_of_1000_numbers():
    thousand_list = []
    for x in range(0,1001):
        number = random.randint(0,100)
        thousand_list.append(number)

    for number in thousand_list:
        print(number)
    return thousand_list

# get the largest and  smallest number from a list
def get_largest_and_smallest_number_from_list(collection):
    maximum = max(collection)
    minimum = min(collection)
    print(maximum)
    print(minimum)

#create and even and odd list
def create_an_even_and_odd_list():
    even = range(2,100,2)
    odd = range(1,100,2)
    print(even)
    print(odd)