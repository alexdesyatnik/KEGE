s = open("24_21717.txt").readline()

# Определите в этом файле минимальное количество идущих подряд символов,
# среди которых подстрока RSQ встречается ровно 130 раз, при этом искомая
# последовательность не оканчивается символом Q

minlen = 10000
l = count = 0
for r in range(2, len(s)):
    if s[r - 2:r + 1] == "RSQ":
        count += 1
    while count == 130 and s[r] != "Q":
        minlen = min(minlen, r - l + 1)
        if s[l:l + 3] == "RSQ":
            count -= 1
        l += 1
print(minlen)