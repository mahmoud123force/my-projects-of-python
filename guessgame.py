print("welcome to guess nuber game")
import random
print("1]start game")
print("2]exit game")
choice=int(input("enter your choice:"))
if choice==1:
    print("welcome to guess nuber game")
while True:
    number=random.randint(1,100)
    guess=int(input("guess a number between 1 and 100:"))
    if guess==number:
        print("congratulation! you guessed the number correctly.")
        break
    elif guess<number:
        print("<")
    elif guess>number:
        print(">")
    
    elif choice==2 : break
    else:
        print("invalid choice, please try again.")
        choice=int(input("enter your choice:")) 