import random

# Function to get a random 5 lettered word
def returnWord():
    with open("words.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))

        return random.choice(words)


def game():
    attempt = 1
    word = returnWord()
    print(word)
    print(f"Attempt {attempt}")
    
    

    while attempt <=5:
        
        inputWord = input("Enter Word: ")
        if len(inputWord) != 5:
            print("Please enter a 5 lettered word only")
        elif inputWord == word:
            print("You won!")
        elif attempt > 5:
            print("You Lost")
            break
        else:
            print("Try Again")
            print(f"Attempt {attempt}")
            attempt += 1


print("Welome to Wordle!")
print("You must guess a 5 letter word in 6 attempts or less!")
game()
