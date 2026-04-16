import math

f = open("27_A_28766.txt")
stars = []
for line in f:
    x, y, info = line.split()
    x = float(x)
    y = float(y)
    stars.append([(x, y), info])

all_stars = stars[:]

clusters = []
eps = 1
while len(stars) > 0:
    clusters.append([stars.pop()])
    for p1 in clusters[-1]:
        for p2 in stars:
            if math.dist(p1[0], p2[0]) < eps:
                clusters[-1].append(p2)
                stars.remove(p2)

print(len(clusters))
for c in clusters:
    print(len(c))

def find_center(cl):
    mindist = 10 ** 10
    center = None
    for p1 in cl:
        sumdist = 0
        for p2 in cl:
            sumdist += math.dist(p1[0], p2[0])
        if sumdist < mindist:
            mindist = sumdist
            center = p1
    return center

# Задача A - нужен только центр кластера с наименьшим кол-вом звезд
center = find_center(clusters[1])

mindist = 10 ** 10
maxdist = 0
for p in all_stars:
    if "Y" in p[1] and "III" in p[1]: # красный гигант
        d = math.dist(p[0], center[0])
        mindist = min(mindist, d)
        maxdist = max(maxdist, d)
print("A:", int(mindist * 10000), int(maxdist * 10000))


