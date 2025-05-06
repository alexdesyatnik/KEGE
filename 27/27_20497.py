from math import dist

m = [[float(x) for x in line.split()]
    for line in open("27.19.A_20497.txt")]

c1 = []
c2 = []
c3 = []

for x, y in m:
    if -1 < x < 1.5 and 1 < y < 6:
        c1.append([x, y])
    elif -2.7 < x < 0 and -5 < y < 0.5:
        c2.append([x, y])
    elif 0.6 < x < 3.1 and -5 < y < 0:
        c3.append([x, y])

def find_edge(c):
    maxd = 0
    maxp = None
    for p in c:
        d = 0
        for p1 in c:
            d += dist(p, p1)
        if d > maxd:
            maxd = d
            maxp = p
    return maxp

e1 = find_edge(c1)
e2 = find_edge(c2)
e3 = find_edge(c3)

print(int((e1[0] + e2[0] + e3[0]) / 3 * 10000))
print(int((e1[1] + e2[1] + e3[1]) / 3 * 10000))

