import time
###### loops #####

### while ###

# an endless loop
# while True:
#     print("I am stuck in a loop")
# else:
#     print("something")
# exercitiu

# write a program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd
# The program terminates when zero is entered

# What we need?
# var - odd numbers
# var - even numbers
# input()

# we declare 2 vars for odd number and even numbers and we set it to 0
odd_numbers = 0
even_numbers = 0

#read the number first
# number = int(input("Enter a number or type 0 to stop: "))
#
# # 0 terminates the execution
# while number != 0:
#     # Check if the number is odd
#     if number % 2 == 1:
#         # Increase the odd_numbers counter
#         odd_numbers += 1
#     else:
#         # increse the even_numbers counter
#         even_numbers += 1
#     number = int(input("Enter a number or type 0 to stop: "))
#
# print("Too bad, user entered 0")
# print("Odd numbers count: ", odd_numbers)
# print("Even numbers count: ", even_numbers)


### exercitiul 2
# make a counter that counts the last 10 seconds until new year
# after the last second print "Happy new year"

# avem nevoie de o variabila counter

# counter = 10
# while counter:
#     print(counter, "seconds left")
#     #se scade o secunda
#     counter -=1
#     time.sleep(1)
# print("Happy new year!!!!!!!!", counter)

############## for #####

###exercitiul 1

# write a for loop that counts to five.
# body of the loop - print the loop iteration number and the word "Mississippi"
# use time.sleep1(1)
# write a print function with the final message

# for second in range(1, 6):
#     print(second, "Mississippi")
#     time.sleep(1)
# print("I will search you and I'll find you!")


#### exercitiul 2

# Define a new list with 7 elements.
# We want to calculate the sum of all the numbers inside the list

#We need: o lista, variabile sum.

# my_list = [5, 7, 1, 3, 10, 20, 30]
# sum = 0 # we start with a counter that we initialize with 0 (we haven't added any number yet)
#
# for i in my_list:
#     print(f"Adding {i} to {sum}")
#     sum += i #as long as we haven't reached the end of the list we will
#             # add the current element to the previous total
#     print(f"Current sum is {sum}")
# else:
#     print("We are done with the sum")
# print(f"The sum of the elements in the list is : {sum}")

######## break ########

# print("The break instruction: ")
# for i in range(1, 6):
#     if i == 3:
#         break
#     print("Inside the loop.", i)
# print("Outside the loop")
#
# ###### continue #######
#
# print("The continue instruction")
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print("Inside the loop.", i)
# print("Outside the loop")


########for each ########

# avem o lista cu 6 animale
# # parcurgem lista cu cele 6 animale si printam "I love this animal"
#
# animals = ["zebra","tigru","maimuta", "iepure", "dinozaur", "pantera", "tapir"]
#
# for animal in animals:
#     print(f"I love this animal --> {animal}")

######## exercices ########

# a junior magician has picked a secret number
# he has hiddent it in avariable named secret_number
#he want everyone to run his program to play Guess the secret number
#if the user doesn't guess the number he will be stuck in the loop
# if he guessed the number, then magician will let him out

secret_number = 200

print ("====Welcome to my game human!====")

user_nr = int(input("Enter a number: "))

while user_nr != secret_number:
    print("You are stuck in my loop, ha ha ha!")
    user_nr = int(input("Enter the number again: "))
print(secret_number, "Well done human! You are free now!")
