f = open("26_12478.txt")

n, start, stop = [int(s) for s in f.readline().split()]
data = []
for _ in range(n):
    ab = [int(s) for s in f.readline().split()]
    data.append(ab)

data.sort()
start0 = start
ans = [data[0]]
for ab in data:
    if ab[0] <= start:
        if ab[1] - start > ans[-1][1] - start:
            ans[-1] = ab
    else:
        start = ans[-1][1]
        if start >= stop:
            break
        ans.append(ab)

#print(ans)
print(len(ans))
print(ans[0][1] - start0)
