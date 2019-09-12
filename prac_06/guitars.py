from prac_06.guitar_class import Guitar

""" Importing a class from the file """

user_input = ""


list_guitar = [Guitar("Gibson L-5 CES", 1922, 16035.40),
                   Guitar("Line 6 JTV-59", 2010, 1512.9)]

while user_input == '':
    name = str(input('Name: '))
    if name != '':
        year = int(input('Year: '))
        cost = int(input('Cost: '))
        guitar_test = Guitar(name, year, cost)
        list_guitar.append(guitar_test)

    else:
        print("These are my guitars:")
        count = 1
        for guitar in list_guitar:
            vintage_string = '(vintage)' if guitar.is_vintage() else ""
            print("Guitar {0}: {1:>20} ({2}), worth ${3:10,.2f}{4}".format(count, guitar.name, guitar.year, guitar.cost,
                                                                      vintage_string))
            count += 1

        break







