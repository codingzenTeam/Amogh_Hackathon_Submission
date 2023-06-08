# caclulator
import os
import random

os.system("cls")
os.system("color a")
os.system("title The OG Calculator")


def regame():
    h = str(random.randrange(1, 10))
    x = "color " + h
    os.system(x)
    print("\nWanna to use it again???\n")
    i = input("Pls enter a 'Yes' to start new game\n \tor Just press enter\n")
    if (
        i == "Yes"
        or i == "YES"
        or i == "yes"
        or i == "YeS"
        or i == "yEs"
        or i == "YEs"
        or i == "yES"
        or i == "yeS"
    ):
        os.system("cls")
        gamestart()


def divide():
    y = int(input("Pls enter a number"))
    x = int(input("Pls enter a number"))
    os.system("cls")
    print("Divided number is = ", x // y)
    regame()


def multiply():
    a = int(input("Pls enter a number(Bigger One)"))
    b = int(input("Pls enter a number(Smaller one)"))
    os.system("cls")
    print("Product is = ", a * b)
    regame()


def sum():
    c = int(input("Pls enter a number(Bigger One)"))
    d = int(input("Pls enter a number(Smaller one)"))
    os.system("cls")
    print("Sum is = ", c + d)
    regame()


def Minus():
    e = int(input("Pls enter a number(Bigger One)"))
    f = int(input("Pls enter a number(Smaller one)"))
    os.system("cls")
    print("Ans is = ", e - f)
    regame()


def all():
    k = int(input("Pls enter a number(Bigger One)"))
    l = int(input("Pls enter a number(Smaller one)"))
    os.system("cls")
    print("Minus is = ", k - l)
    print("Sum is = ", k + l)
    print("Product is = ", k * l)
    print("Divided number is = ", k // l)

    regame()


def complex():
    n = input("Pls enter the complex equation carefully\n")
    os.system("cls")
    print("THe ans to this COMPLEX eqaution is ", eval(n))
    regame()


def gamestart():
    print("What are u gonna do today \n")
    print("1.Sum\n")
    print("2.Multiply\n")
    print("3.Divide\n")
    print("4.minus\n")
    print("5.all\n")
    print("6.complex\n")

    z = input("\nType the process u want to do today in lower caps\n")
    if z == "sum":
        sum()
    elif z == "minus":
        Minus()
    elif z == "divide":
        divide()
    elif z == "multiply":
        multiply()
    elif z == "all":
        all()
    elif z == "complex":
        complex()


print("\t\t\t\t\t\t Weclome To the Calculator\n\n")
g = input("PLs enter the secrect password: ")
if g == "Aditya":
    gamestart()

input()
