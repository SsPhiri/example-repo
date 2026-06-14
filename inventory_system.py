#==================== CLASS ====================

class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        # initialise shoe attributes
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        # returns cost of shoe
        return self.cost

    def get_quantity(self):
        # returns quantity of shoe
        return self.quantity

    def __str__(self):
        # string representation of shoe object
        return (
            f'Country: {self.country}\n'
            f'Code: {self.code}\n'
            f'Product: {self.product}\n'
            f'Cost: R{self.cost:.2f}\n'
            f'Quantity: {self.quantity}\n'
        )


#==================== SHOE LIST ====================

# list to store shoe objects
shoe_list = []


#==================== FUNCTIONS ====================

def read_shoes_data():
    # reads data from file and creates Shoe objects

    import os

    try:
        file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "inventory.txt"
        )

        with open(file_path, "r") as file:

            shoe_list.clear()
            next(file)

            for line in file:

                data = line.strip().split(",")

                country = data[0]
                code = data[1]
                product = data[2]
                cost = float(data[3])
                quantity = int(data[4])

                shoe = Shoe(country, code, product, cost, quantity)
                shoe_list.append(shoe)

        print("Data loaded successfully!")

    except FileNotFoundError:
        print("Error: inventory.txt not found.")

    except Exception as e:
        print("Error reading file:", e)

def save_shoes_to_file():
    import os

    try:
        file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__))
            if "__file__" in globals() else os.getcwd(),
            "inventory.txt"
        )

        with open(file_path, "w") as file:
            # optional: rewrite header if your file has one
            file.write("country,code,product,cost,quantity\n")

            for shoe in shoe_list:
                file.write(
                    f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost:.2f},{shoe.quantity}\n"
                )

        print("Inventory updated successfully in file.")

    except Exception as e:
        print("Error saving file:", e)

def capture_shoes():
    # allows user to add a new shoe

    try:
        country = input("Enter country: ")
        code = input("Enter shoe code: ")
        product = input("Enter product name: ")
        cost = float(input("Enter cost: "))
        quantity = int(input("Enter quantity: "))

        shoe = Shoe(country, code, product, cost, quantity)
        shoe_list.append(shoe)

        print("Shoe added successfully!")

    except ValueError:
        print("Invalid input: cost and quantity must be numbers.")


from tabulate import tabulate

def view_all():

    if len(shoe_list) == 0:
        print("No shoes loaded.")
        return

    table = []

    for shoe in shoe_list:
        table.append([
            shoe.country,
            shoe.code,
            shoe.product,
            f"R{shoe.cost:.2f}",
            shoe.quantity
        ])

    headers = ["Country", "Code", "Product", "Cost", "Quantity"]

    print("\n===== INVENTORY REPORT =====")
    print(tabulate(table, headers=headers, tablefmt="grid"))


def re_stock():

    if len(shoe_list) == 0:
        print("No shoes loaded.")
        return

    lowest_quantity_shoe = shoe_list[0]

    for shoe in shoe_list:
        if shoe.get_quantity() < lowest_quantity_shoe.get_quantity():
            lowest_quantity_shoe = shoe

    print("Shoe with the lowest quantity:")
    print(lowest_quantity_shoe)

    choice = input("Do you want to restock this shoe? (yes/no): ")

    if choice.lower() == "yes":
        try:
            add_amount = int(input("Enter quantity to add: "))
            lowest_quantity_shoe.quantity += add_amount

            print("Stock updated successfully!")
            print(lowest_quantity_shoe)

            save_shoes_to_file()

        except ValueError:
            print("Invalid number entered.")


def search_shoe():
    # searches for a shoe by code

    code = input("Enter shoe code to search: ")

    for shoe in shoe_list:
        if shoe.code == code:
            print("\nShoe found:")
            print(shoe)
            return

    print("\nShoe not found.")


def value_per_item():
    # calculates and displays value of each shoe

    if len(shoe_list) == 0:
        print("No shoes loaded.")
        return

    print("\nValue of each shoe item:")
    print("-" * 30)

    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        print(f"{shoe.product} | Value: R{value:.2f}")


def highest_qty():
    # finds shoe with highest quantity

    if len(shoe_list) == 0:
        print("No shoes loaded.")
        return

    highest_quantity_shoe = shoe_list[0]

    for shoe in shoe_list:
        if shoe.get_quantity() > highest_quantity_shoe.get_quantity():
            highest_quantity_shoe = shoe

    print("Shoe with the highest quantity:")
    print(highest_quantity_shoe)

    print(f"{highest_quantity_shoe.product} is ON SALE!")


#==================== MAIN MENU ====================
# Load data automatically when program starts
read_shoes_data()

while True:

    print("\n===== NIKE STOCK SYSTEM =====")
    print("1. View all shoes")
    print("2. Add new shoe")
    print("3. Search shoe by code")
    print("4. Show lowest quantity (restock)")
    print("5. Show highest quantity")
    print("6. Show value of each shoe")
    print("7. Load shoes from file")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_all()

    elif choice == "2":
        capture_shoes()

    elif choice == "3":
        search_shoe()

    elif choice == "4":
        re_stock()

    elif choice == "5":
        highest_qty()

    elif choice == "6":
        value_per_item()

    elif choice == "7":
        read_shoes_data()

    elif choice == "0":
        print("Exiting system... Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
