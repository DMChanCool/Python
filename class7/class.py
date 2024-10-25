# 九九乘法表
for a in range(1, 10):  # 讓 a 從 1 執行到 9
    for b in range(1, 10):  # 讓 b 從 1 執行到 9
        print(f"{a}x{b}={a*b}")


# while 迴圈
# 這是條件是迴圈，當條件做為 True 時，執行迴圈內程式
i = 0
while i < 10:
    # 當 i 小於 10 時，執行迴圈內程式
    print(i)
    i = i + 1


# 算術指定運算子
# +=,-=,*=,/=,%=. **=, //=
# x=x+1 等於x+=1
# x=x-1 等於x-=1
# x=x*1 等於x*=1
# x=x/1 等於x/=1
# x=x%1 等於x%=1
# x=x**1 等於x**=1
# x=x//1 等於x//=1

i = 1
print(i)
i += 1


"""
升級版密碼門
•輸入正確的時候會顯示歡迎文字
•輸入錯誤則會要求重新輸入
•如果一直輸入錯誤可以無限循環輸入直到正確為止
"""
pwd = "123456"
user_input = input("")
while user_input != pwd:
    user_input = input("請輸入正確的密碼:")

print("歡迎使用升級版密碼門")
