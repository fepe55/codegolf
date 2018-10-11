# flake8: noqa

"""
https://code-golf.io/12-days-of-christmas

12 Days of Christmas
====================

Print the lyrics to the song The 12 Days of Christmas:

"""
def regular():
    stuff = [
        'Twelve Drummers Drumming,',
        'Eleven Pipers Piping,',
        'Ten Lords-a-Leaping,',
        'Nine Ladies Dancing,',
        'Eight Maids-a-Milking,',
        'Seven Swans-a-Swimming,',
        'Six Geese-a-Laying,',
        'Five Gold Rings,',
        'Four Calling Birds,',
        'Three French Hens,',
        'Two Turtle Doves, and',
        'A Partridge in a Pear Tree.',
    ]

    days = [
        'First',
        'Second',
        'Third',
        'Fourth',
        'Fifth',
        'Sixth',
        'Seventh',
        'Eighth',
        'Ninth',
        'Tenth',
        'Eleventh',
        'Twelfth',
    ]

    for i, day in enumerate(days):
        print('On the {} day of Christmas'.format(day))
        print('My true love sent to me')
        j = i+1
        print('\n'.join(stuff[-j:]))
        print()


def golf():
 s=['Twelve Drummers Drumming,','Eleven Pipers Piping,','Ten Lords-a-Leaping,','Nine Ladies Dancing,','Eight Maids-a-Milking,','Seven Swans-a-Swimming,','Six Geese-a-Laying,','Five Gold Rings,','Four Calling Birds,','Three French Hens,','Two Turtle Doves, and','A Partridge in a Pear Tree.']
 w=['First','Second','Third','Fourth','Fifth','Sixth','Seventh','Eighth','Ninth','Tenth','Eleventh','Twelfth']
 for i,d in enumerate(w):print('On the %s day of Christmas\nMy true love sent to me\n'%d+'\n'.join(s[-i-1:])+'\n')


if __name__ == '__main__':
    # regular()
    golf()
