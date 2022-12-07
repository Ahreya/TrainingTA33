class Person:
    def __init__(self, age, weight, height, first_name, last_name):
        self.age = age
        self.weight = weight
        self.height = height
        self.first_name = first_name
        self.last_name = last_name

# cream o noua persoana (o instanta a clasei Person)
# putem accesa atributele clasei si sa le folosim la persoana pe care vrem sa o cream,

user = Person(25, 65, 150, "Akihkio", "Takayama")
print(user.height) # ne arata

print(type("hello"))

# avem functia

def greetings():
    print("Hello there human!")

print(type(greetings))##### de verificat

s = 2
n = "string"
print(s + n)


## methods
mystring = "yellow there"
print(mystring.upper()) #--. metoda care actioneaza asupra unui obiect
#print(s.upper())