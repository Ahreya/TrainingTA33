#-------Hello World si comentarii ---------
# aceasta functie afiseaza hello world
print("Hello World")

print("Acesta este un curs de python")
print('Acesta este un curs de python')

#comentarii
"""
acesta este
un comentariu
pe mai multe linii
"""

# acesta este
# un comentariu
# pe mai multe linii

#TIPS: Pentru a comenta sau a scoate comentariile de pe o portiune mai mare de cod, selectati bucata de cod ce o vreti comentata si
#apasati CTRL + / (pentru Windows) SAU CMD + / (pentru Mac OS)


#---------variabile si tipuri de date -----------

a = 5  # aceasta este o variabila de tip int
b = 24 # aceasta este o variabila de tip int
c = "mama"  # aceasta este o variabila de tip string
d = 1.25  # aceasta este o variabila de tip float
imiPlacePython = True # aceasta este o variabila de tip bool
vreau_sa_muncesc_mult = False #aceasta este o variabila de tip bool

#ii atribuim lui a valoarea lui b
a = b

print(f"Valoarea lui a este {a}")

b = d # ii atribui lui b valoarea lui d
a = b = c # ii atribuim lui a valoarea lui b si apoi lui c. Valoarea finala a variabilei a va fi valoarea lui c.

print("Valoarea finala a lui a este: ")
print(a)
print(c) #valoarea lui c ramane aceeasi


# ------- Functia type() ------------
mama = "Maria" # string
tata = "Ionel" # string
varsta = 49 # int
salariu = 15500 #int
eficienta = 8.5 #float
suntAcasa = True #bool


print(type(mama)) # afisam tipul variabilei mama
print(type(tata)) # afisam tipul variabilei tata
print("Tipul variabilei varsta este: ")
print(type(varsta)) # afisam tipul variabilei varsta
print("Tipul variabilei salariu este: ")
print(type(salariu)) # # afisam tipul variabilei salariu
print("Tipul variabilei suntAcasa este: ")
print(type(suntAcasa)) # # afisam tipul variabilei suntAcasa
print("Tipul variabilei eficienta este: ")
print(type(eficienta)) # afisam tipul variabilei eficienta

# ------Functia type() si casting

varsta = 29 # variabila tip int
print("Tipul variabilei varsta este: ")
print(type(varsta)) # afisam tipul variabilei varsta
print("Acum variabila varsta este de tip: ")
print(type(str(varsta))) # afisam tipul variabilei varsta care este convertit in string
print(type(float(varsta))) # # afisam tipul variabilei varsta care este convertit in float

# -----------Concatenarea ---------------
##### OBS! Nu se pot concatena stringuri cu alte tipuri de variabile (exemplu: string + int )

# exemplul 1
fructe = "mere, pere si portocale " # var tip string
shopping = "Eu am cumparat astazi " # var tip string
pret = 25 # var tip int

str_concat = shopping + fructe # str_concat este o variabila care va contine variabila shopping concatenata cu var fructe
print(str_concat) # printam valoarea variabilei str_concat

pret = str(pret) # convertim variabila pret care era de tip int, in tip string
str2_concat = fructe + pret # concatenam var fructe cu var pret care este acum de tip string, deci string cu string
print(str2_concat) # afisam valoarea variabilei str2_concat

#exemplu 2
# avem urmatoarele variabile:
actiune = "Am cumparat " #string
obiect = "un dulap la " #string
pret = 100 # int

#Vrem sa concatenam toate stringurile intr-o singura variabila so sa obtinem:
# Am cumparat un dulap la 100 lei

#in urmatorul cod vom primi eroare
fraza = actiune + obiect + pret # incercam sa concatenam 2 stringuri cu int
print(fraza) # afisam valoarea variabilei fraza
# la rularea acestui cod vom primi urmatoarea eroare:
#TypeError: can only concatenate str (not "int") to str

# ca sa nu primim eroare, mai intai trebuie sa convertim variabila pret in string, astfel incat sa avem doar stringuri
fraza = actiune + obiect + str(pret) # concatenam cele 2 stringuri cu variabila pret care este convertita in string
print(fraza)

# exemplul 3

#concatenam mai multe stringuri in print, printre care si " " care inseamna spatiu
print("Astazi am mancat" + " " + "multe mere" + " " + "si nu ma simt bine")
#acest print va afisa "Astazi am mancat multe mere si nu ma simt bine"


# --------- Functia print()  -  formatare ------------------

# in print folosim litera f sau F inainte de a deschide ghilimele, iar unde vrem sa se afiseze valoarea variabilei
# vom pune {variabila}. printul va avea aceasta forma: print(f"ceva ceva {variabila} ceva")

#avem urmatoarele variabile
fructe = "struguri, banane, capsuni" # string
shopping2 = "Eu am luat din supermarket" # string
pret = 35 #int

#Vrem sa afisam Eu am luat din supermarket struguri banane capsuni la pretul de 35 de lei
print(f"{shopping2}:{fructe} la pretul de {pret} de lei")


## exercitiul 2
data = "25/10/2022" # string
ora = "19:53" # string

# Eu astazi la data de 25/10/2022 am inceput primul curs de python, iar la ora 19:53 am pus prima intrebare
print(f"Eu astazi la data de {data} am inceput primul curs de python, iar la ora {ora} am pus prima intrebare")

## exercitiul 3

#Astazi fratele meu Mihai a inscris 2 goluri
frate = "Mihai"
nr_goluri = 2

