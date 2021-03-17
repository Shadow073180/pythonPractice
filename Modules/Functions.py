

#create a function to sum numbers of a list
def sum_list(list):
    print(sum(list))

#can functions be called inside functions?
def use_function_inside_a_function():
    i = 3
    def get_i(i):
        i += 40
    print(i)

#can a function call itself?
def function_calls_itself(number):
    if number == 0:
        print(0)
    else:
        function_calls_itself(number - 1)
    

#can variables defined in a function be used in another function?
def can_a_function_variable_be_used_in_another_function():
    print("only if you return them in the function")