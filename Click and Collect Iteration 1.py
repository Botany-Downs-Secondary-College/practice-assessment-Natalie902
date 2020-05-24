#Click and Collect App
#Natalie, May 2020

#Initialise the variables
name = ""
age = ""

#Lists used
items = ["Sandwich $15","Toast $15","Cheese $15"]
student_account = []
chosen_item = []
sandwich = 15
toast = 15
cheese = 15

def order():
    while True:
        chosen_item = input("Please enter one item you would like to order, if you would like to cancel, enter end, if you would like to look at your cart, enter cart").strip()
        if chosen_item == "end":
            break
        if chosen_item == "cart":
            print(chosen_item)
        else:
            cart.append(chosen_item)
            
            
def menu():
    print("This is our menu:")
    print(items)



#main routine
print("""Welcome to Click and Collect program for our school! We serve fresh food ready to pick up at your convinience!""")
age = int(input("How old are you? "))
while True:
    if age < 13 or age > 18:
        print("Unfortunately, you do not meet the requirements to use our Click and Collect. This CLick and Collect app is only available for school students.")
        exit()
    else:
        break
while True:
    member = input("Please enter L for log in or N for creating a new account").upper()
    if member == "L":
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        if username and password in student_account:
                print("You have entered your password manager account")
        else:
                print("You aren't in our database or the password and username entered is incorrect")
                exit()
                break
    elif member == "N":
        username = input("Enter New Username: ")
        password = input("Enter New Password: ")
        student_account.append([username, password])
        print("Your new account has been created")
        break
    else:
        print("That was not an option, please enter L or N")
        
while True:
    start = input("To begin your order, enter order, if you would like to see our menu, enter menu: ").strip()
    if start == "menu":
        menu()
        back = input("If you would like to order enter order, or if you would like to exit enter end").strip()
        if back == "end":
            break
        elif back == "order":
            order()
    elif start == "order":
        order()
    else:
        print("wack")