import turtle
import random

def drawMan(x):
    guess = x
    if guess == 1: 
        # draw head
        turtle.goto(-74, 140)
        turtle.pendown()
        turtle.right(90)
        turtle.circle(15,None,100)
        turtle.penup()
    elif guess == 2:
        # draw torso
        turtle.goto(-74, 140)
        turtle.pendown()
        turtle.left(90)
        turtle.penup()
        turtle.forward(30)
        turtle.pendown()
        turtle.forward(40)
        turtle.right(180)
        turtle.forward(30)
        turtle.penup()
    elif guess == 3:
        # draw first arm
        turtle.goto(-74, 100)
        turtle.pendown()
        turtle.left(55)
        turtle.forward(45)
        turtle.right(180)
        turtle.forward(45)
        turtle.penup()
    elif guess == 4:
        # draw second arm
        turtle.goto(-74, 100)
        turtle.pendown()
        turtle.left(70)
        turtle.forward(45)
        turtle.right(180)
        turtle.forward(45)
        turtle.penup()
    elif guess == 5:
        # draw first leg
        turtle.goto(-74, 100)
        turtle.pendown()
        turtle.left(55)
        turtle.forward(30)
        turtle.right(30)
        turtle.forward(60)
        turtle.right(180)
        turtle.forward(60)
        turtle.penup()
    elif guess == 6:
        # draw second leg
        turtle.goto(-74, 70)
        turtle.pendown()
        turtle.right(120)
        turtle.forward(60)
        turtle.penup()

# initialize turtle
turtle.hideturtle()
turtle.speed(0)
turtle.pensize(2)

# Categories with words and hints
categories = {
    'Movies': {
        'exodus': 'A biblical epic about the journey of the Israelites from Egypt.',
        'galaxy': 'Refers to a sci-fi series involving space adventures, like *Guardians of the Galaxy*.',
        'zombie': 'Refers to the undead creatures in horror films like *Night of the Living Dead*.',
        'whiskey': 'Could refer to a movie like *Whiskey Tango Foxtrot* or films about alcohol.',
        'duplex': 'A term from a comedy film about a couple facing housing challenges.',
        'quiz': 'A movie about a competitive trivia show, like *Slumdog Millionaire*.',
    },
    'Songs': {
        'bagpipes': 'Associated with traditional Scottish music or songs featuring bagpipes.',
        'polka': 'A lively Eastern European dance music style, seen in folk music.',
        'banjo': 'An instrument used in folk and country music, notably in *Dueling Banjos*.',
        'buffalo': 'Used in folk or country songs, such as *Buffalo Gals*.',
        'rhubarb': 'A quirky or playful song could feature this word in its lyrics.',
        'affix': 'A term used in experimental or avant-garde music.',
    }
}

bored = False
while not bored:
    # Ask user to choose a category
    category_choice = turtle.textinput("Hangman", "Choose a category:\nEnter '1' for Movies, '2' for Songs:")
    
    if category_choice == '1':
        wordbank = list(categories['Movies'].keys())
        hints = categories['Movies']
    elif category_choice == '2':
        wordbank = list(categories['Songs'].keys())
        hints = categories['Songs']
    else:
        wordbank = list(categories['Songs'].keys())  # Default to songs if invalid input
        hints = categories['Songs']

    # draw gallows
    turtle.home()
    turtle.pendown()
    turtle.left(90)
    turtle.forward(175)
    turtle.left(90)
    turtle.forward(74)
    turtle.left(90)
    turtle.forward(35)
    turtle.penup()
    turtle.goto(-135, -35)
    
    word = random.choice(wordbank)

    # Display hint with smaller font size
    turtle.goto(-135, -80)
    turtle.write(f"Hint: {hints[word]}", True, font=("Courier", 12, "normal"))

    for i in word:
        turtle.write('_ ', True, font=("Courier", 12, "normal"))

    correct = []
    wrong = 0
    incorrect_guesses = []  # List to keep track of incorrect guesses
    all_guesses = []  # List to keep track of all guesses (correct and incorrect)
    terminate = False
    while wrong < 6 and not terminate:
        letter = turtle.textinput('Hangman','Guess a letter:')

        # Check if the letter has been guessed before
        while letter in all_guesses:
            turtle.goto(-135, -120)
            turtle.write(f"Letter '{letter}' already guessed! Try another.", True, font=("Courier", 12, "normal"))
            letter = turtle.textinput('Hangman', 'Guess a letter:')
        
        # Add guessed letter to the list of all guesses
        all_guesses.append(letter)
        
        turtle.goto(-135, -35)
        if letter not in correct:
            for i in word:
                if i == letter:
                    turtle.write(letter.upper() + ' ', True, font=("Courier", 12, "normal"))
                    correct += letter
                else:
                    turtle.write('_ ', True, font=("Courier", 12, "normal"))
        
        if letter not in word:
            wrong += 1
            incorrect_guesses.append(letter)  # Add incorrect guess to list
            drawMan(wrong)
            # Display incorrect guesses on screen
            turtle.goto(-135, -120)
            turtle.write(f"Incorrect guesses: {', '.join(incorrect_guesses)}", True, font=("Courier", 12, "normal"))
        
        if wrong == 6:
            turtle.goto(-135, -35)
            for i in word:
                if i in correct:
                    turtle.write('_ ', True, font=("Courier", 12, "normal"))
                else:
                    turtle.write(i.upper() + ' ', True, font=("Courier", 12, "normal"))
            turtle.goto(-74, -60)
            turtle.write('Sorry, you lose!', False, align='center', font=("Courier", 12, "normal"))
        if len(correct) == len(word):
            turtle.goto(-74, -60)
            turtle.write('Congratulations!', False, align='center', font=("Courier", 12, "normal"))
            terminate = True

    # play again?
    response = turtle.textinput('Hangman','Would you like to play again? (y or n): ')
    while response != 'y' and response != 'n':
        response = turtle.textinput('Hangman','Please enter "y" or "n": ')
    if response == 'y':
        turtle.clear()
    elif response == 'n':
        turtle.clear()
        turtle.home()
        turtle.write('Thanks for playing!', False, align='center', font=("Courier", 18, "normal"))
        bored = True
