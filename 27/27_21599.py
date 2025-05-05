from math import dist

m = [
    tuple(map(float, line.replace(",", ".").split()))
    for line in open("27_B_21599.txt")
]

clusters = []
r = 1.5
while m:
    clusters.append([m.pop()])
    for p2 in clusters[-1]:
        for p1 in m:
            if dist(p1, p2) < r:
                clusters[-1].append(p1)
                m.remove(p1)

def find_center(c):
    min_d = 10 ** 10
    min_p = None
    for p in c:
        d = 0
        for other_p in c:
            d += dist(p, other_p)
        if min_d > d:
            min_d = d
            min_p = p
    return min_p

centers = [find_center(c) for c in clusters]
avg_x = sum(p[0] for p in centers) / len(centers)
avg_y = sum(p[1] for p in centers) / len(centers)
print(abs(int(avg_x * 10000)), abs(int(avg_y * 10000)))