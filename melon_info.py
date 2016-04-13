"""
Prints out all the melons in our inventory
"""

from melons import melon_data
#
#
# def print_melon(melon_name):
#     """This function takes the name of a melon and prints it's data from the melon_data dictionary"""
#     melon_name = str(melon_name)
#     have_or_have_not = 'have'
#     if melon_data[melon_name]["Seedlessness"] == True
#         have_or_have_not = 'do not have'
#
#
#     print "{}s {} seeds and are ${:.2f}".format(melon_data[melon_name], have_or_have_not, melon_data["Price"])
#
#
# for i in melon_names:
#     print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])


def melon_types():
    """This function returns a list of all melons used as keys in the Melon Dictionary"""
    names = []
    for fruit in melon_data:
        names.append(fruit)
    return names


def parent_interface():
    """This function is the main decision tree"""
    print "\n"
    print "Please select one of the following options:"
    print "1 - Look up info by Melon Name"
    print "2 - See a list of Melon Names"
    print "3 - Exit"
    choice = raw_input("Choice - ")

    while True:
        if choice == "1":
            print "\n"
            print melon_lookup()
            parent_interface()

        elif choice == "2":
            print "\n"
            melon_output = sorted(melon_types())
            for melon in melon_output:
                print melon
            parent_interface()
        elif choice == "3":
            print "\n"
            print "Thank you for choosing Ubermelon! Goodbye!"
            break
        else:
            print "\n"
            print "That's not a valid option, please try again."
            parent_interface()


def melon_lookup():
    """this function takes a melon name and evaluates if it is a key in the Melon Dictionary, returning info if it is"""
    melon_name = raw_input("What is the name of the Melon you'd like info about? - ")
    if melon_name in melon_types():
        return melon_output(melon_name)

    elif melon_name == "Back" or "back":
        parent_interface()
    else:
        print "That's not a valid choice, please try another type of melon or type 'back' to go back to the " \
              "previous menu."
        parent_interface()


def melon_output(melon_name):
    """This function takes the name of a melon in the dictionary and prints the data about it"""
    for melon, attributes in melon_data.items():
        for category, value in attributes.items():
             print category, ":", value
        break




print "Hello, welcome to Ubermelon's Melon info tracker."
parent_interface()


