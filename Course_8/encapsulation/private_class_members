##### Private members #####
# __(dubllu underscore) este prefixul pentru variabile private
# nu trebuie foloiste in afara clasei.

class Car:

    def __init__(self, wheel, speed, color):  # definim constructorul
        self.__wheel = wheel  # private class atribute
        self.__speed = speed  # private class atribute
        self.__color = color  # private class atribute

    def __print_me(self):
        print("I am a private method")


renault = Car("right", 180, "green")
# print(renault.__color)
# Orice incercare de a folosi atributul in afara clasei va rezulta intr-o eroare --> AttributeError
# print(renault.__print())

# python face o modificare a variabilelor private.
# Fiecare membru cu __ o sa fie schimbat in _object.class_variable --> poate fi accesat in afara clasei
# DAR NU TREBUIE SA FACEM ASTA
# print(dir(renault))

# Cum se acceseaza - REFRAIN FROM DOING SO
print(renault._Car__speed)
renault._Car__speed = 500
print(renault._Car__speed)

### Python nu are  un mecanism care sa restrictioneze accessul pe metode sau variabile
# Pur si simplu exista conventia de a folosi _ si __ care sa simuleze comportamentul de protected si private
# Ramane la latitudinea dezvoltatorului sa inteleaga acest lucru.
