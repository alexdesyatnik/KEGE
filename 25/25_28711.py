# Напишите программу, которая перебирает целые числа, большие 2 400 000, в порядке возрастания
# и ищет среди них числа, представимые в виде произведения ровно трёх различных простых множителей,
# каждый из которых содержит в своей записи хотя бы одну цифру 4 или 7. В ответе запишите первые
# пять чисел в порядке возрастания, справа от каждого числа запишите его наибольший простой делитель.

def is_prime(n):
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True

primes = [n for n in range(2, 30000) if is_prime(n) and ("4" in str(n) or "7" in str(n))]

nums = []
for i in range(len(primes) - 2):
    p1 = primes[i]
    if p1 * p1 * p1 > 2_400_000 * 2:
        break
    for j in range(i + 1, len(primes) - 1):
        p2 = primes[j]
        if p1 * p2 * p2 > 2_400_000 * 2:
            break
        for k in range(j + 1, len(primes)):
            p3 = primes[k]
            p = p1 * p2 * p3
            if p > 2_400_000 * 2:
                break
            if p > 2_400_000:
                nums.append((p, max(p1, p2, p3)))
nums = sorted(nums)
print(*nums[:5], sep="\n")