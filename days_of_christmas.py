# flake8: noqa
"""
Print the lyrics to the song The 12 Days of Christmas:

"""
def forma_basica():
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
 for i,d in enumerate(w):
  print('On the {} day of Christmas'.format(d))
  print('My true love sent to me')
  print('\n'.join(s[-i-1:]))
  print()


if __name__ == '__main__':
    golf()
