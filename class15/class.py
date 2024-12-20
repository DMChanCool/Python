# 函式(function):like a magical toolbox where we can store commands that we use often
# when we need ti use there commands, we just need to call the function name!!


# Create a basic function - function name must be followed by parentheses() and  a colon(:)
def say_hello():
    print("Hello! I am DMChan!")
    print("Nice to meet you!")


say_hello()  # call the function-like using your own command


# Functions can recieve information (parameters)
# Parameters are like ingredients for your function
# You can put different values to get different results
def say_hello_with_name(name):
    print(f"Hello, {name}!")
    print("Nice to meet you!")


def say_hello_with_default(name="DMChan"):
    print(f"Hello, {name}!")
    print("Nice to meet you!")


say_hello_with_default()  # use default value
say_hello_with_name("DMChan")  # use new value


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
