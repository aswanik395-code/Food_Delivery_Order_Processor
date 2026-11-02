
# Food Delivery Order Processor

# Menu
menu = {
    "Burger": 120,
    "Pizza": 250,
    "Sandwich": 100,
    "Pasta": 180,
    "Fries": 80,
    "Juice": 60
}

# Sample Orders
orders = [
    {"id": 1, "items": {"Burger": 2, "Fries": 1}},
    {"id": 2, "items": {"Pizza": 1, "Juice": 2}},
    {"id": 3, "items": {"Sandwich": 2, "Juice": 1}},
    {"id": 4, "items": {"Pasta": 2}},
    {"id": 5, "items": {"Burger": 1, "Pizza": 1}},
    {"id": 6, "items": {"Fries": 3, "Juice": 2}},
    {"id": 7, "items": {"Pizza": 2}},
    {"id": 8, "items": {"Sandwich": 1, "Pasta": 1}},
    {"id": 9, "items": {"Burger": 3}},
    {"id": 10, "items": {}},
    {"id": 11, "items": {"InvalidItem": 2}}
]

DELIVERY_CHARGE = 30
DISCOUNT_LIMIT = 500
DISCOUNT_RATE = 0.10


# Calculate item total
def calculate_total(items):
    total = 0

    for item, quantity in items.items():
        if item not in menu:
            print("Invalid item:", item)
            return None

        if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
            print("Invalid quantity for:", item)
            return None

        total += menu[item] * quantity

    return total


# Apply discount
def apply_discount(total):
    if total >= DISCOUNT_LIMIT:
        return total * DISCOUNT_RATE
    return 0


# Calculate final bill
def calculate_bill(items):
    if not items:
        print("Empty order!")
        return None

    total = calculate_total(items)

    if total is None:
        return None

    discount = apply_discount(total)
    delivery = DELIVERY_CHARGE
    final_amount = total - discount + delivery

    return total, discount, delivery, final_amount


# Process all orders
def process_orders():
    total_revenue = 0
    valid_orders = []
    highest_order = None

    print("\n===== FOOD DELIVERY ORDERS =====")

    for order in orders:
        print("\nOrder ID:", order["id"])

        bill = calculate_bill(order["items"])

        if bill is None:
            print("Order could not be processed.")
            continue

        total, discount, delivery, final_amount = bill

        print("Item Total: Rs.", total)
        print("Discount: Rs.", round(discount, 2))
        print("Delivery Charge: Rs.", delivery)
        print("Final Bill: Rs.", round(final_amount, 2))

        total_revenue += final_amount

        valid_orders.append({
            "id": order["id"],
            "amount": final_amount
        })

        if highest_order is None or final_amount > highest_order["amount"]:
            highest_order = {
                "id": order["id"],
                "amount": final_amount
            }

    return total_revenue, valid_orders, highest_order


# Generate sales report
def generate_report(revenue, valid_orders, highest_order):
    with open("sales_report.txt", "w") as file:
        file.write("===== DAILY SALES REPORT =====\n")
        file.write("Total Orders: " + str(len(orders)) + "\n")
        file.write("Successful Orders: " + str(len(valid_orders)) + "\n")
        file.write("Failed Orders: " + str(len(orders) - len(valid_orders)) + "\n")
        file.write("Total Revenue: Rs. " + str(round(revenue, 2)) + "\n")

        if highest_order:
            file.write("Highest Order ID: " + str(highest_order["id"]) + "\n")
            file.write("Highest Order Value: Rs. " +
                       str(round(highest_order["amount"], 2)) + "\n")
        else:
            file.write("No valid orders.\n")

    print("\nSales report saved to sales_report.txt")


# Main function
def main():
    revenue, valid_orders, highest_order = process_orders()

    print("\n===== SALES SUMMARY =====")
    print("Total Orders:", len(orders))
    print("Successful Orders:", len(valid_orders))
    print("Total Revenue: Rs.", round(revenue, 2))

    if highest_order:
        print("Highest Order ID:", highest_order["id"])
        print("Highest Order Value: Rs.",
              round(highest_order["amount"], 2))

    generate_report(revenue, valid_orders, highest_order)


main()
