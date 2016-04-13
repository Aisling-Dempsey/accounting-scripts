"""
Prints out all the melons in our inventory
"""

from melons import melon_data


def melon_types():
    """This function returns a list of all melons used as keys in the Melon Dictionary"""
    names = []
    for fruit in melon_data:
        names.append(fruit)
    return names


def parent_interface():
    """This function is the main decision tree"""

    # presents options for the user to choose
    print "\n"
    print "Please select one of the following options:"
    print "1 - Look up info by Melon Name"
    print "2 - See a list of Melon Names"
    print "3 - Exit"
    choice = raw_input("Choice - ")

    # loops through the menu until user exits
    while True:
        # allows user to look up info by melon name
        if choice == "1":
            print "\n"
            print melon_lookup()
            parent_interface()

        # prints a list of the melon names if they don't know one offhand
        elif choice == "2":
            print "\n"
            melon_output = sorted(melon_types())
            for melon in melon_output:
                print melon
            parent_interface()

        # exits the program
        elif choice == "3":
            print "\n"
            print "Thank you for choosing Ubermelon! Goodbye!"
            break

        # if user enters something other than 1, 2 or 3
        else:
            print "\n"
            print "That's not a valid option, please try again."
            parent_interface()


def melon_lookup():
    """this function takes a melon name and evaluates if it is a key in the Melon Dictionary, returning info if it is"""
    melon_name = raw_input("What is the name of the Melon you'd like info about? - ")
    # checks if the melon in the user input is already in the list of melon types, and if so, passes that as a key to to
    # the melon_output function
    if melon_name in melon_types():
        return melon_output(melon_name)
    # returns the user to the parent menu if they choose 'back' or 'Back'
    elif melon_name == "Back" or "back":
        parent_interface()
    # catches all other responses and states that they're an invalid input, then calls the function again.
    else:
        print "That's not a valid choice, please try another type of melon or type 'back' to go back to the " \
              "previous menu."
        melon_lookup()


def melon_output(melon_name):
    """This function takes the name of a melon in the dictionary and prints the data about it"""
    # assigns 'melon' and 'attributes' to each the key/value pair in the 'melon_data' dictionary, and then 'category'
    # and 'value' for each key/value pair in the 'attributes' dictionary nested as a value inside 'melon_data'.
    # Prints each key/value pair in a readable format.
    for melon, attributes in melon_data.items():
        for category, value in attributes.items():
            print category, ":", value
        break

# SALUTATIONS!
print "Hello, welcome to Ubermelon's Melon info tracker."
parent_interface()
