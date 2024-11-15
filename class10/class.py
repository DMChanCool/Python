import random

# random.randrange 設定範圍的方式跟range一樣，特性也不包含最後一個數字
# random.randrange 的功能是隨機取得一個數字，range是產生一組數字
print(random.randrange(10))
print(random.randrange(1, 10))
print(random.randrange(0, 10, 2))


# random.randint 設定範圍的方式必須要有開始跟結束，且包含最後一個數字
# 不能跳數字抽籤
print(random.randint(1, 10))  # 隨機取得1到10的數字


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


# list 清單
# list 可以存入很多資料，每筆資料用逗號隔開，可存入任何資料型態
# 外層用[]包起來
L = [1, 2, 3, 4, 5]
print(L)

L = [1, 2, 3, 4, 5, "hello", ["world", 6]]
print(L)

# list 取值 方式跟字串一樣，也可以用[:]取值
# list 當中資料的編號(index)都從0開始
L = [1, 2, 3, 4, 5]
print(L[0])  # 取第1值
print(L[1])  # 取第2值
print(L[2])  # 取第3值

# list 取值 方式跟字串一樣，也可以用[:]取值
# 設定範圍的方式跟range一樣，特性也不包含最後一個數字
print(L[0:3])  # 取第1到第3值
print(L[:3])  # 取第1到第3值
print(L[3:])  # 取第4到最後值
print(L[:])  # 取所有值
