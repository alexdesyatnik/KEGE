f = open("26_12478.txt")

n, start, stop = [int(s) for s in f.readline().split()]
data = []
for _ in range(n):
    ab = [int(s) for s in f.readline().split()]
    data.append(ab)

data.sort()
start0 = start
ans = []
last_chosen = data[0]
for ab in data:
    if ab[0] <= start:
        if ab[1] - start > last_chosen[1] - start:
            last_chosen = ab
    else:
        ans.append(last_chosen)
        start = last_chosen[1]
        last_chosen = ab
        if start >= stop:
            break

#print(ans)
print(len(ans))
print(ans[0][1] - start0)
