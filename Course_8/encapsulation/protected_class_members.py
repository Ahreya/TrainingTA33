######## Protected members ##########
# protected members - sunt accesibili in interiorul clasei cat si in subclase. Nu pot fi accesati din oriuce alta parte
# instance variable protected --> _var_name (single underscore). Folosind underscore, previne sa fie accesat, mai putin daca
#e accesat dintr-o subclasa

# Transformam clasa Car

class Car:

    def __init__(self, wheel, speed, color):  # definim constructorul
        self._wheel = wheel  # protected class atribute
        self._speed = speed  # protected class atribute
        self._color = color  # protected class atribute

    def get_speed(self):
        return self._speed

    def get_color(self):
        return self._color

    def get_wheel(self):
        return self._wheel

    # set a new color
    def set_color(self, value):
        self._color = value

    def set_speed(self, value):
        self._speed = value

# daca scrie in felul asta, nu previne variabilele instantei sa acceseze sau sa modifice instanta


peugeot = Car("right", 240, "white")  # nu ne da eroare cand scriem valorile
# print("peugeot color: ", peugeot.color)
print("peugeot color:", peugeot._color)

# Daca vrem sa modificam culoarea
peugeot.color = "black" # nu schimba culoarea
peugeot._color = "black"
print(peugeot._color)

# Daca o variabila jeste scrisa cu underscore(este protected), programatorul se va ABTINE sa o modifice in afara clasei

# setam culoarea apeland metoda de setare a culorii
peugeot.set_color("Black")
print(peugeot.get_color())
