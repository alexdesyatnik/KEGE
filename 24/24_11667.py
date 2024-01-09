s = open("./24_11667.txt").readline().strip()

"""
Определите в прилагаемом файле максимальное количество идущих подряд символов
(длину непрерывной подпоследовательности), среди которых сочетание символов
INFINITY встречается ровно 1000 раз.
"""

begin = end = 0
maxlen = 0
inf_count = 0

while end < len(s):
    end += 1
    if end % 100000 == 0:
        print(".", end="")
    if s[end - 8 : end] == "INFINITY":
        inf_count += 1
    if inf_count == 1000:
        maxlen = max(maxlen, end - begin)
    elif inf_count > 1000:
        begin = s.find("INFINITY", begin) + 1
        inf_count -= 1

print()
print(maxlen)
