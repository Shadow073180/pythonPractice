

# find out if find is case sensitive
def is_find_case_sensitive(statement,find_string):

    if statement.find("Case") == True :
        print(True)
    else:
        print(False)

# What haappens when the word is there twice using find.

def what_happens_when_word_is_present_twice(statement,find_string):
    result = statement.find(find_string)
    print(result)


# Get input from user and querry the results.
# value = input("What is the weather like today? (rainy,cloudy, or sunny)?")
# print(value)