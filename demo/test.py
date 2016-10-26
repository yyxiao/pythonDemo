
import math

def simple_generator_function():
    a = [1,2,3,4,5,6,7,8,9,0]
    for i in a:
        yield i


def re():
    for v in simple_generator_function():
        print(v)


def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 1
        print("get_primes:"+str(number))


def is_prime(number):               # 下面是 is_prime 的一种实现...
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False


if __name__ == '__main__':
    total = 2
    for next_prime in get_primes(3):
        print("next:"+str(next_prime))
        if next_prime < 4:
            total += next_prime
        else:
            print(total)
            exit()
