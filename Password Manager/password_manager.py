from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key) '''



def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key


master_pwd = input("What is the master password? ")

key = load_key() + master_pwd.encode()
fer = Fernet(key)

# key + password + text to encrypt = random text
# random text + key + pasword = text to encrypt


def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            if "|" in data:
                user, passw = data.split("|", 1)

            print("User:", user, "| Password:", fer.decrypt(passw.encode()))


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n") 

while True:
    mode = input("Would you like to add a new password or view existing one (view, add), press q to quit?  ").lower()
 
    if mode == "q":
        quit()
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue


