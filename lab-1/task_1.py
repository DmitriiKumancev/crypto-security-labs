def extended_gcd(a, b):
    """
    Расширенный алгоритм Евклида для нахождения НОД(a, b) и коэффициентов x, y таких, что a * x + b * y = НОД(a, b).

    Parameters:
    a (int): Первое число.
    b (int): Второе число.

    Returns:
    tuple: Кортеж (g, x, y), где g - НОД(a, b), x и y - коэффициенты.

    """
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extended_gcd(b % a, a)
        return (g, y - (b // a) * x, x)

def mod_inverse(e, n):
    """
    Вычисляем мультипликативный обратный элемент d для числа e по модулю n.

    Parameters:
    e (int): Число для которого нужно найти обратный элемент.
    n (int): Модуль.

    Returns:
    int: Мультипликативный обратный элемент d.
    None: Если обратного элемента не существует (если НОД(e, n) != 1).

    """
    g, x, _ = extended_gcd(e, n)
    if g == 1:
        return x % n if x >= 0 else n + x
    else:
        return None  

variants = [(15, 82), (58, 115), (29, 86), (24, 95), (49, 122), (18, 107), (15, 38)]

for e, n in variants:
    d = mod_inverse(e, n)
    print(f'For e = {e}, n = {n}, the multiplicative inverse d is: {d}')
