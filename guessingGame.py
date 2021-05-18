import random
number = random.randint(1, 9)
print("Number Guessing Game")
print("Guess a number between 1-9")
guess = input("Enter the number: ")
chances = 5

while chances > 0:
    if (guess  == number & chances > 0):
        print("Congratulations YOU WON!!!!!!!")    
        break    
    if(guess != number):
        print("Try Again") 
        break
    elif chances == 0:
        print("You Lose!! The number is " , number)    
        
    
    
    
