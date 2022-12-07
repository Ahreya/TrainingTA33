# create classes

# cream o clasa Dog si scriem atributele clasei Dog
# definim o clasa Dog folosing cuvantul cheie class

class Dog:
    ####
    def __init__(self, name, age):
        # trebuie sa accesam numele undeva pt a fi accesar mai tarziu
        self.name = name
        self.age = age

    def bark(self):
        print("Ham ham!")

    def sad(self):
        print("I am sad")

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age

d = Dog("Billy", 5)
print(type(d)) # returneaza <class '__main__.Dog'> este un obiect al clasei Dog
            # avem __ pt a ne arata in ce modul clasa a fost definita.
            # by default modulul pe care l-ai rulat este modulul prinicpal
            # de unde si denumirea __main__

d.bark() # utilizam o metoda pe o instanta a clasei dog

# aplicam metoda sad pe obiectul d
d.sad()
print(d.get_name())

d2 = Dog("Oreo", 12)
print(d2.get_name())
d2.set_age(2)
d.set_age(2)

# mai sus am facut un blueprint pentru clasa dog

# avem un sistem de gestiune universiar

