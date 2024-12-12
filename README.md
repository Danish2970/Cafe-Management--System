Cafe Management System

Overview

The Cafe Management System is a Python-based application designed to facilitate the operations of a cafe. The system provides functionality to display a menu, take customer orders, generate bills, and exit the application. Each function of the system has been meticulously implemented to ensure a seamless user experience.

Functionality

Initialization (__init__)

The system initializes with a predefined menu of items and their respective prices.
An empty list, orders, is created to store customer orders during each session.

Display Menu (display_menu)

Displays the cafe's menu in a user-friendly format.
Lists all available items along with their prices.
Provides a clear overview of the offerings to the user.

Take Order (take_order)

Allows customers to place their orders.
Users can input the name of the item and specify the quantity.
Ensures that only valid items from the menu can be ordered; displays a warning if an invalid item is entered.
Customers can finalize their orders by typing "done."

Generate Bill (generate_bill)

Calculates the total cost of all items in the order.
Displays each item, its quantity, and the respective cost in a detailed bill format.
Shows the total cost at the end.
Prints a thank-you message to the customer.

Main System Loop (run)

Provides a menu of actions:
Display the menu.
Take an order.
Generate the bill.
Exit the system.

Handles user input to perform the corresponding action.

Ensures a smooth flow of operations by allowing users to repeatedly perform actions until they choose to exit.

Validates user input to handle incorrect choices gracefully.

Workflow

Start the System:

The application starts by displaying the main menu.
Choose an Option:
Users can display the menu, place orders, or generate a bill.

Take Orders:

Users input item names and quantities to build their order.
Generate and Review Bill:
A detailed bill is displayed, summarizing the order and total cost.

Exit:
Users can exit the application at any time.

Example Use Case

A customer walks into the cafe.

The system operator displays the menu to the customer.
The customer places an order, specifying the items and quantities.
Once the order is complete, the operator generates a bill.
The system calculates and displays the total cost, providing a summary of the order.
The customer pays, and the system is ready for the next customer.

Dependencies

Python 3.x

Customization

You can modify the default menu by updating the menu dictionary during initialization.
Add more features such as discounts, additional items, or a loyalty program.

License

This project is open-source and available for modification and distribution.


Developed by Danish.

