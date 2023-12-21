class Vacancy:

    def __init__(self, name, url, salary, description):
        self.description = description
        self.salary = salary
        self.url = url
        self.name = name

    def __repr__(self):
        return f'{self.name}, {self.salary}'

    def __str__(self):
        return f'{self.name}, {self.salary}'

    def __eq__(self, other):
        return self.salary == other.salary

    def __lt__(self, other):
        return self.salary < other.salary


