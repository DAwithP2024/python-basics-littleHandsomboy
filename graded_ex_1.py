# Products available in the store by category

#working on this file
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}


def display_sorted_products(products_list, sort_order):
    return sorted(products_list, key=lambda x: x[1], reverse=(sort_order == 2))


def display_products(products_list):
    for index, (product, price) in enumerate(products_list, start=1):
        print(f"{index}. {product} - ${price}")


def display_categories():
    for index, category in enumerate(products, start=1):
        print(f"{index}. {category}")


def add_to_cart(cart, product, quantity):
    cart.append((product, quantity))

def display_cart(cart):
    pass


def generate_receipt(name, email, cart, total_cost, address):
    pass


def validate_name(name):
    parts = name.split()
    return len(parts) == 2 and all(part.isalpha() for part in parts)

def validate_email(email):
    return "@" and ".com" in email


def main():
    #Task 2 
    name = input("Please enter your name: ")
    email = input("Please enter your email address: ")
    #validate name and email
    while not validate_name(name):
        print("Invalid name. Please enter your first and last name using only letters.")
        name = input("Please enter your name: ")    
    while not validate_email(email):
        print("Invalid email address. Please include an @ sign.")
        email = input("Please enter your email: ")   
    #show categories
    display_categories()
    #choose
    category_choice = input("Please enter the category number you would like to explore: ")
    while not category_choice.isdigit() or int(category_choice) > len(products) or int(category_choice) < 1:
        print("Invalid category number. Please enter a correct number.")
        category_choice = input("Please enter the category number you would like to explore: ")
    
    category_choice = int(category_choice) - 1
    selected_category = list(products.keys())[category_choice]
    #display
    display_products(products[selected_category])   
    cart = []
    while True:
        print("\n1. Select a product to buy")
        print("2. Sort the products according to the price.")
        print("3. Go back to the category selection.")
        print("4. Finish shopping")
        choice = input("Please choose an option: ") 
        if choice == 1 :
            product_choice = input("Please enter the product number you would like to buy: ")
            while not product_choice.isdigit() or int(product_choice) > len(products[selected_category]) or int(product_choice) < 1:
                print("Invalid product number. Please enter a correct number.")
                product_choice = input("Please enter the product number you would like to buy: ")
            product_choice = int(product_choice) - 1
            product = products[selected_category][product_choice]
            quantity = int(input("Please enter the quantity you want to buy: "))
            add_to_cart(cart, product, quantity)
        elif choice == 2 :
            sorted_choose =  int(input("Choose 1 for ascending,2 for descending: "))
            sorted_products = display_sorted_products(products[selected_category], sorted_choose)
            print("Products sorted by price:")
            display_products(sorted_products)
        elif choice ==3:
            pass
        elif choice ==4:
            pass
        else:
            pass
        break
    pass
    

""" The following block makes sure that the main() function is called when the program is run. 
It also checks that this is the module that's being run directly, and not being used as a module in some other program. 
In that case, only the part that's needed will be executed and not the entire program """
if __name__ == "__main__":
    main()
