s = open("24_10105.txt").readline()

max_len = 0
l = 0
r = 0
t_count = int(s[l] == "T")
while r < len(s):
    if t_count == 100:
        max_len = max(max_len, r - l + 1)
        if s[l] == "T":
            t_count -= 1
        l += 1
    else:
        r += 1
        if r < len(s) and s[r] == "T":
            t_count += 1
print(max_len)
