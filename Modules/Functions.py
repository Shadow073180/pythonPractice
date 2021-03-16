

#create a function to sum numbers of a list
def sum_list(list):
    print(sum(list))

#can functions be called inside functions?
def use_function_inside_a_function(f):
    print("The total is" + str(f))

#can a function call itself?
def function_calls_itself(number):
    while number > 0:
        number -= 1
        function_calls_itself(number)

#can variables defined in a function be used in another function?
def can_a_function_variable_be_used_in_another_function():
    print("only if you return them in the function")