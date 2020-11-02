import random
import string


adjectives = ['sleepy', 'slow', 'smelly', 'wet', 'fat', 'red', 'orange',
              'blue', 'black', 'white', 'purple', 'fluffy', 'proud', 'brave']
nouns = ['apple', 'dinosaur', 'ball', 'toaster', 'goat', 'dragon',
         'hammer', 'duck', 'panda']

print('Welcome to Password Picker!')
adjective = random.choice(adjectives)
noun = random.choice(nouns)
number = random.randrange(0, 100)
special_char = random.choice(string.punctuation)
password = adjective+noun+str(number)+special_char
print('Your new password is: %s ' % password)
