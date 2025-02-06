import re
s = open("24-7573.txt").readline().strip()

num = r"(?:0|[1-9][0-9]*)"
pattern = rf"{num}(?:[+*]{num})*"
maxlen = 0
for s2 in re.findall(pattern, s):
    if eval(s2) == 0:
        maxlen = max(maxlen, len(s2))
print(maxlen)