import random
import hashlib

"""
реализация алгоритма цифровой подписи на основе алгоритма подписи ГОСТ Р 34.10-2012 (ЭЦП в кольце вычетов).

---------
1. extended_gcd(a, b):
    вычисляет расширенный алгоритм Евклида для нахождения обратного элемента в кольце вычетов.

2. generate_prime(bits):
    генерирует простое число с заданным количеством битов.

3. generate_keys(bits):
    генерирует ключи для алгоритма подписи. Включает генерацию простого числа `p`, случайного числа `g` (генератора), 
    случайного числа `x` (закрытого ключа) и вычисление открытого ключа `y`.

4. hash_message(message):
    хеширует сообщение с использованием SHA-256.

5. sign(message, p, g, x):
    подписывает сообщение. Включает генерацию случайного числа `k`, вычисление `r` и `s` - компонентов подписи.

6. verify(message, signature, p, g, y):
    проверяет подпись сообщения. Вычисляет `v1` и `v2` и сравнивает их для определения действительности подписи.

"""


# Функция для вычисления обратного элемента в кольце вычетов
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

# Функция для генерации простого числа
def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if num > 1 and pow(2, num-1, num) == 1:
            return num

# Функция для генерации ключей
def generate_keys(bits):
    p = generate_prime(bits)
    g = random.randint(2, p - 2)
    x = random.randint(2, p - 2)
    y = pow(g, x, p)
    return p, g, y, x

# Функция для хеширования сообщения
def hash_message(message):
    return int(hashlib.sha256(message.encode()).hexdigest(), 16)

# Функция для подписи сообщения
def sign(message, p, g, x):
    k = random.randint(2, p - 2)
    while extended_gcd(k, p - 1)[0] != 1:
        k = random.randint(2, p - 2)
    r = pow(g, k, p)
    k_inv = extended_gcd(k, p - 1)[1] % (p - 1)
    h = hash_message(message)
    s = (k_inv * (h - x * r)) % (p - 1)
    return r, s

# Функция для проверки подписи
def verify(message, signature, p, g, y):
    r, s = signature
    if r < 1 or r > p - 1 or s < 1 or s > p - 2:
        return False
    h = hash_message(message)
    v1 = pow(g, h, p)
    v2 = (pow(y, r, p) * pow(r, s, p)) % p
    return v1 == v2

# Пример использования
if __name__ == "__main__":
    # Генерация ключей
    p, g, y, x = generate_keys(128)

    # Сообщение для подписи
    message = "Hello, world!"

    # Подписание сообщения
    signature = sign(message, p, g, x)

    # Проверка подписи
    if verify(message, signature, p, g, y):
        print("Подпись верна")
    else:
        print("Подпись недействительна")
