# Accept quantity and price then display net-amount

quantity = int(input("Enter quantity: "))
price = int(input("Enter price: "))

amount = quantity * price

if price > 10000:
    discount = amount *  0.20
elif quantity > 2:
    discount = amount *  0.15
else:
    discount = amount *  0.10

net_amount = amount - discount

print(f"Amount     :  {amount:6}")
print(f"Discount   :  {discount:6.0f}")
print(f"Net Amount :  {net_amount:6.0f}")

