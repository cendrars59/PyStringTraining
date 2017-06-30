# declare the encoding format when running the file
# -*-coding:Latin-1 -*

"""Form a complex number.

    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)
"""

from math import sqrt

NB_ITERATION = 10
OPTIONAL_PARAM1 = 1
OPTIONAL_PARAM2 = 1
WORD = 'word'



def calculation(nb_iteration):
    """example of docstrings.

    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)
    """
    i = 0
    while i < nb_iteration:
        print sqrt(i)
        i += 1

def calculation_with_for():
    """
    enter the item into the list
    """
    temp_items = get_the_items()

    for item in temp_items:
        print item

def get_the_items():
    """
    enter the item into the list
    """
    items = []
    choice = 'o'
    print choice
    while choice == 'o':
        value = input('enter the value')
        items.append(str(value))
        print items
        choice = str(input('do you want to continue'))
        print choice
        if choice != 'n' or choice != 'o':
            print 'Rentre un valeur correcte connard'
            choice = input('do you want to continue')

    return items

def main():
    """
    ta mère en short
    """
    print "Hello World"
    #calculation(NB_ITERATION)
    calculation_with_for()
    print 2017 % 400
    age = input('Quel est ton age olé')
    print age
main()
