#!/bin/python 3.8.7
import random
import time
from Modules import *


print("-------------------SECTION1-----------------------------")
name = "David Masterson"

printName(name)

lyrics = "These are lyrics to a song"

displayLyrics(lyrics)

print("----------------SECTION2--------------------------------")

numbers = [1,2,3,4,5]

show_numbers_of_list(numbers)
sum_sixty_four_and_thirty_two()

x = 32
y = 64

sum_x_and_y

print("----------------SECTION3--------------------------------")

actor = "Nicholas Cage"

my_favorite_actor(actor)
print_lucky_with_substitution()
print_date_2_2_2016_with_substitution

print("-----------------SECTION4-------------------------------")

statement = "Hello person, I am david"

replace_string_in_statement(statement,"person","user")

statement2 = "Hello person, I am person"
can_a_string_be_replaced_twice(statement,"person","David")

can_we_replace_phrase(statement2,"I am person", "It is a pleasure to meet you.")

print("------------------SECTION5------------------------------")

statement = "This will tell me if find is case sesitive"

is_find_case_sensitive(statement,"Case")

statement = "This will tell me if will find case case twice"

what_happens_when_word_is_present_twice(statement,"case")

print("TODO still working on 3rd exercise.")

print("------------------SECTION6------------------------------")

words = ["test","a","new","language"]
join_words_of_a_collection(words)
join_words_of_collection_with_underscore_seperator(words)

print("--------------------SECTION7----------------------------")

sentence = "This is to see if a string can be split / at multiple places."
can_you_split_on_multiple_characters(sentence," " and "/")

words = "World,Earth,America,Canada"
split_this_string(words,",")

article = ''' This ia a single sentence. and this is the ending of the first line.
            I am just typing to type.
            This is another section that has nothing to do with the first.'''
split_article_on_section(article)

print("---------------------SECTION8---------------------------")

assign_random_to_variable()
print_three_random_numbers()
create_100_randoms_get_freq_of_each()

print("---------------------SECTION9---------------------------")

get_phone_number_from_user()
# get_favorite_programming_language_from_user()

print("--------------------SECTION10----------------------------")

ask_user_for_number_0_to_10()
# ask_user_for_password()

print("--------------------SECTION11----------------------------")

output_countries_in_list()
create_loop_from_0_to_10()

numbers = [1,2,3,4,5,6,7,8,9,10]
print_numbers_one_to_ten_backwards_with_loop(numbers)

even_numbers_from_0_to_10()
sum_the_numbers_from_100_to_200()

print("---------------------SECTION12---------------------------")

# print items of list using while loop
clist = ["Canada","USA","Mexico"]
output_items_in_list_with_while_loop(clist)

difference_between_for_and_while_loops()
can_you_sum_the_numbers_in_a_while_loop()
can_a_loop_be_used_in_a_while_loop()


print("---------------------SECTION13---------------------------")

my_list = [1,2,3,4,5]
sum_list(my_list)

use_function_inside_a_function()
function_calls_itself(20)
can_a_function_variable_be_used_in_another_function()

print("--------------------SECTION14----------------------------")

create_a_list_of_states_and_only_return_those_starting_with_m()

print("--------------------SECTION15----------------------------")

nums = [6,4,2]
add_numbers_12_18_and_4_to_list(nums)
change_second_item_to_3(nums)

print("--------------------SECTION16----------------------------")

"TODO"
"TODO"

print("--------------------SECTION17----------------------------")

num = create_list_of_1000_numbers()
get_largest_and_smallest_number_from_list(num)
create_an_even_and_odd_list()

print("-------------------SECTION18-----------------------------")

countries = create_dictionay_of_coutries()
print_keys_of_dictionay(countries)
print_values_of_dictionary(countries)

print("-------------------SECTION19-----------------------------")

read_file_and_number_every_line("test.txt")
what_happens_when_file_doesnt_exist("../nothing.txt")

print("-------------------SECTION20-----------------------------")

write_to_file("test.txt","Take it easy!")
write_to_file("another.txt",open("test.txt"))

print("-------------------SECTION21-----------------------------")

output_ever_position_of_a_3_by_3_tic_tac_toe_board()

players = ["John", "Marissa", "Pete", "Dayton"]
player_matchup(players)

answer_steps_taken()

print("-------------------SECTION22-----------------------------")

people = ["John", "Marissa", "Pete", "Dayton"]
take_a_slice(people)

slice_world()

print("-------------------SECTION23-----------------------------")

num = 40
reduce_variable(num)

has_local_variable()

print("-------------------SECTION24-----------------------------")

get_date_year_month_day()

print("-------------------SECTION25-----------------------------")

print("yes")
print("yes if it is a file not found exception")
print("Where there isn't a condition that could throw and exception.")

print("-------------------SECTION26-----------------------------")

print("yes")
print("yes that is what a class is used for.")
print("no")
auto = Auto("red","automatic")
auto.open_door()

print("-------------------SECTION27-----------------------------")

person1 = Person(40,"male", "David")

print(person1.age)
person1.set_age(33)
person1.get_age()

print("-------------------SECTION28-----------------------------")

math_sin(35)

print("-------------------SECTION29-----------------------------")

corvettte = Car("sports",0)
corvettte.open_door()
corvettte.start_engine()

print("-------------------SECTION30-----------------------------")

print("yes")
Dog.bark()

print("It can be indication of poor design.")

print("-------------------SECTION31-----------------------------")

print("An iteratable is a Python object that can be used as a sequence. You can go to the next item of the sequence using the next() method.")
print("Lists, Strings, Dictionaries, and Sets")

print("-------------------SECTION32-----------------------------")

print("A class method is a method shared among all objects")
print("Class method the parameter is always itself, in static methods the method doesn't even know about the class.")

print("-------------------SECTION33-----------------------------")

print("Not all languages support multi-inheritance.")
print("It increases complexity and makes it harder to be reuseable")
print("No")
