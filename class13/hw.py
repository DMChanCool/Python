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

food_list = {"cake": 1, "sandwich": 10, "juice": 20, "french fries": 15, "pizza": 2}
print("Xiao-Hua's Birthday Party Food List:")
print("-----------------------------------")

for food, quantity in food_list.items():
    if food == "cake" or food == "pizza":
        unit = "piece" if quantity == 1 else "pieces"
    elif food == "juice":
        unit = "cup" if quantity == 1 else "cups"
    else:
        unit = "portion" if quantity == 1 else "portions"

    print(f"{food}: {quantity} {unit}")
