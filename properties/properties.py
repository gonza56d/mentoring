
class Glober:

    def __init__(self, first: str, last: str):
        self.first = first.title()
        self.last = last.title()

    @property
    def email(self):
        try:
            return f'{self.first.lower()}.{self.last.lower()}@globant.com'
        except AttributeError:  # First and/or last with none val will raise AttributeError
            return '404@globant.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, value: str):
        self.first, self.last = value.title().split(' ')

    @fullname.deleter
    def fullname(self):
        self.first, self.last = None, None


gonza = Glober('gonzalo', 'garcia')
print('Email:', gonza.email)
print('Fullname:', gonza.fullname)
print('Last name:', gonza.last)
gonza.fullname = 'gonza dambra'
print('Email:', gonza.email)
print('Fullname:', gonza.fullname)
print('Last name:', gonza.last)

del gonza.fullname
print(gonza.email)
