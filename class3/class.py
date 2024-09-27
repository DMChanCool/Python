# 型態轉換
# int() 轉換成整數
# bool() 轉換成布林值
# str() 轉換成字串
# float() 轉換成浮點數

print(int("123"))  # 123
print(int(123.9999))  # 123
print(int(True))  # 1
print(int(False))  # 0
print("----------------------")

print(float("123.456"))  # 123.456
print(float(123))  # 123.0
print(float(True))  # 1.0
print(float(False))  # 0.0
print("----------------------")

print(str(123))  # 123
print(str(123.456))  # 123.456
print(str(True))  # True
print(str(False))  # False
print("----------------------")

print(bool(123))  # True
print(bool(0))  # False
print(bool("123"))  # True
print(bool("0"))  # True
print("----------------------")


# input() 讓使用者在終端機輸入資料
# input() 的括弧內可放入"提示字串"
a = input("請輸入數字: ")
# 透過input()輸入的資料都是字串
print(a + "1")  # 字串相加
print(int(a) + 1)  # 將字串轉換成整數後再相


# 格式化字串 f-string
bmi = 17.3
print(f"你的BMI為{bmi}")


# try except 錯誤處理

try:  # try to do something
    n = int(input("請輸入數字: "))

except:  # if error occurs, do this
    print("you should input a number")

else:  # if no errors occurs, do this
    print(n + 1)
