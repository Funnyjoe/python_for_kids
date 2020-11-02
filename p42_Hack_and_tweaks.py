def check_guess(guess, answer):
    global score
    still_guessing = True
    attemp = 0
    while still_guessing and attemp < 3:
        if guess.lower() == answer.lower():
            print("Correct answer.")
            score = score+1
            still_guessing = False
        else:
            if attemp < 2:
                guess = input('Sorry wrong answer.Try again. \n')
            attemp = attemp+1
    if attemp == 3:
        print("The correct answer is "+answer+".")


score = 0
guess = input('Which one of these is a fish? \n \
A) Whale\n B) Dolphin\n C) Shark\n D) Squid \nType A, B, C, or D \n')
check_guess(guess, 'C')
print('Your score is ' + str(score)+".")


# Use a backslash character(\) if you need to split a long line of code over two lines.
# You can use \n to make a new line anywhere.
