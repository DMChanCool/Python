import turtle as t
import time

t.speed(9999999999999999999999999999999999999999999999999999999999999999999)

for i in range(61):
    t.penup()
    for u in range(12):
        t.forward(300)
        t.stamp()
        t.backward(300)
        t.right(30)
    t.pendown()
    t.right(6)
    t.forward(250)
    t.backward(250)
    time.sleep(1)  # sleep 1 seconds
    t.clear()

t.done()
