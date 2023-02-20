
#   ========The beginning of the class==========
#   Defines Shoe class


class Shoe:

    def __init__(self, country, code, product, cost, quantity):

        self.country = country    # Attributes for: country
        self.code = code          # code
        self.product = product    # product
        self.cost = cost          # cost
        self.quantity = quantity  # quantity


# Functions below return the values of the shoe.
    def get_country(self):
        return self.country

    def get_code(self):
        return self.code

    def get_product(self):
        return self.product

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, new_quantity):
        self.quantity = new_quantity

    #   Returns a string representation of the class
    def __str__(self):
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}\n"


# =============Shoe list===========
inventory_read = open("inventory.txt", "r")
inventory_write = open("inventory.txt", "a+")

shoe_list = []
shoe_object = []
# ==========Functions outside the class==============


def read_shoes_data():
    file = None
    try:
        #   Splits up text file: country, code, product, cost, quantity
        for line in inventory_read:
            inventory_strip = line.strip("\n")
            inventory_split = inventory_strip.split(",")  # Split at element
            shoe_list.append(inventory_split)

        #   Takes country, code, product, cost, quantity and writes to object.
        for i in range(1, len(shoe_list)):
            element = shoe_list[i]
            shoe = Shoe(element[0], element[1], element[2], element[3], int(element[4]))
            shoe_object.append(shoe)

    except FileNotFoundError as error:
        print("\nFile not found\n")
        print(error)

    finally:
        if file is not None:
            file.close()


def capture_shoes():

    def capture_copy():
        # Create an entry to inventory from code.

        file = None

        try:
            capture_code = input("\nPlease enter the code you are searching for:\n\n")
            for line in shoe_object:
                if line.get_code() == capture_code:
                    temp_capture = line.get_code(), line.get_product()
                    print(f"You have selected: {temp_capture}")
                    country_capture = input(f"Country: ")
                    print(f"Code and product are {line.get_code()} and {line.get_product()}")
                    cost_capture = input(f"Cost: ")
                    quantity_capture = input(f"Quantity: ")
                    inventory_write.write(f'\n{country_capture},{line.get_code()},'
                                          f'{line.get_product()},{cost_capture},{quantity_capture}')
                    print("\nData written\n")
                    inventory_write.close()
                    break

        except FileNotFoundError as error:
            print("\nSorry, file not found.2\n")
            print(error)

        finally:
            if file is not None:
                file.close()

    def capture_new():
        #   Create an entry to inventory from inputting all data.

        file = None

        try:
            country_capture = input("Please enter Country:\n")
            code_capture = input("Please enter product code:\n")
            product_capture = input("Please enter product name:\n")
            cost_capture = int(input("Please enter product cost\n"))
            quantity_capture = int(input("Please enter product quantity\n"))

            shoe_capture = Shoe(country_capture, code_capture, product_capture, cost_capture, quantity_capture)
            shoe_object.append(shoe_capture)

            inventory_write.write(
                f'\n{country_capture},{code_capture},{product_capture},{cost_capture},{quantity_capture}')
            print("\nData written\n")
            inventory_write.close()

        except FileNotFoundError as error:
            print("\nSorry, file not found.2\n")
            print(error)

        finally:
            if file is not None:
                file.close()

    #   Menu asking user how to add to inventory list.
    print("This function allows you to add to the stock inventory list.\n\n" 
          "You can either:\n")
    capture_choice = int(input("1 - Create from product code\n"
                               "2 - Create from scratch\n"
                               "3 - Exit and go back to Menu\n"))
    if capture_choice == 1:
        capture_copy()

    elif capture_choice == 2:
        capture_new()

    elif capture_choice == 3:
        menu()

    else:
        print("\nSorry I didn't understand that\n")
        capture_shoes()


#   Prints a list of all stock including where it is, cost and quantity.
def view_all():

    file = None

    try:

        print("\n--------------------Stock--------------------------\n")

        for i in shoe_object:
            print(
                f"Country: {i.country}, Code:{i.code}, Product: {i.product}, Cost:{i.cost}, Quantity:{i.quantity}")

        print("\n--------------------------------------------------\n")

    except FileNotFoundError as error:
        print("\nFile not found\n")
        print(error)

    finally:
        if file is not None:
            file.close()


#   Takes 4 lowest stock items and allows user to order more stock
def re_stock():
    file = None

    restock_list = []

    try:
        shoe_object.sort(key=lambda x: x.quantity)

        for i in range(1, 5):
            restock_list.append(shoe_object[i])

        #   User chooses which item to restock
        print("\n-------Low Stock----------\n")
        for i in restock_list:
            print(f"Country: {i.country}, Code:{i.code}, Product: {i.product}, Cost:{i.cost}, Quantity:{i.quantity}")
        print("\n------------------------------\n")

        input_index = int(input("\nType the index of the product you wish to restock:\n"))
        input_quantity = int(input("\nQuantity needed:\n"))
        shoe_object[input_index].set_quantity(input_quantity)

        output = ''
        for element in shoe_object:
            output += (
                f'{element.get_country()},{element.get_code()},{element.get_product()},{element.get_cost()},'
                f'{element.get_quantity()}\n')

        inventory_write_test = open("inventory.txt", "w")
        inventory_write_test.write(output)
        inventory_write_test.close()

        print("\nYour product has been ordered")

    except FileNotFoundError as error:
        print("\nFile not found\n")
        print(error)

    finally:
        if file is not None:
            file.close()


#   Search shoe by code
def search_shoe():
    search_shoe = input("\nPlease enter the code you are searching for:\n\n")

    for line in shoe_object:
        if line.get_code() == search_shoe:
            print(f'\n {line}')

    print("\nPlease select another option from the menu below\n")


#   List values of items
def value_per_item():
    for line in shoe_object:
        value = int(line.get_cost()) * int(line.get_quantity())
        print(f'{line.get_code()} Value: {value}\n')


#   Looks for item with most stock and puts it on same.
def highest_quantity():
    highest_quantity = []

    for line in shoe_object:
        highest_quantity.append(line)

    print("\n----------------Highest stock quantity----------------\n")

    print(max(shoe_object, key=lambda item: item.quantity))
    print("\nThis item has now on sale\n")
    menu()
# =================================================== #


# ==========Main Menu=============
def menu():
    read_shoes_data()
    while True:

        try:
            menu = int(input('''\n
            
                Nike Inventory Menu
                ===================
            
    Please select from the options below:
                
    1. View All
    2. Add to inventory
    3. Restock
    4. Search
    5. Item Values
    6. Sale Items
                \n'''))

            if menu == 1:
                view_all()

            elif menu == 2:
                capture_shoes()

            elif menu == 3:
                re_stock()

            elif menu == 4:
                search_shoe()

            elif menu == 5:
                value_per_item()

            elif menu == 6:
                highest_quantity()

            else:
                print("\n Sorry I didn't get that. Please input option again.\n")

        except ValueError:
            print("\nSorry I didn't get that. Please input option again.\n")


# ============================================ #
menu()
