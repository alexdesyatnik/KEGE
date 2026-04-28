f = open("26_28945.txt")
n = int(f.readline())

data = []
for line in f:
    begin, length = line.split()
    begin, length = int(begin), int(length)
    data.append((begin, length, begin + length))

data.sort(key=lambda d: d[2])

chosen = [data[0]]
for b, l, e in data[1:]:
    if b < chosen[-1][2]:
        continue
    chosen.append((b, l, e))

for b, l, e in data:
    if b >= chosen[-1][0] and e > chosen[-1][2]:
        chosen[-1] = (b, l, e)

print(len(chosen), 10000 - chosen[-1][2])