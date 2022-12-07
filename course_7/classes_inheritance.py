# Mostenirea
# mostenirea se foloseste cand avem 2 sau mai multe clase similare

# cream clasele Cat and Dog

# cream o clasa generala numita Pets

# clasa parinte
class Pets:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what sounds I make")

#clasa copil
class Cat(Pets):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    # def speak(self):
    #     print("Meeeeow")

# clasa copil
class Dog(Pets):
    def __init__(self, name, age, race):
        super().__init__(name, age)
        self.race = race

    def speak(self):
        print("Bark")

# class child Fox mosteneste class parinte Pets
class Fox(Pets):
    pass


fox = Fox("Snow", 1)
fox.speak()

# create an object that belongs to Cat class
cat = Cat("Billy",3, "blue")

# create an object that belongs to Dog class
dog = Dog("Black", 5, "Shnautzer")
#
# cat.speak()
# dog.speak()

pet = Pets("Mike", 19) # cream o instanta a clasei Pet
pet.speak()
cat.speak()

