import random
print('H A N G M A N')

my_words = []
f = ['python', 'java', 'kotlin', 'javascript']  # Importing the word collection text file
for x in f:
    word = str(x)
    word = word.rstrip("\n")  # Removine'\n' character from the word
    if (len(word) > 2):  # We take the word which have more than 2 characters
        my_words.append(word)



def pick(my_words):  # This function will pick random one word
    rand_word = random.sample(my_words, 1)
    rand_word = str(rand_word[0]).upper()  # creating the word into uppercase
    return (rand_word)


def initial(rand_word):  # This function will return '_' characters according to the selected word length
    sent = ''
    for i in range(len(rand_word)):
        sent += '_'
    return (sent)


def usr_inp(get, word):  # This function for taking the user input letter
    for i in get:
        print(i, end=' ')
    inp = input('\nInput a letter: ')
    inp = str(inp).upper()
    if (len(inp) > 1 or inp == ''):
        return (get)
    else:
        res = match(inp, get, word)  # Calling the match function for checking the user input
        return (res)


def match(inp, get, word):  # This is the original function which will check if the user input right or wrong
    getl = list(get)
    for i in range(len(word)):
        if inp == word[i]:
            getl[i] = inp
    gts = ''
    for x in getl:
        gts += x
    return (gts)


def play(get, word):  # This function is the main game Function
    var = 0
    max_limit = 8
    while True:

        if (var >= max_limit):  # Checking the wrong chances reach the max limit
            print('')
            print('Your Maximum Wrong Guesses Is Exceed !')
            print('You Lose !')
            print("Thanks for playing!")
            print("We'll see how well you did in the next stage")
            print('')
            #print('Word is : ', word)
            break

        #print("Your Wrong Guesses left :", (max_limit - var))
        ans = usr_inp(get, word)
        if (ans == get):
            var += 1
            print('No such letter in the word')
            print('')

        else:
            get = ans
            print('')

        if (ans.count('_') == 0):  # Checking if any '_' left or not
            print('')
            print('Congrats! You Win')
            print('')
            print("Thanks for playing!")
            print("We'll see how well you did in the next stage")
            #print('The Word Is : ', ans)
            break


word = pick(my_words)  # Picking a randomword
get = initial(word)  # Getting the empty structure
play(get, word)  # Call the game