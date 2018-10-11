# flake8: noqa

"""
https://code-golf.io/pernicious-numbers

Pernicious Numbers
=============

A pernicious number is a positive number where the sum of its binary expansion is a prime number.

For example, 5 is a pernicious number since 5 = 1012 and 1 + 1 = 2, which is prime.

Print all the pernicious numbers from 0 to 50 inclusive, each on their own line.
"""

def _is_prime(n):
    prime = True
    for i in range(2, n):
        if not n%i:
            prime=False
            break
    return prime and n > 1

def regular():
    for number in range(51):
        binary = bin(number)[2:]
        s = 0
        for digit in str(binary):
            s+=int(digit)
        if _is_prime(s):
            print(number)


def golf():
 def p(n):return all(n%m for m in range(2,n))and n>1

 for i in range(51):
  if p(sum([int(x)for x in bin(i)[2:]])):print(i)

if __name__ == '__main__':
    # regular()
    golf()
