############ STRING METHODS #############

#### .capitalize( ) ####
# modifica stringul astfel incat prima litera va fi mare si restul literelor vor fi mici
# syntax: str.capitalize()
myStr = "casa mea este Mica"
print(myStr.capitalize())

#### .endswith() ####
# verifica daca un string se termina cu litera data ca argument
# syntax: str.endswith("something")
myStr = "casa mea este Mica"
print(myStr.endswith("ca"))


#### .find( ) ####

# cauta un substring si returneaza indexul unde se gaseste
# este safe - nu returneaza o eroare daca ii dam un substring nonexistent ca parametru, cu -1
# functioneaza numai cu stringuri - nu incercati sa o aplicati pe alte secvente

## find() with one parameter ##
# syntax: str.find("substring")
my_string = "invat python"
print(my_string.find("at"))

## find() with 2 parameters ##
# if you want to search the substring starting with a certain index
# syntax: str.find("substring", poz)
my_string = "astazi nu vreau sa invat"
print(my_string.find("zi", 2))
fructe = "mere pere caise"
print(fructe.find("er"))

## find() with 3 parameters
# al treilea argument pointeaza catre primul index care nu va fi luat in considerare in cautare
# syntax: str.find("substring", poz, poz_end_search)
nume = "Maria Ioana Angelica Ion"
print(nume.find("Angelica", 0, 20))

#### .isalnum() ####
# verifica daca un string contine numai litere si cifre. Returneaza un bool -> True / False
mother = "Cristina10"
print(mother.isalnum())


#### .isalpha() ####
# verifica daca un string este format numai din litere si returneaza True / False
# syntax: str.isalpha()
# spatiile nu sunt considerate litere, sunt considerate caractere
my_string = "Am ani"
print(my_string.isalpha())


#### .isdigit() ####
# verifica daca un string este format numai din numere
# syntax: str.isdigit()
varsta = "28"
print(varsta.isdigit())


#### .islower() ####
# verifica daca un string este format numai din litere mici si returneaza True / False
# syntax: str.islower()
litera_mica = "am plEcat in vacanta"
print(litera_mica.islower())

#### .isspace() ####
# verifica daca stringul este format numai din spatii goale si returneaza True / False
# syntax: str.isspace()
spatiu = "am plecat"
spatiu2 = "   "
print(spatiu.isspace())
print(spatiu2.isspace())


#### .isupper() ####
# verifica daca un string este format numai din litere mari si returneaza True / False
# syntax: str.isupper()


#### .lower() ####
# face o copie a stringului original si inlocuieste toate literele mari din string cu litere mici si returneaza noul string ca rezultat
# the original string remains untouched.
# syntax: str.lower()


#### .upper() ####
# face o copie a stringului original si inlocuieste toate literele mici din string cu litere mari si returneaza noul string ca rezultat
# the original string remains untouched.
# syntax: str.upper()


#### replace() ####
# retruneaza o copie a stringului original in care toate aparitiile primului argument au fost inlocuite cu al doilea argument
# syntax: str.replace(arg1, arg2)

my_str = "cainele ma musca"
print(my_str.replace("cainele", "pisica"))

## exercitiu: ce returneaza urmatorul cod

s = 'It is either easy or impossible'
s = s.replace('easy', 'hard').replace('im', '')
print(s)
#Answer:


#### split() ####
# aceasta metoda considera ca stringurile sunt delimitate de spatii albe
# syntax str.split()
# example: print("phi       chi\npsi".split()) -> ['phi', 'chi', 'psi']
ex = "bujori flori trandafiri"
print(ex.split())


#### strip() ####
# returneaza un nou string fara spatii albe
# syntax: str.strip()


## exercitiu: ce returneaza urmatorul cod?

s1 = 'Where are the snows of yesteryear?'
s2 = s1.split()
print(s2)
print(s2[-2])
#Answer: of

##ex 2
a = "Tomorrow I will leave my home"
b = a.split()
print(b)
print(b[-4])

#### swapcase() ####
# returneaza un nou string in care tipul de litere este inversat. litere mici -> litere mari , viceversa

s = "i WaS a BaD CaT"
print(s.swapcase())

