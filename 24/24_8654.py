# Определите максимальное количество идущих подряд символов, среди которых нет
# ни одной подстроки, соответствующей маске ?B??D

from fnmatch import fnmatch

s = open("24_8654.txt").readline()

begin = end = 0
maxlen = 1

while end < len(s):
    if end % 10000 == 0:
        print(".", end="")
    end += 1
    if fnmatch(s[end - 4 : end + 1], "?B??D"):
        begin = end - 3
    maxlen = max(maxlen, end - begin + 1)

print()
print(maxlen)
