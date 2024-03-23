import turtle as t
import math

screen = t.Screen()

xc = int(input())
yc = int(input())
r = int(input())
x = int(input())
y = int(input())

# Draw a circle.
t.penup()
t.goto(xc, yc)
t.pendown()
t.circle(r)

# draw a point.
t.penup()
t.goto(x, y)
t.color('red')
t.pendown()
t.dot()

# We find the length of the vector and
# compare it with the radius.
d = math.sqrt((x - xc)**2 + (y - yc)**2)
if d < r:
    print('Точка внутри окружности')
elif d == r:
    print('Точка на окружности')
else:
    print('Точка вне окружности')

screen.mainloop()
