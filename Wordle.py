#Attempt to create a wordle game 
import random
import string
#test function 
def test(word, guess, alpha,arr, tempList):
    for i in range(5):
        char1, char2 = word[i], guess[i]
        print(char2, "-", sep = "", end = "")
        #correct letter, correct position
        if char1 == char2: 
            print("🟩")
            if char2 not in tempList:
                tempList.append(char2)
            arr[i] = char2
        #letter absent
        elif(char2 not in word):
            print("⬛")
            try:
                alpha.remove(char2)
            except ValueError:
                pass 
        #letter present in word
        else:
            #counting no. of times letter present 
            w_cnt = 0
            for elem in word:
                if elem == char2:
                    w_cnt += 1 
            #counting no. of times letter present in guess previously
            g_cnt = 0
            for elem in guess[:i]:
                if elem == char2:
                    g_cnt += 1
            if w_cnt - g_cnt > 0:                
                print("🟨")
            else:
                print("⬛")
            #letter in our tempList
            if char2 not in tempList: 
                tempList.append(char2)
    #Printing correct letters
    print("Correct letters-", tempList)
    #Printing the progress
    print("Progress-",arr)
    #Printing available letters
    print("Available letters-", end = " ")
    for char in alpha:
        print(char, end = "")
    print()

#Starting the game
def wordle(word): 
    #List of all alphabets
    alphabet_string = string.ascii_uppercase
    alpha_list = list(alphabet_string) 
    #List displaying correct positions
    arr = ["_","_","_","_","_"]
    tempList = []
    #6 guesses from user
    count = 6
    i = 1
    while(i <= 6):
        print("Guesses Left:", count)
        if i == 1:
            guess = input("Please Enter Your Guess: ")
        else:
            guess = input("Please Enter Your Next Guess: ")
        
        if len(guess) != 5:
            print("Please enter a valid 5 letter word.") 
            i -= 1
            continue 
        
        guess = guess.upper()
        #insert a check function here
        test(word, guess, alpha_list,arr,tempList) 
        count -= 1
        
        if(word == guess):
            print()
            print("*****************************************")
            print("Hurray!!")
            print("The Word Was " , word, "!", sep = "")
            print("You Have Solved The Wordle!!")
            print("*****************************************")
            return 
        i+=1
    
    print("*****************************************")
    print("The Word Was ", word, "!", sep = "")
    print("Better Luck Next Time.")
    print("*****************************************")
    return 

if __name__ == '__main__': 
    #alphabet_string = string.ascii_lowercase
    alphabet_string = string.ascii_lowercase
    alphabet_string = alphabet_string.upper()
    f = open("Modern word list.txt", "r")
    #All valid 5 letter words
    wordList = []
    for elem in f:
        elem = elem.upper()
        wordList.append(elem[:5])   
    #Word of the round
    word = random.choice(wordList) 
    print("*****************************************")
    print("Welcome!")
    print("*****************************************")
    wordle(word)
    
    f.close()