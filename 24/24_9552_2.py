s = open("24_9552.txt").readline().strip()

m = [0] * len(s)
for i in range(1, len(s)):
    if s[i-1:i+1] == "PC":
        m[i] = m[i - 2] + 2
    if i >= 3 and s[i-3:i+1] == "CSGO":
        m[i] = m[i - 4] + 4
print(max(m))