print(f"Astazi fratele meu {frate} a inscris {nr_goluri} goluri")

# ------------ assertion ------------------
# syntaxa: assert expression, assertion message

# avem urmatoarea variabila de tip int
varsta = 29

# comparam valoarea variabilei varsta cu 30, daca valoarea nu este 30, atunci se afiseaza mesajul de eroare, iar codul nu curge mai
# departe
assert varsta == 30, f"Ma astept sa am 30 de ani, dar se pare ca varsta mea este de, {varsta}"
a = 2
b = 5
print(a+b)

# inlocuieste acum varsta = 29, cu varsta = 30. codul va curge mai departe si se va executa printul cu a + b


####ex 2

nr_placinte = 3
# Trebuia sa mananc 3 placinte, dar se pare ca am mancat x placinte
assert nr_placinte == 3, f"Trebuia sa mananca 3 placinte, dar se pare ca am mancat {nr_placinte}"
print("Am trecut testul")

#### ex 3
mama = "Maria"

assert mama == "Maria", f"Pe mama mea o cheama Maria, dar se pare ca s-a incurcat si acum e {mama}"
print("Am gasit-o pe mama!")

# ------------Functia input() ----------------

# functia input cere utilizatorului sa introduca ceva de la tastatura
# ## OBS!! orice valoare ar introduce utilizatorul de la tastatura, aceasta va fi mereu de tip string

## ex 1:
# utilizatorul va introduce de la tastatura un numar intreg care se va salva in variabila utilizator_input
utilizator_input = input("Introduceti de la tastatura un numar intreg")
print(utilizator_input) # afisam valoarea care s-a stocat in utilizator_input

## ex 2:
# utilizatorul va introduce de la tastura un numar intreg pe care il vom aduna cu valoarea variabilei b
# din moment ce orice va introduce utilizatorul este de tip string, valoarea trebuie convertita in int pt a o putea aduna
# la val lui b
# Avem 2 variante:

# varianta 1
b = 73 # int
# stocam in variabila a inputul de la utilizator
# convertim inputul de la utilizator in int inainte de a-l asigna variabilei a
a = int(input("Te rog sa introduci un numar intreg: "))
print(type(a)) # tipul va fi int
c = b+a
print(f"valoarea variabilei {c} este: ")

# varianta 2
b = 73 # int
# stocam in variabila a inputul de la utilizator fix asa cum vine el
a = input("Te rog sa introduci un numar intreg: ")
print(type(a)) # tipul va fi string
#cand cream variabila c si ii asignam cele 2 valori adunate ale lui a si b, convertim var a in int
c = b+int(a)
print(f"valoarea variabilei {c} este: ")


#### ----- functii string ------------

###  functia len() - afiseaza numarul de caractere dintr-un string
# syntaxa: len(variabila)
c = "Vreau acasa" # string
lungime = len(c) # am creat variabila lungime in care stocam outputul functiei len(c), adica numarul de caractere din stringul
                # "vreau acasa"
print(f"Lungimea stringului c este: {lungime}")
# daca nu vrem sa folosim variabila lungime putem printa astfel:
print(len(c))


### index
# indexul reprezinta pozitia pe care se afla un caracter
# numerotarea incepe de la 0
# exemplu
# p e r e
# 0 1 2 3
myString = "ciuperca" # variabila myString de tip string
poz = myString[4] # avem variabila poz careia ii asignam litera care se afla de pe pozitia 4
print(f"Pe pozitia 4 este litera {poz}")
# c i u p e r c a
# 0 1 2 3 4 5 6 7
# deci caracterul de pe pozitia 4 este e
# daca voiam sa aflam care este prima litera, am fi avut myString[0]

#### slicing
# prin slicing obtinem portiuni (felii) din stringuri
# syntaxa my_str[start:end:step]
# start - integer care specifica punctul de plecare. Optional
# stop - integer care specifica punctul de oprire
# step - este default 1, e optional

#exemplu:
myString = "cosmonaut"

# vrem sa obtinem cuvantul cosmo
new_string = myString[:5] # feliem incepand cu caracterul de pe pozitia 0 (c) pana la pozitia 5 (n)
# ATENTIE: punctul de oprire nu se ia in seama. pe pozitia 5 avem litera n, dar practic el s-a oprit la o
print(new_string) # va afisa cosmo

# vrem sa afisam naut
# varianta 1
new_string2 = myString[5:] # incepand cu caracterul 5 n, pana la final
print(new_string2)

# varianta 2
# specificam si punctul de inceput si punctul de sfarsit
# atentie, desi pozitia 9 nu exista, vom merge pana la 9 ca sa se ia in calcul ultimul caracter (pozitia 8)
new_string2 = myString[5:9]
print(new_string2)

#### cum parcurgem un string in sens invers cu slice?
# syntaxa: my_str[::-1] adica parcurgem tot stringul de la coada la cap (pas = -1)
my_var = "viteza"
print(my_var[::-1]) # ne va afisa azetiv


########## alte functii string ########   O B S - le vom discuta la urmatorul curs

# myStr.upper() - converteste tot stringul in litere mari
myStr = "ana"
print(myStr.upper())  # va afisa ANA
# myStr.isupper() - returneaza True sau False. Verifica daca stringul e scris cu caractere mari
print(myStr.isupper())

#### puteti verifica mai multe functii daca scrieti myStr.  vi se va da o lista cu sugestii
# din care puteti sa alegeti ce functie vreti










