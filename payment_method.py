items_to_prices = {}
with open("mydata.txt", encoding="utf-8") as prices:
    while True:
        item = prices.readline()
        if item.strip() == '':
            break
        product, cost = item.split(":")
        items_to_prices[product] = float(cost)
'''items_to_prices = {"iced coffee: 2.00, soda:3.45, water:1.00, bagel:2.45}'''
items_on_the_menu = list(items_to_prices.keys())


def add_item(item_name, item_cost):
    with open("mydata.txt", "a", encoding="utf-8") as update:
        if item_name in items_to_prices:
            print("This item is already in the menu")
        elif item_name not in items_to_prices:
            update.write("{}:{} \n".format(item_name, item_cost))


def main(decision=input("What do you want to do? (enter 1 to add an item, enter 2 to take an order): "), total_cost=0):
    if decision == "1":
        new_item = input("What item do you want to add?: ")
        new_price = input("What is the price: ")
        add_item(new_item, new_price)
    elif decision == "2":
        while True:
            desired_items = input(f"Name the item you want to purchase {items_on_the_menu}: ")
            if desired_items not in items_on_the_menu:
                print("This is not in the menu, please enter something else")
                continue
            desired_quantity = input("How much of that item do you want?: ")
            total_cost += int(desired_quantity) * float(items_to_prices[desired_items])
            add_more = input("would you like to add more (y/n): ")
            if add_more != "y":
                break
            elif add_more == "y":
                continue
    print("Your total cost: is {:.2f}".format(1.5*total_cost))

main()
