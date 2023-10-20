orders = {}

def add_order():
    global Total
    Total = 0
    Table_size = input("Enter table size: ")
    print("""
          Menu:
          1: Pie - $8.00
          2: Fish - $9.00
          3: Pasta - $10.00
          4: Steak - $14.00
          5: Nothing - $0.00
          """)
    if Table_size == "3":
        i = 0
        while i < 3:
            name = input("Enter customer name: ")
            order = input("Enter menu order: ")
            if order == "1":
                Total = Total + 8.00
                price = 8.00
            elif order == "2":
                Total = Total + 9.00
                price = 9.00
            elif order == "3":
                Total = Total + 10.00
                price = 10.00
            elif order == "4":
                Total = Total + 14.00
                price = 14.00
            elif order == "5":
                Total = Total + 0.00
                price = 0.00
            i = i + 1
            orders[name] = {"order": order, "price": price}
    elif Table_size == "5":
        while i < 5:
            name = input("Enter customer name: ")
            order = input("Enter menu order: ")
            if order == "1":
                Total = Total + 8.00
                price = 8.00
            elif order == "2":
                Total = Total + 9.00
                price = 9.00
            elif order == "3":
                Total = Total + 10.00
                price = 10.00
            elif order == "4":
                Total = Total + 14.00
                price = 14.00
            elif order == "5":
                Total = Total + 0.00
                price = 0.00
            i = i + 1
            orders[name] = {"order": order, "price": price}
    else:
        print("Invalid choice. Please try again.")

def display_orders():
    print("Name\tOrder\tPrice")
    for name, order in orders.items():
        print(f"{name}\t{order['order']}\t{order['price']}")
    global Leave
    Leave = input("Would you like to leave (y/n): ")
    

while True:
    print("1. Add order")
    print("2. Display orders")
    print("3. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_order()
    elif choice == "2":
        display_orders()
        if Leave == "y":
            break
        elif Leave == "n":
            continue
        else:
            print("Invalid choice. Please try again.")
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")


Payment_Type = input("How would you like to pay? (Cash or Credit): ")

if Payment_Type == "Cash":
    pass
elif Payment_Type == "Credit":
    Surcharge = Total * 0.10
    
   
while True:    
    Tip = input("Would you like to leave a tip? (y/n): ")

    if Tip == "y":
        Tip_Amount = float(input("How much would you like to leave? (Enter as decimal): "))
        Final_Total = Total + Tip_Amount
        break
    elif Tip == "n":
        Tip_Amount = 0
        pass
        break
    else:
        print("Invalid choice. Please try again.")

Final_Total = Final_Total + Surcharge
                

if Payment_Type == "Credit":
    print(f"Your total is ${round(Total, 2)}.")
    print(f'Payment Method: {Payment_Type}')
    print(f'Card Surcharge: ${round(Surcharge, 2)}')
    print(f'Tip: ${round(Tip_Amount, 2)}')
    print(f'Final total: ${round(Final_Total, 2)}')
elif Payment_Type == "Cash":
    print(f"Your total is ${round(Total, 2)}.")
    print(f'Payment Method: {Payment_Type}')
    print(f'Tip: ${round(Tip_Amount, 2)}')
    print(f'Final total: ${round(Final_Total, 2)}')
else:
    print("Unknown error occured. Please try again.")

print("Thank you for dining with us today. Have a nice day!")
