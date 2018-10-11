# flake8: noqa

"""
https://code-golf.io/niven-numbers

Niven Numbers
==============

A niven number is a non-negative number that is divisible by the sum of its digits.

Print all the niven numbers from 0 to 100 inclusive, each on their own line.
"""
def regular():
    for i in range(101):
        sum = 0
        for digit in str(i):
            sum += int(digit)
        if sum and not i % sum:
            print(i)

def golf():
 for i in range(1,101):
  if not i%sum([int(x)for x in str(i)]):
   print(i)


if __name__ == '__main__':
    # regular()
    golf()
