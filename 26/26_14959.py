file = open("26_14959.txt")
k, n = map(int, file.readline().split())
data = []
for line in file:
    s, t = map(int, line.split())
    data.append([s, s + t])

data.sort(key=lambda x: x[1])
chosen = [data[0]]
for begin, end in data[1:]:
    if begin >= chosen[-1][1]:
        chosen.append([begin, end])

second_last_end = chosen[-2][1]
best_last = min(task for task in data if task[0] >= second_last_end)

print(len(chosen) * k, best_last[0])