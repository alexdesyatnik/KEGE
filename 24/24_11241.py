s = open("24_11241.txt").readline()
for ch in "ABCD":
    s = s.replace(ch, " ")
s = s.split()
print(len(max(s, key=len)))