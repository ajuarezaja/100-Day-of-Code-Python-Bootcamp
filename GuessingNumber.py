import random
from art import logo

print(logo)
print('Welcome to the Guessing Number Game!')
print("I'm guessing a number between 1 and 100.")
lives = 0


def number_think():
    number_chosen = random.randint(1, 101)
    return number_chosen


def difficulty_set():
    level = input("Chose a difficulty/. Type 'easy' or 'hard': ")
    global lives
    if level == 'easy':
        lives = 10
    elif level == 'hard':
        lives = 5


def guessing_number():
    number_guessing = int(input('Make a guess: '))
    return number_guessing


def check_number_match(guess, think):
    global lives
    if guess == think:
        print(f'You win, number guessed: {think}')
        return True
    elif guess > think:
        print('Too high')
        print('Guess again')
        lives -= 1
        return False
    elif guess < think:
        print('Too low')
        print('Guess again')
        lives -= 1
        return False


def main():
    control = False
    number_to_guess = number_think()
    difficulty_set()
    while not control:
