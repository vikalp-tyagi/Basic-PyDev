# Input validation function
def get_input(prompt, is_int=False):
    while True:
        try:
            value = int(input(prompt)) if is_int else float(input(prompt))
            if value > 0:
                return value
            print("Enter a positive value.")
        except ValueError:
            print(f"Invalid input. Enter a {'integer' if is_int else 'number'}.")

# Customer category
categories = {
    'New': 5,
    'Regular': 10,
    'Premium': 15,
    'VIP': 20,
}

print("Available categories:", ", ".join(categories))
while (category := input("Enter customer category: ").capitalize()) not in categories:
    print("Invalid category. Try again.")

# Products cart and cost calculation
cart = []
total_cost = 0

while True:
    product_name = input("Enter product name: ")
    product_price = get_input("Enter product price: ")
    product_qty = get_input("Enter product quantity: ", is_int=True)

    product_total = product_price * product_qty
    total_cost += product_total

    cart.append({
        'Product_Name': product_name,
        'Product_Price': product_price,
        'Product_Quantity': product_qty,
        'Product_Total': product_total,
    })

    if input("Add more products? (Y/N): ").strip().upper() != 'Y':
        break

# Discount and final cost calculation
discount_rate = categories[category]
discount_amount = (discount_rate / 100) * total_cost
final_cost = total_cost - discount_amount

# Purchase summary
print("\nPURCHASE SUMMARY")
print("-" * 40)
print(f"Customer Category: {category}")
print("\nProducts Purchased:")
for product in cart:
    print(f" - {product['Product_Quantity']} x {product['Product_Name']} @ ${product['Product_Price']:.2f} each = ${product['Product_Total']:.2f}")
print("-" * 40)
print(f"Total Before Discount: ${total_cost:.2f}")
print(f"Discount Applied: ${discount_amount:.2f}")
print(f"Total After Discount: ${final_cost:.2f}")
print("-" * 40)
