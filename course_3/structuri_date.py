############ liste ###########
#syntax: list_name = [elem1, elem2, elem 3]
 
# lista goala
myList = []
print(myList)

#lista cu elemente mixte

myList1 = ["mama", 13, True, 13.5, True, False, "miau"]

# elementul de pe pozitia 2
print(myList1[2])

# de cate ori apare True in myList1
print(myList1.count(True))
myList1[2] = "corect"
print(myList1)

# extindem o lista
ls1 = [1,2,3,4]
ls2 = ["tata", "mama", "max"]
ls1.extend(ls2)
print(ls1)

# adaugam un element cu append() la lista 
ls3 = [1,2,3,4]
ls4 = ["tata", "mama", "max"]
ls3.append(ls4)
print(ls3)
print(len(ls3))
print(len(ls1))

######### tuple ##########

# cream o tupla cu string
myTuple = ("mama", "unu", "portocala")

# afisam elem de pe pozitia 0
print(myTuple[0])

# verificam daca elementul "unu" este in tupla - returneaza True sau False
print("unu" in myTuple)

### exercitii

# avem o lista. sa se afle elemntul de pe pozitia 1.
# sa se inlocuiasca elemntul de pe pozitia 1 cu "bingo"
# daca valoarea veche a elementului de pe pozitia 1 este in lista, atunci vom afisa "I am here"

lt = [12, 5, "tata", True, False, "gaina"]
poz1 = lt[1]
lt[1] = "bingo"
if poz1 in lt:
    print("I am here")
    

###### seturi ########

# definim un set
ms = {"iarna", "toamna", "primavara", "vara"}

# printam lungimea setului
print(len(ms))

# adaugam cu add() elemente in lista
ms.add("frig")
ms.add("cald")
ms.add("rece")
ms.add("fierbinte")
print(ms)

# adaugam o tupla la set
ms.add((1,2, False))
print(ms)
# definim o tupla
tp = ("n", 2, 5)
ms.add(tp)
print(ms)

# remove element from set
ms.remove("frig")
print(ms)
ms.discard("fierbinte")
print(ms)

# remove an element that doesn't exists that doesn't exist
# renove - returnes an error, discard ignores it.
ms.remove("ciorap")
ms.discard("ciorap")



######## dictionare ##########

dict1 = {"a": 2, "b":3, "c":4}

# afisam valoarea lui b
print(dict1["b"])

dt = {"tip_carte": "roman", "editura": "Corint",
      "Autor": "Agatha Christie", "nr_pag": 250,
      "carti": ["Cu cartile pe fata", "Oglinda", "Crima in Orient Expres"]}

# din cheia carti vrem sa obtinem cartea 2
cartea2 = dt["carti"][1]
print(cartea2)


# daca numele cartii 2 este "Cianura" atunci afisam "Nu am citit", altfel
# "Am citit"
if cartea2 == "Cianura":
    print("Nu am citit")
else:
    print("Am citit")

# sa se numere caracterele valorii cheii 2. Daca lungimea este mai mare
# decat 7 si primul caracter este litera mica, sa se afiseze "Great"

# aflam valoarea cheii editura
val = dt["editura"]
print(val)
lungime = len(val)
print(len(val))
val1 = val[0]
if lungime > 7 and val1.islower():
    print("Great")
else:
    print("first letter is not lower")

tpl1 = (1, 6, 8)
print(list(tpl1))

print(tuple(tpl1))
print(set(tpl1))

tuple()
set()
list()


