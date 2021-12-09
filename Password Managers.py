#Organize and store managers
#store password in text file but with encryption.
#advanced
#define a function to call it whenever needed.
#Pipe operator to get the strings in between "|"
#encrypt passwords, using manual encryption algorithm or modules created by others.
#currently using module
#.bytes()=.encode()
#master_pwd= input("What is the Master Password ? ")
#key + password used to encrypt.
#key is required to decrypt
#key + pasword + text to encrypt = random text
#function to create a key
#function to store a key
#wb is write in bytes
#''' ''' commented out to not use the function again
#to view th apssword stored in a file by using the defined function
#now we have read and closed they key
#create a new file for if new file doesn't exist.
#with open('passwords.txt', 'a') as f for using indented after file closed separately if not using "with"
#"w" for overwriting, "a" mode to add end of exisiteng file and create if a new file doesnot exist, "r"  mode read a file
#print(line.rstrip())

from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

key= load_key()

fer = Fernet(key)


def view():

    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password: ", fer.decrypt(passw.encode()).decode())

def add():

    name = input('Account Name: ')
    pwd = input("Password: ")


    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode().decode()) + "\n")

        
while True:
    mode= input("Would you like to add a new password or view existing one's?.(view/add). Press 'Q' to Quit. ").lower()

    if mode == "q":
        break
    
    if mode =="view":
        view()
        
    elif mode == "add":
        add()
        
    else:
        print("Invalid Mode")
        continue



