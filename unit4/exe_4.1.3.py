def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def first_prime_over(n):
    prime_gen = (x for x in range(n + 1, n + 1000000) if is_prime(x))
    return next(prime_gen)


if __name__ == '__main__':
    print(first_prime_over(1000000))