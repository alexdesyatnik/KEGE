from turtle import *
color("black", "red")
speed(0)
m = 50
left(90)
begin_fill()
# Повтори 12 [Вперёд 4 Направо 144 Вперёд 4 Налево 72]
# Уменьшил количество повторений, чтобы фигура правильно заливалась красным
for i in range(5):
    forward(4 * m)
    right(144)
    forward(4 * m)
    left(72)
end_fill()

count = 0
canvas = getcanvas()
for x in range(-100 * m, 100 * m, m):
    for y in range(-100 * m, 100 * m, m):
        item = canvas.find_overlapping(x, y, x, y)
        # item[0] == 5 - проверка на красный цвет (заполнение фигуры, чтобы не посчитать линии)
        if len(item) == 1 and item[0] == 5:
            count += 1
print(count)
done()