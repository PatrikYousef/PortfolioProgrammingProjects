import random

def passwordsystem():
    letters = "abcdefghijklmnopqrstuvwxyz".upper()
    newpassword = ""

    for i in range(10):
        newpassword += random.choice(letters)
    
    print("Generated password:", newpassword)

passwordsystem()

