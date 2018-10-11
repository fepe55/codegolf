# flake8: noqa

"""
https://code-golf.io/emirp-numbers

Emirp Numbers
=============

An emirp (prime spelled backwards) is a prime number that results in a different prime when its decimal digits are reversed. For example both 13 and 31 are emirps.

Print all the emirp numbers from 1 to 1000 inclusive, each on their own line.
"""

def _is_prime(n):
    prime = True
    for i in range(2, n):
        if not n%i:
            prime=False
            break
    return prime


def regular():
    for number in range(10,1001):
        digits = str(number)
        reversed_number = int(str(number)[::-1])
        if number != reversed_number:
            if _is_prime(number) and _is_prime(reversed_number):
                print(number)


def golf():
 def p(n):return all(n%m for m in range(2,n))
 for n in range(12,1001):
  r=int(str(n)[::-1])
  if all([p(n),p(r)]):print(n)

if __name__ == '__main__':
    # regular()
    golf()
