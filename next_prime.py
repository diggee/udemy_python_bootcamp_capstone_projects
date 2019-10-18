# Next Prime Number - Have the program find prime numbers until the user chooses to stop asking for the next one.

import math


# next prime number
def isprime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for divisor in range(3, math.ceil(number / 2 + 1)):
            if number % divisor == 0:
                return False
        return True
    return False


def next_prime():
    yield 2
    number = 3
    while True:
        if isprime(number):
            yield number
        number += 2


p = next_prime()

while True:
    try:
        choice = int(input('Enter 1 for next prime number or 0 to abort: '))
    except ValueError:
        print('Invalid input. Please try again')
    if choice not in (0, 1):
        print('Error! Enter either 0 or 1')
        continue
    elif choice is 0:
        break
    else:
        print(next(p))
