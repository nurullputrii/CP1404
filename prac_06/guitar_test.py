

from prac_06.guitar_class import Guitar

guitar_test = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar_age = guitar_test.get_age()
guitar_vintage = guitar_test.is_vintage()

another_guitar = Guitar("Another guitar", 2012, 10000)
another_age = another_guitar.get_age()
another_vintage = another_guitar.is_vintage()


print(guitar_test)
print("the guitar is {} years old".format(guitar_age))
print('vintage = {}'.format(guitar_vintage))

print(another_guitar)
print("the guitar is {} years old".format(another_age))
print('vintage = {}'.format(another_vintage))