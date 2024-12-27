# 區域變數與全域變數
# local and global variables
# local variables are variables that are only available in the function
# global variables are variables that are available in the function and in other functions
toy_name = "玩具熊"  # global variable


def play_with_toy():
    toy_name = (
        "慧魚積木"  # 區域變數 local variable-like your own toy that you can play with
    )
    print(f"下課時我在玩：{toy_name}")  # 顯示"下課時我在玩：慧魚積木"


def share_toy():  # tell python we want to use shared toys
    global toy_name
    toy_name = "積木"  # modify the toy that everyone shares
    print(f"大家在玩：{toy_name}")  # 顯示"大家在玩：積木"


# let's see how the toys change
print(f"一開始教室的玩具是：{toy_name}")  # 顯示"一開始教室的玩具是：玩具熊"
play_with_toy()  # 下課時我在玩：慧魚積木
print(
    f"下課後教室的玩具還是：{toy_name}"
)  # 顯示"下課後教室的玩具還是：玩具熊"（no change）


print("\n現在讓我們改變大家的玩具！")  # \n--> 換行
print(f"教室的玩具是：{toy_name}")  # 顯示"教室的玩具是：玩具熊"
share_toy()  # 大家在玩：積木
print(f"教室的玩具變成：{toy_name}")  # 顯示"教室的玩具是：積木"


# 函式可以回傳資料 -就像是我們請人們幫忙的東西，他會把他們的幫忙傳回給我們
# return是回傳的關鍵字
def calculate_sum(number1, number2=0):
    total = number1 + number2
    return total


result = calculate_sum(5, 3)
print(f"sum of 5 and 3 is {result}")  # 顯示"sum of 5 and 3 is 8"
result = calculate_sum(10)  # 預設的參數是0
print(f"sum of 10 and 0 is {result}")  # 顯示"sum of 10 and 0 is 10"


# 函式參數預設值的順序-有預設值的參數一定要放在沒有預設值得後面
# like ordering food, you must first choose main dish


# this is correct
def order_lunch(main_dish, side_dish="薯條"):
    print(f"你選擇了{main_dish})")
    print(f"你也選擇了{side_dish}")


order_lunch("燒烤牛肉")
order_lunch("燒烤牛肉", "薯條")

# this is wrong
# def order_lunch(side_dish="薯條", main_dish):
#     print(f"你選擇了{main_dish})")
#     print(f"你也選擇了{side_dish}")
