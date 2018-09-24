# flake8: noqa
"""
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


def forma_basica():
    def is_happy(numero, valores_anteriores):
        valor_actual = 0
        for digito in str(numero):
            valor_actual += pow(int(digito), 2)
        if valor_actual == 1:
            return True
        if valor_actual in valores_anteriores:
            return False
        valores_anteriores.append(valor_actual)
        return is_happy(valor_actual, valores_anteriores)

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
    # forma_basica()
    golf()
