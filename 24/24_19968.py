import re
s = open("24_19968.txt").readline().strip()
NUM = r"(?:0|[1-5][0-5]*)"
pattern = rf"{NUM}(?:[*+]{NUM})*"
s2 = max(re.findall(pattern, s), key=len)
print(len(s2))