f = open("26_28945.txt")
n = int(f.readline())

data = []
for line in f:
    begin, length = line.split()
    begin, length = int(begin), int(length)
    data.append([begin, begin + length])

data.sort(key=lambda d: d[1])

chosen = [data[0]]
for d in data[1:]:
    if d[0] < chosen[-1][1]:
        continue
    chosen.append(d)

for d in data:
    if d[0] >= chosen[-1][0] and d[1] > chosen[-1][1]:
        chosen[-1] = d

print(len(chosen), 10000 - chosen[-1][1])