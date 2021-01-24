import random, os, time 
from os import system, name 
from time import sleep

#ALL THE FUNCTIONS -->
def logo(): #Logo function
    print('###########################\n#    PASSWORD GENERATOR   #\n###########################\n')

def clear(): #Clear function
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def passwordgen(): #Password Generator
    chars = "abcdefghijklmnopqrstuvwxyz123456789#$&.<>"
    while True:
        logo()
        output_file = open('output.txt', 'a')
        name = input('Site / Username : ')
        length = int(input('\nLength of the password : '))
        clear()
        logo()
        password = ''
        for i in range(length):
            password += random.choice(chars)
        print("Password for "+ name +" = "+ password)
        answer = input('\n[Y = Save N = Try again]')
        if answer == 'Y' or answer == 'y':
            print("\nPassword has been saved.")
            output_file.write("\nPassword for "+ name +" = "+ password+'\n')
            output_file.close
            time.sleep(1)
            break
        elif answer == 'N' or answer == 'n':
            print('Trying again.')
            time.sleep(0.5)
            clear()

clear()
passwordgen()

