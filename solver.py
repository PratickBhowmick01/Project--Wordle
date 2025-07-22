import random 

# Designing an algo to solve wordle.
def wordle(wordList): 
    grey, yellow, green = [], [], []   
    count = {}    

    for i in range(6):
        # Selecting suggestion.
        if i == 0:
            word = "SPARE"
        else:
            word = random.choice(wordList)

        print("Suggested word:", word)
        print("Enter your word:", end = " ")
        while True:
            word = input().upper()
            if len(word) != 5:
                print("Please enter a 5 letter word:",end = " ")
            else:
                break

        # Obtain results. 
        print("Please enter the results: [X-> grey, Y-> Yellow, G-> Green]")
        while True:  
            res = input().upper()
            print()
            if len(res) != 5:
                print("Please enter the results correctly: [X-> grey, Y-> Yellow, G-> Green]")
            else:
                break

        if res == "GGGGG":
            print("*****************************************")
            print("Hurray!!")
            print("You Have Solved The Wordle!!")
            print("*****************************************")
            break

        temp = {}
        for i in range(5):
            if res[i] == "X" and word[i] not in grey and word[i] not in green:
                grey.append(word[i])

            elif res[i] == "Y" and [word[i],i] not in yellow:
                yellow.append([word[i],i])
            
            elif res[i] == "G" and [word[i],i] not in green:
                green.append([word[i], i])

            if word[i] in temp:
                temp[word[i]].append(res[i])
            else:
                temp[word[i]] = [res[i]]

        for key, value in temp.items():
            if len(value) > 1 and "X" in value:
                dup = value.count("X") 
                count[key] = len(value) - dup 

        # print(grey, yellow, green)
        
        for l,ind in green+yellow:
            if l in grey:
                grey.remove(l)
        

        # Remove incorrect words. 
        tempList = []
        for w in wordList:
            flag = True 
            for letters in grey:
                if letters in w:
                    flag = False
                    break  
            
            if flag == False: 
                continue 

            for letters, ind in yellow:
                if letters not in w or w[ind] == letters:
                    flag = False 
                    break 
            
            if flag == False: 
                continue 

            for letters, ind in green:
                if letters not in w or w[ind] != letters:
                    flag = False 
                    break 

            if flag == False:
                continue

            for key, value in count.items():
                if key in w:
                    if w.count(key) != value:
                        flag = False
                        break
            
            if flag:
                tempList.append(w)

        wordList = tempList.copy()


# Importing the text file -> Storing in a list.  
fr = open("Modern word list.txt", "r")
#All valid 5 letter words
wordList = []
for elem in fr:
    elem = elem.upper()
    wordList.append(elem[:5])   

print("*****************************************")
print("Welcome!")
print("We shall guide you in your conquest!")
print("*****************************************")
print()
wordle(wordList)

fr.close()
