###### Turn this snipet into a function

print("Enter a value: ")
a = int(input())

print("Enter a value: ")
b = int(input())

print("Enter a value: ")
c = int(input())

### define the function

def get_value():
    print("Enter a value: ")


print("We start here")
get_value()
print("We end here")


##### positional parameter passing

def introduction(first_name, last_name):
    print("Hello, my name is ", first_name, last_name)


introduction("Luke", "Skywalker")
introduction("Clark", "Kent")
introduction("Jessie", "J")
introduction(first_name="James", last_name="Bond")
introduction(last_name="Skywalker", first_name="Luke")


#### functie cu parametru predefinit

def introduction_a(first_name, last_name = "Smith"):
    print("Hello, my name is", first_name, last_name)


introduction_a("Diana")

##### return fara argumente ####


def happy_new_year(wishes=True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return
    print("Happy new year")


happy_new_year()


##### functie cu un argument gresit

def introduction_b(first_name, last_name):
    print("Hello, my name is", first_name, last_name)


introduction_b("Luke")

##### return cu argumente - folosit
def boring_function():
    a = 345
    return a

x = boring_function()
print("The boring_function has returned its result. It's: ", x)


#### nu folosim ce returneaza

def boring_function_a():
    print("'Boredom Mode' ON.")
    return 123

print("This is quite interesting!")
boring_function_a()
print("This lesson is boring...")

#### invocam functie cu lista

def list_sum(my_list):
    s = 0

    for item in my_list:
        s += item
    return s

print(list_sum([10, 20, 30]))
print(list_sum(6))


##### function that returns a list #######
########## exercitiu pt tema - explica functia si insertul   ###

def my_strange_list(n):
    strange_list = []

    for i in range(0, n):
        strange_list.insert(2, i)

    return strange_list

print(my_strange_list(5))

########## functie -> valoarea absoluta a unui numar


def absolute_value(num):
    """
    This function returns the absolute value of the entered number
    :param num:
    """
    if num >=0:
        return num
    else:
        return -num


print(absolute_value(int(input("Introduceti un numar: "))))
print(absolute_value(-4))


#### functia cu un nr necunoscut de argumente

def multiple_args(*fruits):
    print(f"I really like {len(fruits)} fruits, they are: {fruits}")

multiple_args("mar", "cireasa", "banana", "piersica")


def multiple_args(**name):
    print((name["fam_name"] + " " + name["first_name"]))

def main():
    multiple_args(fam_name="Barbu",
                  first_name="Georgiana")

main()