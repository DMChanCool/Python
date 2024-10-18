# 時鐘

import turtle as t

t.penup()
t.speed(5)
for i in range(12):
    t.forward(300)
    t.stamp()
    t.backward(300)
    t.right(30)

t.done()
