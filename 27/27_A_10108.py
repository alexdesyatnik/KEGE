f = open("27_A_10108.txt")
k = int(f.readline())
n = int(f.readline())
data = []
for i in range(n):
    num = int(f.readline())
    data.append(num)

maxsum = -(10**10)
for i in range(n):
    for j in range(i + k, n):
        for m in range(j + k, n):
            s = data[i] + data[j] + data[m]
            maxsum = max(maxsum, s)

print(maxsum)
