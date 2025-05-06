import fnmatch
s = open("24_18284.txt").readline()

lis = [i for i in range(len(s)) if s[i] == "L"]
ois = [i for i in range(len(s)) if s[i] == "O"]
vis = [i for i in range(len(s)) if s[i] == "V"]
eis = [i for i in range(len(s)) if s[i] == "E"]

minlen = 10 ** 10
oi = vi = ei = 0
for li in lis:
    while ois[oi] < li: oi += 1
    while vis[vi] < ois[oi]: vi += 1
    while eis[ei] < vis[vi]: ei += 1
    minlen = min(minlen, eis[ei] - li + 1)
print(minlen)

