############ OPERATORI ARITMETICI ###############


# Addition
a = 5
b = 275
c = 1985

print(a+b+c)

# Substraction

print(c - a + b)

# Multiplication
print(a * b)

# Division
a = 20
b = 10
print(a/b)

# Modulus
a = 5
b = 2
print(a%b)

# Exponentiation
a = 2
b = 3
print(a**b)

############ OPERATORI DE ATRIBUIRE #############

# " = "

a = 5
b = 888

# " += "
a = 6
a += 5 # a = a + 5 => a = 6 + 5
print(a)


# " -= "
b = 110
b -= 10 # => b = 110 - 10
print(b)

# " *= "
c = 3
c *= 2 # =>c = 3 * 2
print(c)

# " /= "
d = 22
d /= 11 # d = 22 /11
print(d)

d = 11
d /= 7
print(round(d))


############ OPERATORI LOGICI #############

# "and"
# returns TRUE if both statements are true
a = 0
b = 1
print(a and b)

# "or"
# returns true if one of the statements is true
c = 0
d = 0
print(c or d)

# "not"
e = 1
b = 6
print(not(b<e))
n = 10
s = 12
x = 2
print(not(n*2 < s and s < 15)) # => not( 20 < 12  and 12 < 15) => not( False and True ) => not (False) => True


############ OPERATORI DE COMPARARE #############
# string comparison is always case-sensitive --> upper-case letters are taken as lesser than lower-case letters.
# OBS! - nu comparam 2 tipuri diferite de date cu comparatorii <, > <=, >=, primim eroare "TypeError "


# " == "
a = 12
c = 10
print(a==c)


# " != "
print(a!=c)

# " > "
print(a > c)

# " < "
a = 12
c = 10
print(a < c)

# " >= "
s = 199
n = 200
print(n>=s)

# " <= "
print(n<=s)