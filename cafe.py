class CafeManagementSystem:
    def __init__(self):
        self.menu = {
            "Coffee": 2.50,
            "Tea": 2.00,
            "Sandwich": 5.00,
            "Cake": 3.50
        }
        self.orders = []

    def display_menu(self):
        print("\n--- Cafe Menu ---")
        for item, price in self.menu.items():
            print(f"{item}: ${price:.2f}")
        print()

    def take_order(self):
        print("\nEnter 'done' when you finish ordering.")
        while True:
            item = input("Enter item name: ").capitalize()
            if item == "Done":
                break
            elif item in self.menu:
                quantity = int(input(f"How many {item}s would you like? "))
                self.orders.append((item, quantity))
            else:
                print("Item not available in the menu. Please try again.")

    def generate_bill(self):
        print("\n--- Bill ---")
        total = 0
        for item, quantity in self.orders:
            price = self.menu[item]
            cost = price * quantity
            total += cost
            print(f"{item} x {quantity} = ${cost:.2f}")
        print(f"\nTotal: ${total:.2f}")
        print("Thank you for visiting the cafe!")

    def run(self):
        while True:
            print("\n--- Cafe Management System ---")
            print("1. Display Menu")
            print("2. Take Order")
            print("3. Generate Bill")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                self.display_menu()
            elif choice == "2":
                self.take_order()
            elif choice == "3":
                self.generate_bill()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Run the Cafe Management System
if __name__ == "__main__":
    cms = CafeManagementSystem()
    cms.run()
