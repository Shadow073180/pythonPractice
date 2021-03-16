

# print countries in a list
def output_countries_in_list():
    clist = ['Canada','USA','Mexico','Australia']
    for country in clist:
        print(country)

# create loop that loop from 0 to 10
def create_loop_from_0_to_10():
    for num in range(0,11):
        print(num)

# multplication table


# print numbers 1 to 10 backwards using a for loop
def print_numbers_one_to_ten_backwards_with_loop(collection):
    count = len(collection) - 1
    while count >= 0:
        for num in collection:
            print(collection[count])
            count - 1

# count all even number from 0 to 10
def even_numbers_from_0_to_10():
    for number in range(1,11):
        if number % 2 == 0:
            print(number)

# sum the numbers from 100-200
def sum_the_numbers_from_100_to_200():
    sum = 0
    for number in range(100,201):
        sum += number
    print(sum)