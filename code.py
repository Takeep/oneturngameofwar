import random

#Is at 52 points
at_52_points = False 

#This is setting the amount of cards needed
list_of_cards = ['Ace of clubs', '2 of clubs', '3 of clubs', '4 of clubs', '6 of clubs', '7 of clubs', '8 of clubs', '9 of clubs', '10 of clubs', 'jack of clubs', 'queen of clubs', 'king of clubs', 'Ace of Diamonds', '2 of Diamonds', '3 of Diamonds', '4 of Diamonds', '6 of Diamonds', '7 of Diamonds', '8 of Diamonds', '9 of Diamonds', '10 of Diamonds', 'jack of Diamonds', 'queen of Diamonds', 'king of Diamonds', 'Ace of Hearts ', '2 of Hearts', '3 of Hearts', '4 of Hearts', '6 of Hearts', '7 of Hearts', '8 of Hearts', '9 of Hearts', '10 of Hearts', 'jack of Hearts', 'queen of Hearts', 'king of Hearts', 'Ace of Spades', '2 of Spades', '3 of Spades', '4 of Spades', '6 of Spades', '7 of Spades', '8 of Spades', '9 of Spades', '10 of Spades', 'jack of Spades', 'queen of Spades', 'king of Spades'  ]


#Asking if you want to play war.
play = input('Do you want to play(yes/no)')

if play == 'yes':
    print('Allright lets play')
else:

    print('Ok that is cool')
    end()

#Defining the random choice
def randomcardchoice():

    pick_random_card = random.choice(list_of_cards)

    print(pick_random_card)

    return 

def aicardchoice():

    ai_choice = random.choice(list_of_cards)

    print(ai_choice)



ask_if_draw = input('Do you want to draw(yes/no')

if ask_if_draw == 'yes':

    randomcardchoice()
    aicardchoice()

