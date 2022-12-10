## conventii
# verificam daca o variabila este None sau nu, cu is None, is not None. nu folosim ==
#
# a = None
# if a is None:
#     print("something")
#
# if a is not None:
#     print("something")
#
# ### cum se face unpacking ###
# # vrem sa facem unpack la o colectie si sa asignam fiecare valoare unei variabile
#
# tup = (10, 12, 1, 5, 0)
# a, b, c, d, e = tup
# print(a, b, c, d, e)
#
# my_dict = {"name": "Madalina", "age": 29, "language": "romanian"}
# val_a, val_b, val_c = my_dict.values()
# print(f"val_a este {val_a}, val_b este {val_b}, val_c este {val_c}")
# s, n, x = my_dict
# print(s,n,x)
#
# # vrem sa obtinem si cheile si valorile. obtinem tuple
# g, f, j = my_dict.items()
# print(g, f, j)
#
# #### multiple assignement --> switch ####
# a, b = 10, 100
# a, b = b, a
# print(a, b)

##### ternar condition (inline) ####

# if 2*5 > 1*3:
#     d = 10
# else:
#     d = 0

# folosim conditie ternara
# d = 10 if 2*5 > 1*3 else 0
# asigneaza lui d valorea 10
# conditie
# daca nu, asigneaza-i 0

#### zip function - combina colectii de date impreuna ca sa putem itera prin toate odata

fruits = ["mango", "strawberry", "apple", "watermelon"]
kilos = [1, 3, 1, 10]
color = ["orange", "red", "yellow", "green"]

# print(list(zip(fruits, kilos, color)))

# for fruits, kilos, color in zip(fruits, kilos, color):
#     if color == "green":
#         print(fruits)
#     print(kilos)

####### *args, **kwargs #####
# *args = positional arguments -> este un argument in care pozitia conteaza
# **kwargs = keywords arguments -> putem apela o functie cu ce poz vrem, atata timp cat le trecem

# positional
#
# def my_function(ar1, ar2, ar3):
#     print(ar1, ar2, ar3)
#
# def my_function1(ar1=None, ar2=None, ar3=None):
#     print(ar1, ar2, ar3)

#### dac ca argumente unei functii liste si dictionare
# args = [2, 5, 7]
# kwargs = {"ar1": 2, "ar2": 3, "ar3": 4}
#
# my_function(*args)
#
# # cu dictionare
# my_function1(**kwargs)

###### sort by key #########

# l = [[1, 2], [10, 1], [13, 2], [0, 6]]

# folosim functia sort() care o sa sorteze dupa primul elemnt din fiecare nested list
# l.sort()
# print(l)


# l.sort(reverse=True)
# print(l)

# vrem sa sortam dupa al doilea element

# l.sort(key=lambda x: x[1]) # x este parametrul pt functie si returnam x[1] adica al doilea element din fiecare nested list
# print(l)

# vrem sa ssortam dupa suma elementelor din fiecare nested list
# l.sort(key=lambda x: x[0] + x[1])
# print(l)
#
# def sort_func(x):
#     return x[0] + x[1]
#
# l.sort(key=sort_func())
# print(l)

# create a function that takes a variable number of arguments

# def multiply(x, y):
#     return x * y

# print(multiply(2, 5))

# multiply(2, 5, 10, 12) - too many arguments, error returned

def multiply(*numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

print(multiply(2, 5, 12, 30, 100, 1, 3, 15))

### we want a function that saves information


def save_info(**info_user): ## folosim keyword arguments
    for key, value in info_user.items():
        print(key, value)


save_info(name="Luther", age=50, e_mail="luther.king@gmail.com")


