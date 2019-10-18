import math
import random


# function to display pi upto n decimals
def pi_finder(precision):
    pi_value = math.acos(-1)
    print('The value of pi upto ' + str(precision) + ' decimal is:', end=' ')
    print(round(pi_value, precision))


# function to display e upto n decimals
def e_finder(precision):
    print('The value of e upto' + str(precision) + 'decimal is:', end=' ')
    print(round(math.e, precision))


# function to print the fibonacci series
def fibonacci(limit):
    a = 0
    b = 1
    print('Printing Fibonacci series upto ' + str(limit))
    while(a <= limit):
        print(a)
        a, b = b, a + b


# function to find out the prime factors of a number
def prime_factors(num):
    print('Prime factors of ' + str(num) + ' are:', end=' ')
    factors = []
    prime_factors = []
    for i in range(2, math.ceil(num / 2 + 1)):
        if num % i == 0:
            factors.append(i)
    for i in factors:
        for j in range(2, math.ceil(i / 2 + 1)):
            if i % j == 0:
                break
        prime_factors.append(i)

    print(prime_factors)


# simple calculator
def calculator(input, a, b):
    if input == 1:
        return a + b
    elif input == 2:
        return a - b
    elif input == 3:
        return a * b
    else:
        return a / b


# factorial
def factorial(n):
    result = 1
    while(n > 0):
        result = result * n
        n -= 1
    return result

    if n == 0:
        return 1


# complex nubmer algebra
def complex(input, a, b, c, d):
    if input == 1:
        return a + c, b + d
    if input == 2:
        return a - c, b - d
    if input == 3:
        return a * c + b * d * -1, a * d + b * c
    else:
        den = (c**2) + (d**2)
        num1 = (a * c + b * d * -1) / den
        num2 = (a * d + b * c) / den
        return num1, num2


# Happy numbers
def happy_numbers():
    numbers = []
    temp = []
    counter = 0
    no = 1
    start = 1
    while counter < 9:
        a = start / 1
        b = start % 10
        result = (a**2) + (b**2)
        temp.append(result)
        if result == 1:
            temp = []
            numbers.append(start)
            counter += 1
            no += 1
            start = no
            continue
        elif result in temp:
            temp = []
            no += 1
            start = no
            continue
        start = result
        continue
    return numbers


# Fast exponent
def fast_exponent(a, b):
    return math.e**(b * math.log(a))


# Coin flip
def coin_flip():
    return random.randint(1, 2)


def coin_flip_counter(choice):
    n_heads = 0
    n_tails = 0
    for i in range(0, choice):
        result = coin_flip()
        if result == 1:
            n_heads += 1
        else:
            n_tails += 1

    print('Number of heads: ' + str(n_heads))
    print('Number of tails: ' + str(n_tails))


# Numbers in words
def num_to_words(num):
    quotient = [num / 1, int(num / 10), int(num / 100), int(num / 1000), int(num / 10000), int(num / 100000)]
    ones = {1: 'one', 2: 'two', 3: 'three', 4: 'four',
            5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    mid_tens = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
                15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
    tens = {2: 'twenty', 3: 'thirty', 4: 'fourty', 5: 'fifty',
            6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety', 100: 'hundred'}
    num_string = ''
    count = 1
    for i in quotient[::-1]:
        if i is 0:
            count += 1
        else:
            if count is 1:
                num_string += ones[i] + ' hundred '
                count += 1
            elif count is 2:
                if i is 1:
                    num_string += mid_tens[i % 10] + ' '
                    count += 1
                else:
                    num_string += tens[i % 10] + ' '
                    count += 1
            elif count is 3:
                num_string += ones[i % 10] + ' thousand '
                count += 1
            elif count is 4:
                num_string += ones[i % 10] + ' hundred '
                count += 1
            elif count is 5:
                if i is 1:
                    num_string += mid_tens[i % 100] + ' '
                    count += 1
                else:
                    num_string += tens[i % 10] + ' '
                    count += 1
            else:
                num_string += ones[i % 10] + ' '

    print(num_string)


# Sieve of Eratosthenes
def eratosthenes(num):
    numbers = list(range(2, num + 1))
    for j in numbers:
        for i in range(0, len(numbers) + 1):
            if i >= len(numbers):
                break
            elif numbers[i] is j:
                continue
            elif numbers[i] % j == 0:
                numbers.pop(i)
        j += 1
    return numbers


# decimal to binary and reverse converter
def converter(number, choice):
    length = 0
    temp = number
    while(temp > 1):
        temp = temp/10
        length += 1
    sum = 0
    if choice == 1:
        for i in range(0, length):
            sum += (2**i) * (number % 10)
            number = int(number / 10)
        print(sum)

    elif choice == 2:
        quotient = number
        num_str = ''
        while quotient >= 1:
            remainder = quotient % 2
            quotient = int(quotient/2)
            num_str += str(remainder)
        print(num_str[::-1])

    else:
        print('Invalid input')


def caesar(word, caesar_key):
    alphabets = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j'
     , 11:'k', 12:'l', 13:'m', 14:'n', 15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t'
     , 21:'u', 22:'v', 23:'w', 24:'x', 25:'y', 26:'z'}
    new_word = ''
    for i in word:
        for key, value in alphabets.items():
            if value == i:
                letter_key = key
                break
        temp = letter_key + caesar_key
        if temp > 26:
            temp = temp - 26
        new_word += alphabets[temp]

    print(new_word)


# function calls
# pi_finder(5)
# e_finder(5)
# fibonacci(15)
# prime_factors(33)
# num_to_words(68541)
# print(eratosthenes(30))
# coin_flip_counter(10)
# print(fast_exponent(2, 3))
# print(happy_numbers())
# print(calculator(4, 2, 3))
# print(complex(3, 2, 3, 4, 5))
# caesar('hi', 20)
# converter(13,2)
