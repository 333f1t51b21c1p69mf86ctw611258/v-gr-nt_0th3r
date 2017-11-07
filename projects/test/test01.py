class Person():
    name = 'Victor'
    def say(self, what):
        print(self.name, what)

getattr(Person, 'name')

attr_name = 'name'
person = Person()
getattr(person, attr_name)

getattr(person, 'say')('Hello')