f = open("26_13101.txt")
n = int(f.readline())
clients = [[int(x) for x in line.split()] for line in f]
clients.sort()

windows = [[], []]
window2_count = 0
left_count = 0

for time, duration, win_num in clients:
    windows[0] = [end_time for end_time in windows[0] if end_time > time]
    windows[1] = [end_time for end_time in windows[1] if end_time > time]
    if win_num == 0:
        win_num = 1 if len(windows[0]) <= len(windows[1]) else 2
    win_num -= 1
    if len(windows[win_num]) >= 14:
        left_count += 1
    else:
        if win_num == 1:
            window2_count += 1
        if len(windows[win_num]) == 0:
            windows[win_num].append(time + duration)
        else:
            windows[win_num].append(windows[win_num][-1] + duration)

print(window2_count, left_count)
