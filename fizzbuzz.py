# flake8: noqa
"""
https://code-golf.io/fizz-buzz

Print the numbers from 1 to 100 inclusive, each on their own line.

If, however, the number is a multiple of three then print Fizz instead, and if
the number is a multiple of five then print Buzz.

For numbers which are multiples of both three and five then print FizzBuzz.
"""
def forma_basica():
    for i in range(1, 101):
        if(i % 3 == 0):
            print('Fizz', end='')
        if(i % 5 == 0):
            print('Buzz', end='')
        if(i % 3 != 0 and i % 5 != 0):
            print(i, end='')
        print()


def forma_uno():
    a = ['{}-fizz'.format(i) for i in range(1,16) if not i%3]
    b = ['{}-buzz'.format(i) for i in range(1,16) if not i%5]
    c = [str(i) for i in range(1,16) if i%3 and i%5]
    print(a)
    print(b)
    print(c)


def golf():
    i=0;exec("print(i%3//2*'Fizz'+i%5//4*'Buzz'or-~i);i+=1;"*100)


if __name__ == '__main__':
    golf()
