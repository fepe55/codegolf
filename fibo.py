# flake8: noqa

"""
https://code-golf.io/fibonacci

Print the first 31 Fibonacci numbers from F0 = 0 to F30 = 832040 (inclusive),
each on a separate line.

"""

def regular():
    def fibo(i):
        if i==0 or i==1:
            return i
        else:
            return fibo(i-1) + fibo(i-2)

    for i in range(31):
        print(fibo(i))

def golf():
    def f(i):return i if i<2 else f(i-1)+f(i-2)
    # def f(i):return i and i<2 or f(i-1)+f(i-2)
    # def f(i):return [i,f(i-1)+f(i-2)][i>1]
    i=0;exec('print(f(i));i+=1;'*31)



if __name__ == '__main__':
    # regular()
    golf()
