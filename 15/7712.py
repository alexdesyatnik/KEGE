"""
((x & 17 ≠ 0) → ((x & A ≠ 0) → (x & 58 ≠ 0))) → ((x & 8  = 0) ∧ (x & A ≠ 0) ∧ (x & 58  = 0))
тождественно ложно
наименьшее A
"""


def f(x, A):
    return ((x & 17 != 0) <= ((x & A != 0) <= (x & 58 != 0))) <= (
        (x & 8 == 0) and (x & A != 0) and (x & 58 == 0)
    )


for A in range(1, 100):
    for x in range(1, 1000):
        if f(x, A):
            break
    else:
        print(A)
        break
