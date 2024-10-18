# import turtle as t

# t.color("green")
# t.shape("turtle")
# t.shapesize(1)
# t.speed(1000)

# for i in range(999):
#     t.stamp()
#     t.penup()
#     t.right(50)
#     t.forward(10 + i)

# t.done


l = int(input("please enter number:"))

sum = 0
for i in range(int(l + 1)):
    sum = sum + i

print(f"1to{l}sum is {sum}")
