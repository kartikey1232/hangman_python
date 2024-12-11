stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel","candle","noodle","tree","bug"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.
import random
chosen_word=random.choice(word_list)
space=[]
visited=[]
for i in range(len(chosen_word)):
    space.append(" _ ")
    visited.append(0)
def print_space():
    for items in space:
        print(items, end=" ")
    print("\n")
def indexOf(letter):
    for j in range(len(chosen_word)):
        if chosen_word[j]==letter and visited[j]==0:
            visited[j]=1
            return j
    return -1
print_space()
guess=input("Guess the first letter of the word.\n").lower()
correct_counter=len(chosen_word)
lives=6
def modify_space(letter):
    pos=indexOf(letter)
    if pos==-1:
        print("You have already guessed the word")
        return -1
    else:
        space[pos]=letter
while lives >0 and correct_counter > 0:
    if guess in chosen_word:
        print("That was a correct guess")
        check=modify_space(guess)
        if check != -1:
            correct_counter-=1
        if correct_counter==0:
            break
        print_space()
        guess = input("Guess the another letter.\n").lower()
    else:
        print("Wrong guess!")
        lives-=1
        print(stages[lives])
        print(f"lives left: {lives}")
        if lives ==0 :
            break
        print_space()
        guess = input("Guess the another letter.\n").lower()

if lives > 0:
    print("You won")
else:
    print("You lost")


