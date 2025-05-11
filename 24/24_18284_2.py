s = open("24_18284.txt").readline()
o = s.find('O')
v = s.find('V')
e = s.find('E')
minlen = 100000000
begin = 0
for l in range(80000, len(s)):
    if s[l] == 'L':
        begin = l
        if begin > o:
            o = s.find('O', o + 1)
        if o > v:
            v = s.find('V', v + 1)
        if v > e:
            e = s.find('E', e + 1)
        if e - begin + 1 < minlen:
            minlen = e - begin + 1

print(minlen)