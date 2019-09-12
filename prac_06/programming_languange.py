"""Programming Language practical"""

class ProgrammingLanguage:
    """Represent a Programming Language object"""

    def __init__(self, language_name = "", typing="", reflection="", year=''):
        self.language_name = language_name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.reflection

    def __str__(self):
        return '{0}, {1} typing, reflection={2}, first appeared in {3}'.format(self.language_name, self.typing,
                                                                               self.reflection, self.year)

    """ Printing the list """
    def __repr__(self):
        return '{0}, {1} typing, reflection={2}, first appeared in {3}'.format(self.language_name, self.typing,
                                                                               self.reflection, self.year)









