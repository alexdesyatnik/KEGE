s = open("24_10105.txt").readline().strip()

maxlen = 0
begin = 0  # включительно
end = 0  # НЕ включительно
count_t = 0

while end < len(s):
    end += 1
    if end % 100000 == 0:
        print(".", end="")
    if s[end - 1] == 'T':
        count_t += 1
    if count_t == 100:
        maxlen = max(maxlen, end - begin)
    elif count_t > 100:
        begin = s.find('T', begin) + 1
        count_t -= 1

print()
print(maxlen)