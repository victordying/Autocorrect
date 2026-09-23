
#this is going to be my spell checker!!! made in python
#i just downloaded a word bank from github and turned the text file
#into a set

import sys


print("Hello, World.")

try:
    print("\nOpening file...")
    file = open("WordList.txt")
    print("File opened...\n")
except:
    sys.exit("Error: Failed to open file")

word_set = set()


print("Reading lines...")

for line in file:
    word_set.add(line.strip().lower())

print("\"word_set\" ready...\n")


try:
    print("Closing file...")
    file.close()
    print("File closed...")
except:
    sys.exit("Error: Failed to close file")


#everything works !! bet bet bet



def generate_candidates(word): #GENERATING CANDIDATE WORDS!!

    candidate_word_set = set() #just making an empty set to add the candidate words

    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    #OKAY so now that i know it works, im gonna start going down the list and test the deletions, insertions, etc.


    #DELETIONS: 
    for i in range(len(word)): 
        candidate_word_set.add(word[:i] + word[i+1:])

    #INSERTIONS: 
    for i in range(len(word)+1): 
        for letter in alphabet:
            candidate_word_set.add(word[:i] + letter + word[i:])

    #REPLACEMENTS: 
    for i in range(len(word)):
        for letter in alphabet:
            candidate_word_set.add(word[:i] + letter + word [i+1:])

    #SWAPS
    for i in range(len(word)-1):
        candidate_word_set.add(word[:i] + word[i+1] + word[i] + word[i+2:])


    return candidate_word_set #RETURN CANDIDATES



def is_valid(x):
    #x<1 characters
    if len(x) < 1:
        print("Input is too short bruh. (1 minimum)")
        return False

    #x>30 characters
    if len(x) > 30:
        print("Input is too long bruhh. (30 max)")
        return False

    #alphabetic
    if x.isalpha() == False:
        print("Input must be alphabetic. (letters only bruh)")
        return False

    #word must not be in set
    if x in word_set:
        print("Input is a valid word, silly")
        return False

    return True



#Output SECTION! - - - - - - - - - - - - - - - - - 

#user input but its a string and i strip it of spaces and lowercase it
x = str(input("\nInput Word to Spell Check: ").strip().lower())

#loop input if its not valid (error handling :p)
while is_valid(x) == False:
    x = str(input("\nUse an actual word bruh: ").strip().lower())

#copy the set into the candidates value
candidates = generate_candidates(x)
#copy the words from the word set that match vandidates into the value
valid_candidates = {x for x in candidates if x in word_set}


print(f'\ncandidates: {candidates}')
print(f'\nvalid_candidates: {valid_candidates}')

