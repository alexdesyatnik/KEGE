# Определите максимальное количество идущих подряд символов, среди которых нет
# ни одной подстроки, соответствующей маске ?B??D
s = open("24_8654.txt").readline()

begin = end = 0
maxlen = 1

while end < len(s) - 1:
    if end % 10000 == 0:
        print(".", end="")
    end += 1
    if s[end] == "D" and s[end - 3] == "B":
        begin = end - 3
    maxlen = max(maxlen, end - begin + 1)

print()
print(maxlen)
