#!/usr/bin/env python3
import math


def eratosthenes(upper_bound):
    primes = []
    numbers_to_upper_bound = [i for i in range(2, upper_bound)]

    current = 2
    while current < math.sqrt(upper_bound):
        for i in range(current, upper_bound, current):
            if i in numbers_to_upper_bound:
                numbers_to_upper_bound.remove(i)

        primes.append(current)
        current = numbers_to_upper_bound[0]

    primes = primes + numbers_to_upper_bound
 
    return primes


if __name__ == '__main__':
    primes = eratosthenes(100000)
    print(primes)