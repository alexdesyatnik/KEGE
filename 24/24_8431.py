s = open("./24_8431.txt").readline().strip()

maxlen = b = e = 0
xyz = set("XYZ")
while e < len(s):
    e += 1
    if (
        (e - 3 > 0 and set(s[e - 3 : e]) == xyz)
        or (e - 2 > 0 and e < len(s) and set(s[e - 2 : e + 1]) == xyz)
        or (e - 1 > 0 and e < len(s) - 1 and set(s[e - 1 : e + 2]) == xyz)
    ):
        b = e
    maxlen = max(maxlen, e - b)
print(maxlen)
