"""
Enter a number and check if it is a prime number. Display the result on the screen.
Prime Number Condition: A prime number can only be divided evenly by itself and 1—no other numbers.

Here's an example(in terminal):
---
Enter a number: 7  
Result: 7 is a prime number.

Enter a number: 10  
Result: 10 is not a prime number.
---
Explanation:
- For 7: It can only be divided by 1 and 7 without leaving a remainder, so it's a prime number.
- For 10: It can be divided by 1, 2, 5, and 10, so it's not a prime number.
"""

num = int(input("Enter a number: "))
is_prime = True
for i in range(2, num):
    if num % i == 0:
        is_prime = False
if is_prime and num > 1:
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")

"""
Let's create a checkout register program!
1. Each time you enter (input) the price of an item, the program will add it to the total amount.
2. The program will show the new total every time you add a new item.
3. When you enter 0, the program will stop adding and end the checkout.

for example (in terminal):
---
Please enter the item price: 10
Current total is 10 dollars.

Please enter the item price: 23
Current total is 33 dollars.

Please enter the item price: 55
Current total is 88 dollars.

Please enter the item price: 100
Current total is 188 dollars.

Please enter the item price: 0
"""

total = 0
while True:
    price = int(input("Please enter the item price: "))
    if price == 0:
        break
    total += price
print("Current total is", total, "dollars.")
