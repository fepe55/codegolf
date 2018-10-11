# flake8: noqa

"""
https://code-golf.io/odious-numbers

Odious Numbers
==============

An odious number is a non-negative number that has an odd number of 1s in its binary expansion.

Print all the odious numbers from 0 to 50 inclusive, each on their own line.

Numbers that are not odious are called evil numbers.

"""

def regular():
    for i in range(51):
        ones = 0
        binary = bin(i)[2:]
        for d in binary:
            if d == '1':
                ones += 1
        if ones % 2:
            print(i)

def golf():
 for i in range(51):
  if sum([int(x)for x in bin(i)[2:]])%2:print(i)


if __name__ == '__main__':
    regular()
    # golf()
