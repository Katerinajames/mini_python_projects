import sys

VOWELS = 'aeiouy'

while True:
    word = input("Type a word and get its pig latin translation: ").strip()
    
    if not word:
        print("Please type a word!")
        continue
        
    if word[0].lower() in VOWELS:
        pig_Latin = word + "way"
    else:
        
        i = 0
        while i < len(word) and word[i].lower() not in VOWELS:
            i += 1
        pig_Latin = word[i:] + word[:i] + "ay"
    
    print(pig_Latin)
    
    try_again = input("Would you like to try again? (Press Enter else n to stop)\n")
    if try_again.lower() == "n":
        sys.exit()
