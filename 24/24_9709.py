s = open("24_9709.txt").readline().strip()

s = s.replace("XYZ", " ").replace("YZX", " ").replace("ZXY", " ")
s = s.split()
print(max(s, key=len))
print(len(max(s, key=len)) - 3)