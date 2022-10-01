import random

'''

Use a dict to keep country-capital pairs as key-value.
prompt the user 3 times for a capital in a country.
print the number of correct capitals.
Print whether answer correct, and what it is.


dict[key] returns the corresponding value

'''

capitals = {'France': 'Paris',
        'Finland': 'Helsinki',
        'Sweden': 'Stockholm',
        'Denmark': 'Copenhagen',
        'Germany': 'Berlin'
        }

score = 0

def guessing_game(score):
    for _ in range(3):
        country = random.choice(list(capitals.keys()))
        guesses = input(f"Please give me the capital of {country}: ")
        if guesses.lower() == capitals[country].lower():
            score += 1
            print(f"Success! Your score is {score}")
        else:
            print(f"Wrong! The correct answer would have been {capitals[country]}")
    print(f"Game is over, your final score is {score} - Thanks for playing!")

if __name__ == '__main__':
    guessing_game(score)
