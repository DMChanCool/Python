import turtle as t
import time

t.speed(0)

for i in range(60):
    for u in range(1, 13):
        t.penup()
        t.forward(300)
        t.stamp()
        t.backward(300)
        t.right(30)
    print(6 * i)
    t.right(6 * i)
    t.pendown()
    t.forward(250)
    t.backward(250)
    time.sleep(1)  # sleep 1 seconds
    t.clear()
    t.left(6 * i)

t.done()
