"""
Определите в прилагаемом файле минимальное количество идущих подряд символов, среди которых подстрока 2025
встречается не менее 110 раз и при этом содержится ровно 90 букв W.
"""
s = open("24_26078.txt").readline().strip()

count_2025 = 0
count_w = 0
l = 0
minlen = 10 ** 10

for r in range(len(s)):
    if s[r] == "W":
        count_w += 1
    if r > 2 and s[r-3:r+1] == "2025":
        count_2025 += 1
    while count_w > 90:
        if s[l] == "W":
            count_w -= 1
        if s[l:l+4] == "2025":
            count_2025 -= 1
        l += 1
    while count_w == 90 and count_2025 >= 110:
        minlen = min(minlen, r - l + 1)
        if s[l] == "W":
            count_w -= 1
        if s[l:l+4] == "2025":
            count_2025 -= 1
        l += 1
print(minlen)

