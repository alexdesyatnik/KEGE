s = open("./24_9552.txt").readline().strip()

"""
Определите максимальную длину подпоследовательности, которая состоит только из
пар символов PC, только из четверок символов CSGO, или из непересекающихся пар
символов PC и четверок символов CSGO.
"""

s = s.replace("PC", "**")
s = s.replace("CSGO", "****")

for letter in s:
    if letter != "*":
        s = s.replace(letter, " ")

lst = s.split()
print(len(max(lst, key=len)))
