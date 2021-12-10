import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    for j in secret_word:
        if j in letters_guessed:
            return True
    return False

def get_guessed_word(secret_word, letters_guessed):
    secret_word_check =""
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for j in secret_word:

        if j in letters_guessed:
            secret_word_check+=j

        else:
            secret_word_check += "_ "

    return secret_word_check

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_not_guessed = ""
    for j  in string.ascii_lowercase:

        if j  not in letters_guessed:
            letters_not_guessed += j
    return letters_not_guessed


secret_word= choose_word(wordlist)
secret_word ="abc"
letters_guessed_empty= []
for char in secret_word:
    letters_guessed =input("Please enter your guess word :> ")
    letters_guessed_empty += letters_guessed

print("secret word is :" + secret_word)
print(">>letter guessed is :" +str(letters_guessed_empty))
print(is_word_guessed(secret_word,letters_guessed))
print(get_guessed_word(secret_word, letters_guessed_empty))
print(get_available_letters(letters_guessed_empty))

