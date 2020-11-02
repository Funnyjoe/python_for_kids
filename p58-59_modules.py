import webbrowser  # First way to use modules
from random import choice  # Second way to use modules
from time import time as time_now  # Third way to use modules
# webbrowser.open('https://youtube.com')
direction = choice(['N', 'S', 'E', 'W'])
print(direction)
now = time_now()
print(now)
