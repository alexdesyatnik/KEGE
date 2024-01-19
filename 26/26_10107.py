def intersects(a, b):
    if a[1] <= b[0] or b[1] <= a[0]:
        return False
    return True

file = open("26_10107.txt")
n = int(file.readline())
lst = []
for line in file:
    a, b = line.split()
    lst.append([int(a), int(b)])

lst.sort(key=lambda i: i[1])
res = [lst[0]]
for i in lst[1:]:
    if not intersects(i, res[-1]):
        res.append(i)

print(len(res))
print(res[-1][0] - res[-2][1])