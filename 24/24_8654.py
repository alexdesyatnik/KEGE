# Определите максимальное количество идущих подряд символов, среди которых нет
# ни одной подстроки, соответствующей маске ?B??D
s = open("24_8654.txt").readline()

begin = end = 0
maxlen = 0

while end < len(s):
    if end % 10000 == 0:
        print(".", end="")
    end += 1
    if s[end - 1] == "D" and s[end - 4] == "B":
        begin = end - 4
    maxlen = max(maxlen, end - begin)

print()
print(maxlen)
