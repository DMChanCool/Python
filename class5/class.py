try:
    n = int(input("請輸入數字:"))
except:
    print("輸入錯誤")
else:
    if n % 2 == 0:
        print("數字是偶數")
    else:
        print("數字是奇數")
print(n)

# 匯入模組
# import

# import turtle #匯入模組turtle
import turtle as t  # 匯入模組turtle並取名為t

# from turtle import * #匯入turtle的所有指令
# from turtle import done #匯入模組turtle的當中的done指令

t.forward(100)  # 向前移動100個單位
t.backward(200)  # 向後移200個單位
# 發現turtle一開始面向右邊
t.done()  # 讓視窗不要關閉

# 正方形
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.done()


# "for" example
# for 的組成有三個部分

# for迴圈變數in範圍
# 迴圈變數只能活在for迴圈中
# 迴圈變數每回合都會從範圍中取出一個值
for i in range(5):
    print(i)

for i in range(1, 6):
    print(i)

for i in range(1, 6, 2):
    print(i)

t.penup()  # 提筆，這要就不會畫線但可以移動
t.forward(100)  # 向前移動100個單位
t.stamp()  # 蓋一個印章
t.right(90)  # 向右移動90度
t.done()  # 讓視窗不要關閉
