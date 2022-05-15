items_to_prices = {}
with open("mydata.txt", encoding="utf-8") as prices:
    while True:
        item = prices.readline()
        if item.strip() == '':
            break
        product, cost = item.split(":")
        items_to_prices[product] = float(cost)
'''items_to_prices = {"iced coffee: 2.00, soda:3.45, water:1.00, bagel:2.45}'''

def total_price(items, quantity):
    expense = 0
    items_list = items.split(", ")
    '''items_list = [lemonade]'''
    quantity_list = quantity.split(", ")
    '''quantity_list = [2]'''
    try:
        for products in items_list:
            expense += 1.05*(items_to_prices[products])*int(quantity_list[items_list.index(products)])
        print("The total cost of your purchase is: {:.2f}".format(expense))
    except KeyError:
        print("please enter an item on the menu")

def add_item(item_name, item_cost):
    with open("mydata.txt", "a", encoding="utf-8") as update:
        if item_name in items_to_prices:
            print("This item is already in the menu")
        elif item_name not in items_to_prices:
            update.write("{}:{} \n".format(item_name,item_cost))

def main(decision = input("What do you want to do? (enter 1 to add an item, enter 2 to take an order): ")):
    if decision == "1":
        new_item = input("What item do you want to add?: ")
        new_price = input("What is the price: ")
        add_item(new_item, new_price)
    elif decision == "2":
            while True:
                items_on_the_menu = list(items_to_prices.keys())
                desired_items = input(f"What items would you like to buy {items_on_the_menu}: ")
                desired_quantity = input("How much of that item do you want?: ")
                add_more = input("would you like to add more (y/n): ")
                if add_more == "n":
                    break

            total_price(desired_items, desired_quantity)


main()

