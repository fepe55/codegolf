# flake8: noqa

"""
https://code-golf.io/happy-numbers

Happy Numbers
=============

A happy number is defined by the following sequence: Starting with any positive
integer, replace the number by the sum of the squares of its digits in
base-ten, and repeat the process until the number either equals 1 (where it
will stay), or it loops endlessly in a cycle that does not include 1.
Those numbers for which this process ends in 1 are happy numbers, while those
that do not end in 1 are sad numbers.

For example, 19 is happy, as the associated sequence is:

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1.
Print all the happy numbers from 1 to 200 inclusive, each on their own line.
"""


def regular():
    def is_happy(number, prev_values):
        current_value = 0
        for digit in str(number):
            current_value += pow(int(digit), 2)
        if current_value == 1:
            return True
        if current_value in prev_values:
            return False
        prev_values.append(current_value)
        return is_happy(current_value, prev_values)

    for i in range(201):
        if is_happy(i, []):
            print(i)

def golf():
 def h(n,a):
  v=0
  for d in str(n):
   v+=int(d)**2
  if v==1:return 1
  if v in a:return 0
  a+=[v]
  return h(v,a)
 # for i in range(201):
  # if h(i,[]):print(i)
 print('\n'.join([str(i) for i in range(201) if h(i,[])]))
 # i=0;exec('if h(i,[]):print(i);i+=1;'*201)


if __name__ == '__main__':
    # regular()
    golf()
