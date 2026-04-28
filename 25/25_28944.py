def is_prime(n):
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True


c = 0
n = 8_996_453
while c < 5:
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            d2 = n // d
            if is_prime(d) and is_prime(d2):
                if str(d).count("3") == 2 and str(d2).count("3") == 2:
                    print(n, d2)
                    c += 1
    n += 1