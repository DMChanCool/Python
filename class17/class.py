a = ["a", "b", "c"]
b = a  # assign the memory location of a to b, so a and b point to the same memory location
b[0] = "d"  # modify the first element of b, and will also change
print(a)  # print a, it will be ["d","b","c"]

a = 10
b = a
b = 20  # 修改b的值，但是不會影響a
print(a)  # shows 10


# def doc用途
def add(a, b):
    """
    加法函式
    :param a:數字1
    :param b:數字2
    :return:a+b
    """
    return a + b


# using the "help" function you can view the function's documentation
# ex:
# help(add)

# you can also use the __doc__ attribute to view the function's documentation
# ex:
print(add.__doc__)


# eval(input()) -this function allows the user's input text to become 程式碼
# ex:
ans = eval("5+3")
print(ans)  # shows 8

# this way, users can input mathematical expressions and caculate the result
# ex:
ans = eval(input("輸入算式:"))
print(ans)
# 5+3--->8
