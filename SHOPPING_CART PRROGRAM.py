food = ()
price = []
total = 0
while True:
    item = input("Enter the item to add to cart (or type 'done' to finish): ")
    if item.lower() == 'done':
        break
    food += (item,)
    item_price = float(input(f"Enter the price of {item}: "))
    price.append(item_price)


print("\nItems in your cart:")
for i in range(len(food)):
    print(f"{food[i]}: ${price[i]:.2f}")
    total += price[i]
print(f"\nTotal price: ${total:.2f}")
print("Thank you for shopping with us!")