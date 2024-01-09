s = open("./24_6029.txt").readline().strip()
maxlen = b = e = 0

while e < len(s):
    e += 1
    if e - b > 1:
        if s[e - 2 : e] != "EF" and s[e - 2 : e] != "FE":
            if s[e - 1] != "D":
                b = e - 1
            else:
                b = e
    maxlen = max(maxlen, e - b)

print(maxlen)
