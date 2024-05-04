file = open("26_14705.txt")
n = int(file.readline())
t = [0] * 5_000_000
for line in file:
    a, b = map(int, line.split())
    t[a] += 1
    t[b] -= 1

proc_count = 0
max_proc_count = 0
for i in range(5_000_000):
    proc_count += t[i]
    max_proc_count = max(proc_count, max_proc_count)

max_proc_time = 0
proc_count = 0
for i in range(5_000_000):
    proc_count += t[i]
    if proc_count == max_proc_count:
        max_proc_time += 1

print(max_proc_count, max_proc_time)