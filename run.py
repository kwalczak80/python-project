import random
import sys

#player name
player_name =""

#number of tries
number_of_tries = 5

#list of words
list_of_words = ["code", "institute", "python", "java", "programming"]

#list of letters used by the user
used_letters = []

#randomly select word from list of words
word = str(list_of_words[random.randint(0, len(list_of_words) - 1)])
table = list(word)

#display table with _ based on word length
for i in range(len(word)):
    table[i] = "_"
    
def get_player_name():
    """
    Display game name and get name from player
    """
    print("\033[1;32;40m************************")
    print("************************")
    print("\033[1;32;40m Guess the word to win!")
    print("\033[1;32;40m************************")
    print("************************\n")

    while True:
        # Name accepts all characters to allow users to get creative
        player_name = input("\033[0;36mPlease enter your name: ").strip()

        if validate_player_name_input(player_name):
            print(f"Welcome {player_name} \n")
            break

def validate_player_name_input(player_name):
    """
    Validates player input for name.
    Player name cannot be blank or longer that 20 characaters
    """
    # name cannot be blank or longer that 20 characters
    try:
        if player_name == "":
            raise ValueError("\033[1;40mPlayer name cannot be blank !!\n")
        elif (len(player_name) > 20):
            raise ValueError("\033[1;31mPlayer name is too long - max 20 characters !! \n")

    except ValueError as error:
        print(f"\033[1;31mTry again. {error}")
        return False
    return True

def update_game_status():
    print()
    print("You have", number_of_tries, "tries to finish the game")
    print()
    print(" ".join(table))
    print()

get_player_name()

while number_of_tries > 0:
    update_game_status()
    print("Used letters : ", used_letters)
    print("PLease enter the letter: ")
    letter = input()
    used_letters.append(letter)
    #check if letter is in word
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
               table[i] = letter
    else:
        number_of_tries -=1
    if "".join(map(str, table)) == word:
        print()
        print("Fantastic !! You have guessed the word")
        sys.exit(0)
    elif number_of_tries == 0:
        print()
        print("Sorry you lost !!")
        sys.exit(0)   
