s = open("./24_7853.txt").readline().strip()

maxlen = b = e = 0

while e < len(s):
    e += 1
    if s[e - 1] in "NOT" and s[e - 3] in "NOT":
        b = e - 2
    maxlen = max(maxlen, e - b)

print(maxlen)
