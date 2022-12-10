import random
# game with dictionary
# quizz with european capitals

# de ce avem nevoie?:
# - dictionar cu tari si  capitale
# random choice- ca sa selecteze o tara din dictionar
# input de la user
# variabia in care stocam inputul de la user
# functie care face verificarea
# counter care ii spune cate raspunsuri corecte are din nr total

def get_europe_capitals():
    europe_capitals = {
        "Romania": "Bucharest",
        "Spain": "Madrid",
        "Turkey": "Ankara",
        "Russia": "Moscow",
        "Bulgary": "Sofia",
        "Hungary": "Budaphest",
        "Germany": "Berlin",
        "Belgium": "Brixelles"
    }
    return europe_capitals

def main():
    europeCapitals = get_europe_capitals()
    print("Welcome! Input the correct capital for each country!")
    correct_answers = 0

    while len(europeCapitals) != 0:
        # get a random country
        country = random.choice(tuple(europeCapitals.keys()))
        capital = europeCapitals[country]

        # remove from dictionary the selected country
        del europeCapitals[country]

        # get answer from user
        answer = input(f"What is the capital of {country}?: ")

        # verificam raspunsul utilizatorului
        if answer == capital:
            correct_answers += 1
            if len(europeCapitals) != 1:
                print("That's correct! Good luck with the next one!")
            else:
                print("That's correct")
        else:
            print("Incorrect")
            continue
    print(f"GAME OVER!! {correct_answers} correct answers from 8")

main()
