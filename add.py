from os import system, name
from time import sleep

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


print("whats the first number you wanna add?")
input1 = int(input(""))
print("whats the second number you wanna add?")
input2 = int(input(""))
answer = input1 + input2
print("Your answer is", answer)
while True:
    print("press e to clear console and exit")
    exit = str(input(""))
    exte = "e"
    if exit == exte:
        print("clearing console in 2 seconds")
        break

    if exit != exte:
        print("Invalid command, Try Again")
sleep(2)
clear()
