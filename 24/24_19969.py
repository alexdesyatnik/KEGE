import re
s = open("24_19969.txt").readline().strip()
pattern = r"[a-z]+\@[a-z]+\.[a-z]+"
s2 = max(re.findall(pattern, s), key=len)
print(len(s2))
