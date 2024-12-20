"""
Xiao-Hua's birthday is coming soon! He wants to have a special birthday party with his friends.
He has already decided what food to prepare and put the information in a dictionary, like this:
food_list = {"cake": 1, "sandwich": 10, "juice": 20, "french fries": 15, "pizza": 2}
The terminals will show the following information:
cake: 1 piece
sandwich: 10 pieces
juice: 20 cups
french fries: 15 portions
pizza: 2 pieces
"""

a=input((int"cake:"))
b=input((int"sandwich:"))
c=input((int"juice:"))
d=input((int "french fries:"))
e=input((int "pizza:"))
food_list = {"cake": a, "sandwich": b, "juice": c, "french fries": d, "pizza": e}

for food, quantity in food_list.items():
    if food == "juice":
        unit = "cups"
    elif food == "french fries":
        unit = "portions"
    elif quantity == 1:
        unit = "piece"
    else:
        unit = "pieces"
    
    print(f"{food}: {quantity} {unit}")
