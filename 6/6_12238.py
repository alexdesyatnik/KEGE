"""
Повтори 2 [Вперёд 5 Налево 90 Назад 13 Налево 90]
Поднять хвост
Назад 10 Направо 90 Вперёд 9 Налево 90
Опустить хвост
Повтори 2 [Вперёд 11 Направо 90 Вперёд 7 Направо 90]
"""
from turtle import *
speed(0)
color("red", "red")
m = 10
left(90)
begin_fill()
for i in range(2):
    forward(5 * m)
    left(90)
    backward(13 * m)
    left(90)
end_fill()
up()
backward(10 * m)
right(90)
forward(9 * m)
left(90)
down()
begin_fill()
for i in range(2):
    forward(11 * m)
    right(90)
    forward(7 * m)
    right(90)
end_fill()

count = 0
canvas = getcanvas()
for x in range(-200 * m, 200 * m, m):
    for y in range(-200 * m, 200 * m, m):
        item = canvas.find_overlapping(x, y, x, y)
        if len(item) > 0:
            count += 1
print(count)

done()