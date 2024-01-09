s = open("./24_7853.txt").readline().strip()

maxlen = b = e = 0

for letter in "NOT":
    s = s.replace(letter, "*")

while e < len(s):
    e += 1
    if s[e - 1] == "*" and s[e - 3] == "*":
        b = e - 2
    maxlen = max(maxlen, e - b)

print(maxlen)
