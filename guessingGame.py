import random
number = random.randint(1, 9)
print("Number Guessing Game")
print("Guess a number between 1-9")
guess = int(input("Enter the number: "))
chances = 0

while chances < 5:
    if guess  == number :
        print("Congratulations YOU WON!!!!!!!")    
        break    
    elif guess > number:
        print("Try Again.The number is too big")         
    else:
        print("Try again.The number is too small")

    chances = chances + 1

if chances == 5:
    print("You Lose!! The number is " , number)     
        
    
    
    
