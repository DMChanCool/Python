import random

x = random.randint(1, 100)

while True:
    y = int(input("請輸入一個數字:"))

    if x > y:
        print("再大一點")
    elif x == y:
        print("答對")
        break
    else:
        print("再小一點")
