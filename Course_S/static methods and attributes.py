# static attributes
# self was referint to the instance
# class attributes are attributes specific to the class

class Person:
    number_of_people = 0 # this is a class attribute
                        # it's not a regular attribute, it's not defined inside a method
                        # it doesn't have any access to an instance of a class
                        # is defined for the entire class
                        # it will not change for every person
                        # the value will be the same

    def __init__(self, name):
        self.name = name

person1 = Person("Lina")
person2 = Person("Tom")

Person.number_of_people = 8 # scriem Person. pt ca este specific clasei, nu instantei
print(person2.number_of_people)

Person.number_of_people = 3
print(person1.number_of_people)

print(Person.number_of_people)


####
x = 5.5
print(round(x))



