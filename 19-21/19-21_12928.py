def fn(s1, k, pb):
    if s1 >= 21:
        return k in pb
    if k > max(pb):
        return False
    moves = [fn(s1 + 1, k + 1, pb),
             fn(s1 * 2, k + 1, pb)]
    if k % 2 != pb[0] % 2:
        return any(moves)
    else:
        return all(moves)


for s in range(1, 20 + 1):
    if (fn(s, 0, [1]) == False and
            fn(s, 0, [3]) == True):
        print("19:", s)


for s in range(1, 20 + 1):
    if (fn(s, 0, [2]) == False and
            fn(s, 0, [2, 4]) == True):
        print("20:", s)


for s in range(1, 20 + 1):
    if (fn(s, 0, [1, 3, 5]) == True and
            fn(s, 0, [1]) == False and
            fn(s, 0, [3]) == False):
        print("21:", s)