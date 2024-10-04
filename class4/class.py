# 比較預算子

print(1 == 1)  # 1 is equal to 1
print(1 != 1)  # 1 is not equal to 1
print(1 < 2)  # 1 is less than 2
print(1 <= 2)  # 1 is less than or equal to 2
print(1 > 2)  # 1 is greater than 2
print(1 >= 2)  # 1 is greater than or equal to 2


# 邏輯預算子
print(True and True)  # True and True is True
print(True and False)  # True and False is False
print(False and True)  # False and True is False
print(False and False)  # False and False is False
print(True or True)  # True or True is True
print(True or False)  # True or False is True
print(False or True)  # False or True is True
print(False or False)  # False or False is False
print(not True)  # not True is False
print(not False)  # not False is True

# if
pwd = input("請輸入密碼:")
if pwd == "123456":  # 如果密碼是123456
    print("密碼正確")  # 印出密碼正確

# if else
pwd = input("請輸入密碼:")
if pwd == "123456":  # 如果密碼是123456
    print("密碼正確")  # 印出密碼正確
else:  # 如果密碼不是123456
    print("密碼錯誤")  # 印出密碼錯誤

# if elif else
pwd = input("請輸入密碼:")
if pwd == "123":
    print("歡迎a")
elif pwd == "456":  # 如果密碼是456
    print("歡迎b")  # 印出歡迎b
else:
    print("密碼錯誤")

# if elif else is a continous judjment. If one condition is met, the subsequent judjment will not be executed.

# if is required, elif can have multiple but optional, else can only have one but optional.


score = int(input("請輸入分數:"))


if score >= 90 and score <= 100:
    print("A")
elif score >= 80 and score <= 89:
    print("B")
elif score >= 70 and score <= 79:
    print("C")
elif score >= 60 and score <= 69:
    print("D")
elif score >= 59 and score <= 59:
    print("E")
else:
    print("please input again")
