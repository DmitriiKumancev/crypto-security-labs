from math import gcd

"""
реализация алгоритма факторизации числа на простые множители с использованием метода Полларда Rho.

Функции:
---------
1. is_prime(num):
    проверяет, является ли число простым.
    - Параметры:
        - `num`: Число для проверки.
    - Возвращает:
        - `True`, если число простое.
        - `False`, если число составное.

2. pollard_rho(n):
    применяет метод Полларда Rho для поиска нетривиального делителя числа n.
    - Параметры:
        - `n`: Число для факторизации.
    - Возвращает:
        - Нетривиальный делитель числа n.

3. factorize(n):
    факторизует число n на простые множители.
    - Параметры:
        - `n`: Число для факторизации.
    - Возвращает:
        - Список простых множителей числа n.

"""


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
    
def pollard_rho(n):
    if n % 2 == 0:
        return 2
    x, y, c = 2, 2, 1
    f = lambda x: (x**2 + c) % n
    
    while True:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)
        if d == n:
            c += 1
            x, y = 2, 2
            continue
        elif d > 1:
            return d

def factorize(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
        
    if n > 1:
        while not is_prime(n):
            factor = pollard_rho(n)
            if factor is not None:
                while n % factor == 0:
                    factors.append(factor)
                    n //= factor
        if n > 1:
            factors.append(n)

    return factors

number = 8051
factors = factorize(number)
print(f"Число {number} разложено на множители: {factors}") # [97, 83]