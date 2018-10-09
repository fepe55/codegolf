# flake8: noqa
"""
https://code-golf.io/evil-numbers

An evil number is a non-negative number that has an even number of 1s in its binary expansion.

Print all the evil numbers from 0 to 50 inclusive, each on their own line.

Numbers that are not evil are called odious numbers.
"""

def regular():
    for i in range(51):
        ones = 0
        binary = bin(i)[2:]
        for d in binary:
            if d == '1':
                ones += 1
        if not ones % 2:
            print(i)

def golf():
 for i in range(51):
  if not sum([int(x)for x in bin(i)[2:]])%2:print(i)


if __name__ == '__main__':
    # regular()
    golf()
