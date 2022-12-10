###### Polymorphism ####

### cream clase cu limbi straine

class Japanese:
    # avem o functie care saluta in japoneza
    def say_hello(self):
        print("Konnichi wa")


class Chinese:
    def say_hello(self):
        print("Ni hao")


class French:
    def say_hello(self):
        print("Bonjour")


def greetings(language):
   language.say_hello()


# cream o instanta a clasei Japanese
Takumi = Japanese()

# cream o instanta a clasei Chinese
Lee = Chinese()

# cream o instanta a clasei French
Paul = French()

greetings(Takumi)
greetings(Lee)
greetings(Paul)

