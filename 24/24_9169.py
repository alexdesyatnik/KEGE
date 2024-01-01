"""
Определите минимальную длину подстроки, в которой ровно три тройки BAD или FAT.
"""

s = open("./24_9169.txt").readline().strip()
s = s.replace("FAT", "BAD")

a = s.find("BAD")
b = s.find("BAD", a + 1)
c = s.find("BAD", b + 1)
minlen = c + 2 - a + 1

while True:
    a = b
    b = c
    c = s.find("BAD", b + 1)
    if c == -1:
        break
    minlen = min(minlen, c + 2 - a + 1)

print(minlen)
