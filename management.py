menu = {
    'pizza':40,
    'pasta':50,
    'burger':60,
    'cofee':70,
    'tea':20,
    'salad':80
    }
print("welcome to python restaurent")
print("pizza : 40\npasta : 50\nburger : 60\ncofee : 70\ntea : 20\nsalad : 80")

order_total = 0
item_1 = input("enter the name of the item you want to order = ")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"your {item_1} has been added to your order")
else:
    print("ordered item is not available yet")
another_item = input("do you want to order anther item ? (yes/no) ")
if another_item == "yes":
    item_2 = input("enter the second item = ")
    if item_1 in menu:
        order_total+=menu[item_2]
        print(f"your {item_1} has been added to your order")
    else:
      print("ordered item is not available yet")
print(f"the total amount of ordered item is {order_total}")
    

