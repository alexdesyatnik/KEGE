s = open("./24/24_12254.txt").readline().strip()

# RSQ: R->S->Q->R
correct_next = {
    "R": "S",
    "S": "Q",
    "Q": "R",
}

maxlen = 1
currlen = 1

for i in range(1, len(s)):
    if s[i] == correct_next[s[i - 1]]:
        currlen += 1
        maxlen = max(maxlen, currlen)
    else:
        currlen = 1

print(maxlen)