# kompege.ru
# № 7417 Вариант от ChatGPT (Уровень: Средний)

from random import shuffle


def alg(s):
    while ">1" in s or ">2" in s or ">0" in s:
        s = s.replace(">1", "22>", 1)
        s = s.replace(">2", "2>", 1)
        s = s.replace(">0", "1>", 1)
    return s


def is_prime(n):
    for d in range(2, n):
        if n % d == 0:
            return False
    return True


def sum_digits(s):
    return sum(map(int, filter(lambda ch: ch.isdigit(), s)))


for n in range(1, 10):
    # Рандомизация на самом деле не нужна, т.к. алгоритм выдаёт
    # строку с одинаковой суммой цифр для данного n при любом их расположении
    # Но для того, чтобы понять это, нужно вчитываться в алгоритм
    for _ in range(1000):
        s = list("0" * 37 + "1" * n + "2" * 37)
        shuffle(s)
        s = ">" + "".join(s)
        s2 = alg(s)
        if is_prime(sum_digits(s2)):
            print(n)
            break
