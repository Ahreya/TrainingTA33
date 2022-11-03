##### if statament #####

# condition not fullfieled
a = 70
b = 10
c = a * b
if c > 1000:
    print("Yay valoarea lui c este mai mare decat 1000")
print(f"c are valoarea {c}")

# condition fullfilled
if c < 1000:
    print("valoarea lui c este mai mica decat 1000")
print(f"{c}")


#### if..else statements ####

a = "mama"
b = "Mama"

if a == b:
    print("Mama si cu tata merg la restaurant")
else:
    print("Mama sta acasa")

#### if else if statements ####

a = 12
b = 3
c = 3
s = b % c

if s == 0:
    print("s is an even number")
elif s < 2:
    print("S este mai mic decat 2")
elif b > c:
    print("b este mai mare decat c")
else:
    print("s este numar impar")
print("Se continua codul")


## ex 2
fruct1 = "pere"
fruct2 = "Pere"
alt_str = "tanculete"

if fruct1 == fruct2:
    print("Facem dulceata de pere")
elif fruct1 != alt_str:
    print("Nu mai facem dulceata")
else:
    print("I don't care")
print("Ai ajuns aici")


#### nested if else statements ####

nr1 = 24
nr2 = 25
s1 = "mama"
s2 = "mama"

if nr1 > nr2:
    if s1 == s2:
        print("conditia s-a indeplinit")
    else:
        print("Nu s-a indeplinit conditia")
else:
    print("Am intrat pe else clause")

print("S-a terminat ora, seara buna!")