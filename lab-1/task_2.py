import random
import math

def sieve_of_eratosthenes(n):
    """
    Реализация алгоритма Решето Эратосфена для нахождения простых чисел до заданного числа n.

    Parameters:
    n (int): Верхний предел для поиска простых чисел.

    Returns:
    list: Список простых чисел до n.
    """
    primes = []
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if sieve[p]:
            primes.append(p)
            for i in range(p*p, n+1, p):
                sieve[i] = False
    return primes

def fermat_test(n, k=5):
    """
    Тест простоты Ферма для числа n.

    Parameters:
    n (int): Проверяемое число.
    k (int): Количество итераций теста (по умолчанию 5).

    Returns:
    bool: True, если число вероятно простое, False в противном случае.
    """

    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for _ in range(k):
        a = random.randint(2, n - 1)
        if pow(a, n-1, n) != 1:
            return False
    return True

def miller_rabin_test(n, k=5):
    """
    Тест простоты Миллера-Рабина для числа n.

    Parameters:
    n (int): Проверяемое число.
    k (int): Количество итераций теста (по умолчанию 5).

    Returns:
    bool: True, если число вероятно простое, False в противном случае.
    """

    if n == 2:
        return True
    if n % 2 == 0:
        return False

    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1:
            return True
        for _ in range(s - 1):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return x == n - 1

    s = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1
        s += 1

    for _ in range(k):
        a = random.randint(2, n - 1)
        if not check(a, s, d, n):
            return False
    return True

def generate_prime(bits):
    """
    Генерирует простое число с битовой длиной bits.

    Parameters:
    bits (int): Битовая длина для генерации простых чисел.

    Returns:
    int: Сгенерированное простое число.
    """

    while True:
        candidate = random.getrandbits(bits)
        candidate |= (1 << bits - 1) | 1
        if fermat_test(candidate) and miller_rabin_test(candidate):
            return candidate

def save_keys(p, q):
    """
    Сохраняет простые числа p и q в файл 'prime_numbers.txt'.

    Parameters:
    p (int): Первое простое число.
    q (int): Второе простое число.

    """
    
    with open('prime_numbers.txt', 'w') as file:
        file.write(f"p: {p}\nq: {q}")

def main():
    n = 250  # количество простых чисел для решета Эратосфена
    bits = 512  # битовая длина для генерации простых чисел

    primes = sieve_of_eratosthenes(n)
    p = random.choice(primes)
    q = random.choice(primes)

    while p == q:
        q = random.choice(primes)

    while math.log2(p * q) < 128:
        p = generate_prime(bits)
        q = generate_prime(bits)

    save_keys(p, q)
    print("Ключи успешно сохранены в файл 'prime_numbers.txt'")

if __name__ == "__main__":
    main()
