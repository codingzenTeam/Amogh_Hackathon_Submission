# Guessing Game Name = Amogh Sharma Class:10
import os
import random


os.system("color a")
os.system("cls")
print("\t\t\t\t\tWelcome To my guessing game:)")
z = input("\t\t\t\t -->Pls enter a 'Yes' to start the game\n")
a = False


def game():
    os.system("color a")
    Number = random.randint(1, 101)
    for x in range(11):
        guess = int(input("-->Enter your guess "))

        if guess > Number:
            print("-->Too High it is", guess - Number, "Higher\n")
            os.system("color 1")

        elif guess < Number:
            print("-->Too Low it is ", Number - guess, "lower\n")
            os.system("color 0")

        elif guess == Number:
            print("-->Hurray! right guess entered", guess, "\n")
            a = True
            regame()
            break

        if x == 3:
            print("-->>Game Over")
            regame()


def regame():
    print("-->Wanna Play again???\n")
    k = input("-->Pls enter a 'Yes' to start new game\n or Just press enter\n")
    if k == "Yes":
        game()
    else:
        print("-->Pls press 'enter' again to End the game")


if z == "Yes":
    game()


input()
