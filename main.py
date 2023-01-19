from store import Store

seller = Store(
    int(input("Enter your banc balance: "))
)

while True:
    print("For adding products enter A: ")
    print("For selling enter S: ")
    print("For filtering enter F: ")
    print("For balance enter B: ")
    print("For all products enter P: ")
    print("For future profit enter FP: ")
    print("For exit neter EX: \n\n")
    choose = input("Enter option: ")

    if choose == "A":
        name = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        purchase = int(input("Enter purchase price: "))
        sell = int(input("Enter selling price: "))

        seller.add_product(name, quantity, purchase, sell)
    if choose == "S":
        name = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))

        seller.sell_product(name, quantity)
        print(f'\n\nYour balance now {seller.balance}\n\n')

    if choose == "P":
        for prod in seller.products:
            print(f'{prod.name} of count {prod.quantity}')
        print("\n\n")

    if choose == "FP":
        print(f'\n\nYour future profit is {seller.profit()}\n\n')

    if choose == "B":
        print(f'\n\nYour balance now {seller.balance}\n\n')

    if choose == "F":
        seller.filter_by_mode()

    if choose == "EX":
        break
