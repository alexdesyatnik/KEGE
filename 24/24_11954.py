s = open("24_11954.txt").readline().split("Y")

min_len = 10**10
for substr in s:
    if substr.count("X") >= 500:
        l = 0
        r = 0
        x_count = int(substr[l] == "X")
        while r < len(substr):
            if x_count >= 500:
                min_len = min(min_len, r - l + 1)
                if substr[l] == "X":
                    x_count -= 1
                l += 1
            else:
                r += 1
                if r < len(substr) and substr[r] == "X":
                    x_count += 1

print(min_len)
