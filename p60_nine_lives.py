import random


def update_clue(guessed_letter, secret_word, clue, unkown_letters):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
            unkown_letters = unkown_letters-1
        index = index+1
    return unkown_letters


lives = 9
words = ['pizza', 'fairy', 'teeth', 'shirt', 'otter',
         'plane', 'plane', 'brush', 'horse', 'light']
secret_word = random.choice(words)
unkown_letters = len(secret_word)
#clue = list('?????')
clue = []
index = 0
while index < len(secret_word):
    clue.append('?')
    index = index+1

heart_symbol = u'\u2764'
guessed_word_correctly = False

difficulty = input(
    'Choose difficulty (type 1, 2 or 3):\n 1 Easy\n 2 Normal\n 3 Hard\n')
difficulty = int(difficulty)
if difficulty == 1:
    lives = 12
elif difficulty == 2:
    lives = 9
else:
    lives = 6

while lives > 0:
    print(clue)
    print('Lives left:' + heart_symbol*lives)
    guess = input('Guess a letter or the whole word:\n')
    if guess == secret_word:
        guessed_word_correctly = True
        break
    if guess in secret_word:
        unkown_letters = update_clue(guess, secret_word, clue, unkown_letters)
    else:
        print('Incorrect.You lose a life.')
        lives = lives-1
    if unkown_letters == 0:
        guessed_word_correctly = True
        break
        # The game ends when you guess the last letter.


if guessed_word_correctly:
    print('You won! The secret word was '+secret_word+'.')
else:
    print('You lost! The secret word was '+secret_word+'.')
