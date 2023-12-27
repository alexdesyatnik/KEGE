s = open("./24/24_12254.txt").readline().strip()

maxlen = 1

begin = 0
end = 0


# RSQ: R->S->Q->R

correct_next = {
    "R": "S",
    "S": "Q",
    "Q": "R",
}

while end < len(s) - 1:
    if s[end + 1] == correct_next[s[end]]:
        end += 1        
    else:
        begin = end + 1
        end = begin
    maxlen = max(maxlen, end - begin + 1)

print(maxlen)