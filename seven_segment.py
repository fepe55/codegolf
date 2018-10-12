# flake8: noqa
"""
https://code-golf.io/seven-segment#python

Seven Segment
=============

Using pipes and underscores print the argument as if it were displayed on a seven segment display.

For example the number 0123456789 should be displayed as
"""

def regular():
    up = ' _ '
    not_up = '   '
    no_up = [1,4]

    middle = [
        '| |',  # 0

        '  |',  # 1, 7

        ' _|',  # 2, 3

        ' _|',  # 2, 3

        '|_|',  # 4, 8, 9

        '|_ ',  # 5, 6

        '|_ ',  # 5, 6

        '  |',  # 1, 7

        '|_|',  # 4, 8, 9

        '|_|',  # 4, 8, 9
    ]

    down = [
        '|_|',  # 0, 6, 8

        '  |',  # 1, 4, 7

        '|_ ',  # 2

        ' _|',  # 3, 5, 9

        '  |',  # 1, 4, 7

        ' _|',  # 3, 5, 9

        '|_|',  # 0, 6, 8

        '  |',  # 1, 4, 7

        '|_|',  # 0, 6, 8

        ' _|',  # 3, 5, 9
    ]

    number = '01234567890'
    # print(''.join([not_up if int(x) in no_up else up for x in number]))
    # print(''.join([middle[int(x)] for x in number]))
    # print(''.join([down[int(x)] for x in number]))

    print('\n'.join([
        ''.join([not_up if int(x) in no_up else up for x in number]),
        ''.join([middle[int(x)] for x in number]),
        ''.join([down[int(x)] for x in number]),
    ]))



def golf():
 import sys
 n=sys.argv[1]
 c='| |'
 d='  |'
 e=' _|'
 f='|_|'
 g='|_ '
 m=[c,d,e,e,f,g,g,d,f,f]
 d=[f,d,g,e,d,e,f,d,f,e]
 print('\n'.join([''.join(['   'if int(x) in [1,4] else ' _ ' for x in n]),''.join([m[int(x)] for x in n]),''.join([d[int(x)] for x in n])]))


if __name__ == '__main__':
    regular()
