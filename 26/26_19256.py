f = open("26_19256.txt")
n = int(f.readline())
tasks = dict()
for line in f:
    s_id, t_id = map(int, line.split())
    if s_id in tasks:
        tasks[s_id].add(t_id)
    else:
        tasks[s_id] = {t_id}

# определяем наибольшую длину последовательности чисел без пропусков
# в коллекции m
def longest_span(m) -> int:
    m = sorted(m)
    maxlen = 0
    currlen = 1
    for i in range(1, len(m)):
        if m[i] - m[i-1] == 1:
            currlen += 1
        else:
            currlen = 1
        maxlen = max(maxlen, currlen)
    return maxlen

max_s_id = 0
max_tasks = 0
for s_id in sorted(tasks.keys()):
    task_span = longest_span(tasks[s_id])
    if task_span > max_tasks:
        max_tasks = task_span
        max_s_id = s_id
print(max_s_id, max_tasks)