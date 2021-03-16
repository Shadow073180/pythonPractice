
# ask user for number 0-10 , and if out of range return invalid number
def ask_user_for_number_0_to_10():  
    number = input("pick a number between 0 and 10.")
    if number not in range(0,11):
        print("invalid number.")
    else: 
        print(number)

# ask user for a password
def ask_user_for_password():
    password = "Please create a password."
    print(password)