def is_prime(n):
    for i in range(2, int(n ** 0.5 ) + 1):
        if n % i == 0:
            return False
    return True  


if __name__ == '__main__':
    a = [4, 7, 13, 127, 17, 44, 32, 38]
    #result = list(filter(is_prime, range(2, 1000)))
    result = [ v for v in a if is_prime(v) ]
    print(list(map(lambda v: v*v, a)))
    print(result)

            