import string
import random
import pyperclip as pc

        ####ENTER PASSWORD CHARACTER LEGNTH 
length = int(input("Enter password length: \n"
"\n"
"\n"

"16 or more is highly recommended!!-: "))

        ####LABEL OR TITLE FOR PASSWORD
        ####TO REMEMBER WHAT YOU USED IT FOR...
label = input('Enter a label for this password to be stored with...'  
"\n"
"\n")

        ####ALPHA AND NUMERIC LIBRARY 
        ####AS WELL AS SYMBOLS 
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
all = string.ascii_letters + string.digits + string.punctuation
        ####RANDOMIZE STRING
temp = random.sample(all, length)

        ####COMBINIG LENGTH INPUT W/ RANDOM STRING
password = "".join(random.sample(all, length))

        ####COPY TO CLIPBOARD SECURLEY
pc.copy(password)

        ####OPTIONAL BUT CONVENIENT
        ####APPEND TEXT FILE TO STORE PASSWORD W/ LABEL 
with open('password.txt', 'a') as f:

    f.write('\n')
    f.write(label)
    pc.paste()
    f.write(' -- ')
    f.write(password)
    f.close()
    print("Your password has been copied to the clipboard and saved to a text file in the same folder as this program. :)  ")

    exit = input("Press 'enter' to exit this program.")

    ####



