s = open("24_9753.txt").readline().strip()

# b - начало текущей подстроки (включительно)
# e - конец текущей подстроки (НЕ включительно, как принято в Python)
# Т.е. в начале имеем подстроку длиной 0, пустая подстрока
# в принципе не может нарушать ни одно ограничение любой задачи

maxlen = b = e = 0

while e < len(s):
    if e % 100000 == 0:
        print(".", end="")
    e += 1
    while s[b:e].count("Y") > 150:
        b += 1
    maxlen = max(maxlen, e - b)

print()
print(maxlen)
