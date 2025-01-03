a = ["a", "b", "c"]
b = a  # assign the memory location of a to b, so a and b point to the same memory location
b[0] = "d"  # modify the first element of b, and will also change
print(a)  # print a, it will be ["d","b","c"]

a = 10
b = a
b = 20  # 修改b的值，但是不會影響a
print(a)  # shows 10
