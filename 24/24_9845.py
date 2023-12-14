from itertools import product

s = open("24_9845.txt").readline()
s = s.replace("B", "A")
s = s.replace("C", "A")
s = s.replace("9", "8")
while "AA" in s:
    s = s.replace("AA", "A A")
while "88" in s:
    s = s.replace("88", "8 8")

print(max(len(c) for c in s.split()))
