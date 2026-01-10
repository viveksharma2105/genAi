order_amount = int(input("Enter the order amount: "))

delivery_fees = 0 if order_amount > 300 else 30
print(f"Delivery fees: ${delivery_fees}")

#Train seat info system
seat_type = input("Enter seat type (sleeper/AC/general/luxury): ").lower()

match seat_type:
    case 'sleeper':
        print("Sleeper seat selected. Price: $50")
    case 'ac':
        print("AC seat selected. Price: $100")
    case 'general':
        print("General seat selected. Price: $30")
    case 'luxury':
        print("Luxury seat selected. Price: $200")
    case _:
        print("Invalid seat type entered.")