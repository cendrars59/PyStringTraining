# declare the encoding format when running the file
# -*-coding:Latin-1 -*

"""Form a complex number.
Main description
"""

from math import sqrt

NB_ITERATION = 10
OPTIONAL_PARAM1 = 1
OPTIONAL_PARAM2 = 1
WORD = "word"
EMAIL_TO_TEST = "toto@domaine.exte"



def calculation(nb_iteration):
    """Form a complex number.
    Main description
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
    choice = "o"
    while choice == "o":
        items.append(raw_input("enter the value: "))
        choice = raw_input("Voulez-vous continuez o ou n ?: ")
        if choice == "n":
            print "Vous quittez la saisie"
        else:
            print "Saisie invalide"
            choice = raw_input("Voulez-vous continuez o ou n ?: ")
    return items

def main():
    """
    Def de la fonction main()
    """
    print "Hello World"
    #calculation(NB_ITERATION)
    calculation_with_for()
    print 2017 % 400
    age = input("Quel est ton age olé")
    print age
main()
