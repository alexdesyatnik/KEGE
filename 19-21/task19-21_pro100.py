"""
Задача 14954 КомпЕГЭ

Два игрока, Петя и Ваня, играют в следующую игру. Перед ними лежат три кучки камней,
в первой из которых 2, во второй – 3, в третьей – S (1 ≤ S ≤ 19) камней.
У каждого игрока неограниченно много камней. Игроки ходят по очереди, первый ход
делает Петя. Ход состоит в том, что игрок или удваивает число камней в какой-то
куче или добавляет по два камня в каждую из куч.

Выигрывает игрок, после хода которого в одной из куч становится не менее 20 камней,
или после хода которого общее число камней во всех трех кучах становится не менее 25.

Будем говорить, что игрок имеет выигрышную стратегию, если он может выиграть при любых ходах противника.

Укажите такое значение S, при котором Петя не может выиграть за один ход,
но при любом ходе Пети Ваня может выиграть своим первым ходом.

Задание 20.
Для игры, описанной в предыдущем задании, найдите два наименьших значения S,
при которых у Пети есть выигрышная стратегия, причём одновременно выполняются два условия:
    − Петя не может выиграть за один ход;
    − Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.
Найденные значения запишите в ответе в порядке возрастания.


Задание 21.
Для игры, описанной в задании 19, найдите минимальное значение S, при котором
одновременно выполняются два условия:
    – у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или
    вторым ходом при любой игре Пети;
    – у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом.
"""

def fn(s1, s2, s3, k, pb):
    if s1 >= 20 or s2 >= 20 or s3 >= 20 or s1 + s2 + s3 >= 25:
        return k in pb
    if k > max(pb):
        return False
    next = [fn(s1 * 2, s2, s3, k + 1, pb),
            fn(s1, s2 * 2, s3, k + 1, pb),
            fn(s1, s2, s3 * 2, k + 1, pb),
            fn(s1 + 2, s2 + 2, s3 + 2, k + 1, pb), ]
    if k % 2 != max(pb) % 2:
        return any(next)
    else:
        return all(next)


# Задача 19: П не может выиграть первым ходом, В выигрывает своим первым
for s in range(1, 19 + 1):
    if (fn(2, 3, s, 0, [1]) == False and
            fn(2, 3, s, 0, [2]) == True):
        print("19:", s)

# Задача 20: П выигрывает вторым ходом, но не первым
for s in range(1, 19 + 1):
    if (fn(2, 3, s, 0, [1]) == False and
            fn(2, 3, s, 0, [3]) == True):
        print("20:", s)

# Задача 21: В выигрывает своим вторым ходом, но не первым
for s in range(1, 19 + 1):
    if (fn(2, 3, s, 0, [2, 4]) == True and
            fn(2, 3, s, 0, [2]) == False):
        print("21:", s)