s = open("24_19254.txt").readline().strip()

l = 0
k = 0
maxlen = 0
for r in range(4, len(s) + 1):
    if s[r-4:r] == "FSRQ":
        k += 1
    if k == 80:
        maxlen = max(r - l, maxlen)
    elif k > 80:
        l = s.find("FSRQ", l) + 1
        k -= 1
print(maxlen)