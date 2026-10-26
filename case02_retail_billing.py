n = int(input("Enter number of products: "))
total = 0

for i in range(n):
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    amount = price * quantity
    total = total + amount

    print(name, "Amount: Rs.", round(amount, 2))

if total >= 1000:
    discount = total * 0.10
else:
    discount = 0

final_bill = total - discount

print("Total amount: Rs.", round(total, 2))
print("Discount: Rs.", round(discount, 2))
print("Final bill: Rs.", round(final_bill, 2))
