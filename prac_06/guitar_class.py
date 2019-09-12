""" Guitar class case from practical 2 """

class Guitar:
    def __init__(self, name='', year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return '{0} ({1}) : ${2}'.format(self.name, self.year, self.cost)

    def get_age(self):
        return 2019 - self.year

    def is_vintage(self):
        if self.get_age() > 50:
            return True
        else:
            return False
