s = open("./24_8615.txt").readline().strip()

"""
Определите максимальное количество идущих подряд символов, среди которых любые
три символа из набора A, B, C, D, E, F в различных комбинациях (с учётом
повторений) не стоят рядом.
"""

for letter in "BCDEF":
    s = s.replace(letter, "A")

begin = end = 0
maxlen = 0

while end < len(s) - 1:
    end += 1
    if s[end - 2 : end + 1] == "AAA":
        begin = end - 1
    maxlen = max(maxlen, end - begin + 1)

print(maxlen)
