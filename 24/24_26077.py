s = open("24_26077.txt").readline().strip()

# Определите в прилагаемом файле последовательность из максимального количества идущих подряд символов,
# среди которых ровно 45 нечётных цифр и при этом начинающуюся с буквы G, не содержащую других букв G, кроме первой.

s = s.replace("3", "1").replace("5", "1").replace("7", "1").replace("9", "1")

s = s.replace("G", " G")
m = s.split()

def limit1(s):
    pos = 0
    count = 0
    for i in range(len(s)):
        if s[i] == "1":
            count += 1
        if count > 45:
            return s[:i]
    return s

m = [limit1(k) for k in m if k.count("1") >= 45]
maxlen = len(max(m, key=len))
print(maxlen)
