#!/bin/python3 3.8.2
import random
import time
from Modules import *


print("\n-------------------SECTION1-RunPythonPrograms----------\n")

name = "David Masterson"
printName(name)
lyrics = "These are lyrics to a song"
displayLyrics(lyrics)

print("\n----------------SECTION2--Variables-------------------\n")

numbers = [1,2,3,4,5]
show_numbers_of_list(numbers)
sum_sixty_four_and_thirty_two()
x = 32
y = 64
sum_x_and_y

print("\n----------------SECTION3-----Strings------------------\n")

actor = "Nicholas Cage"
my_favorite_actor(actor)
print_lucky_with_substitution()
print_date_2_2_2016_with_substitution

print("\n-----------------SECTION4---String Replace-----------\n")

statement = "Hello person, I am david"
replace_string_in_statement(statement,"person","user")
statement2 = "Hello person, I am person"
can_a_string_be_replaced_twice(statement,"person","David")
can_we_replace_phrase(statement2,"I am person", "It is a pleasure to meet you.")

print("\n------------------SECTION5---String Find-------------\n")

statement = "This will tell me if find is case sesitive"
is_find_case_sensitive(statement,"Case")
statement = "This will tell me if will find case case twice"
what_happens_when_word_is_present_twice(statement,"case")
print("TODO still working on 3rd exercise.")

print("\n------------------SECTION6--String Join--------------\n")

words = ["test","a","new","language"]
join_words_of_a_collection(words)
join_words_of_collection_with_underscore_seperator(words)

print("\n--------------------SECTION7-String Split------------\n")

sentence = "This is to see if a string can be split / at multiple places."
can_you_split_on_multiple_characters(sentence," " and "/")
words = "World,Earth,America,Canada"
split_this_string(words,",")
article = ''' This ia a single sentence. and this is the ending of the first line.
            I am just typing to type.
            This is another section that has nothing to do with the first.'''
split_article_on_section(article)

print("\n---------------------SECTION8-Random Numbers---------\n")

assign_random_to_variable()
print_three_random_numbers()
create_100_randoms_get_freq_of_each()

print("\n---------------------SECTION9-Keyboard Inputs--------\n")

get_phone_number_from_user()
get_favorite_programming_language_from_user()

print("\n--------------------SECTION10-If Statements----------\n")

ask_user_for_number_0_to_10()
ask_user_for_password()

print("\n--------------------SECTION11-For Loops--------------\n")

output_countries_in_list()
create_loop_from_0_to_10()
numbers = [1,2,3,4,5,6,7,8,9,10]
print_numbers_one_to_ten_backwards_with_loop(numbers)
even_numbers_from_0_to_10()
sum_the_numbers_from_100_to_200()

print("\n---------------------SECTION12-While Loops-----------\n")


clist = ["Canada","USA","Mexico"]
output_items_in_list_with_while_loop(clist)
difference_between_for_and_while_loops()
can_you_sum_the_numbers_in_a_while_loop()
can_a_loop_be_used_in_a_while_loop()


print("\n---------------------SECTION13-Functions-------------\n")

my_list = [1,2,3,4,5]
sum_list(my_list)
use_function_inside_a_function()
function_calls_itself(20)
can_a_function_variable_be_used_in_another_function()

print("\n--------------------SECTION14-Lists------------------\n")

create_a_list_of_states_and_only_return_those_starting_with_m()

print("\n--------------------SECTION15-List Operations--------\n")

nums = [6,4,2]
add_numbers_12_18_and_4_to_list(nums)
change_second_item_to_3(nums)

print("\n--------------------SECTION16-Sorting Lists----------\n")
col = [ (3,6),(4,7),(5,9),(8,4),(3,1)]
sort_list_with_pairs_on_first_element(col)
sort_list_with_pairs_on_second_element(col)

print("\n--------------------SECTION17-Range Functions--------\n")

num = create_list_of_1000_numbers()
get_largest_and_smallest_number_from_list(num)
create_an_even_and_odd_list()

print("\n-------------------SECTION18-Dictionary--------------\n")

countries = create_dictionay_of_coutries()
print_keys_of_dictionay(countries)
print_values_of_dictionary(countries)

print("\n-------------------SECTION19-Read File---------------\n")

read_file_and_number_every_line("test.txt")
what_happens_when_file_doesnt_exist("../nothing.txt")

print("\n-------------------SECTION20-Write File--------------\n")

write_to_file("test.txt","Take it easy!")
write_to_file("another.txt",open("test.txt"))

print("\n-------------------SECTION21-Nested Loops------------\n")

output_ever_position_of_a_3_by_3_tic_tac_toe_board()
players = ["John", "Marissa", "Pete", "Dayton"]
player_matchup(players)
answer_steps_taken()

print("\n-------------------SECTION22-Slices------------------\n")

people = ["John", "Marissa", "Pete", "Dayton"]
take_a_slice(people)
slice_world()

print("\n-------------------SECTION23-Multiple Return---------\n")

multi_return(4,5)
return_five_variables()

print("\n-------------------SECTION24-Scope--------------------\n")

num = 40
reduce_variable(num)
has_local_variable()

print("\n-------------------SECTION25-Time And Date-----------\n")

get_date_year_month_day()

print("\n-------------------SECTION26-Try Except--------------\n")

print("yes")
print("yes if it is a file not found exception")
print("Where there isn't a condition that could throw and exception.")

print("\n-------------------SECTION27-Class-------------------\n")

print("yes")
print("yes that is what a class is used for.")
print("no")
auto = Auto("red","automatic")
auto.open_door()

print("\n-------------------SECTION28-Getter And Setter-------\n")

person1 = Person(40,"male", "David")
print(person1.age)
person1.set_age(33)
person1.get_age()

print("\n-------------------SECTION29-Modules-----------------\n")

math_sin(35)

print("\n-------------------SECTION30-Inheritance-------------\n")

corvettte = Car("sports",0)
corvettte.open_door()
corvettte.start_engine()

print("\n-------------------SECTION31-Static Method-----------\n")

print("yes")
Dog.bark()
print("It can be indication of poor design.")

print("\n-------------------SECTION32-Iterable----------------\n")

print("An iteratable is a Python object that can be used as a sequence. You can go to the next item of the sequence using the next() method.")
print("Lists, Strings, Dictionaries, and Sets")

print("\n-------------------SECTION33-Class Method------------\n")

print("A class method is a method shared among all objects")
print("Class method the parameter is always itself, in static methods the method doesn't even know about the class.")

print("\n-------------------SECTION34-Multiple Inheritance----\n")

print("Not all languages support multi-inheritance.")
print("It increases complexity and makes it harder to be reuseable")
print("No")
