from cryptography.fernet import Fernet #module 
import os


"""def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)"""
        
# write_key()

def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key

f = open('master_password_file.txt','a')
f.close()
if os.stat('master_password_file.txt').st_size == 0:
    f = open('master_password_file.txt','a')
    print('master file is empty')
    master_pwd = input('please input a master password: ')
    f.write(master_pwd)
    print('please remember your master password for next time. master password =', master_pwd)
    f.close()
else:
    f = open('master_password_file.txt','r')
    master_pwd = input('What is the master password: ')
    if f.read() == master_pwd:
        print('access granted')
        
    else:
        print('your master password is wrong, access not granted')
        question = input('do you want to re try or reset the master password? (re try or reset): ').lower()
        if question =='reset':
            open('master_password_file.txt', 'w').close()
            new_master_pwd = input('password has been cleared. please enter your new master password: ')
            with open("master_password_file.txt", 'a') as f:
                f.write(new_master_pwd)
            print('your new master password has been set to: ',new_master_pwd)
        elif question == 're try':
            master_pwd = input('What is the master password: ')
            with open("master_password_file.txt", 'r') as f:
                if f.read() == master_pwd:
                    print('access granted')
                else: 
                    ask_again = input('either quit by entering q or reset password: type (q or reset): ').lower()
                    if ask_again == 'q':
                        quit()
                    elif ask_again == 'reset':
                        open('master_password_file.txt', 'w').close()
                        new_master_pwd2 = input('password has been cleared. please enter your new master password: ')
                        with open("master_password_file.txt", 'a') as f:
                            f.write(new_master_pwd2)
                        print('your new master password has been set to: ',new_master_pwd2)
                    else:
                        print('invalid option, now quitting, goodbye')
                        quit()
                        
        else:
            print('invalid entry, goodbye')
        
        quit()
    f.close()



key = load_key() + master_pwd.encode() 
fer = Fernet(key)
#save master password into a file
#


def view():
    # print('your account name is', name)
    with open("passwords.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print('Username:',user,'| Password:', fer.decrypt(passw.encode()).decode())

def add():
    name = input('Account Name: ')
    pwd = input('Password: ')
    
    with open("passwords.txt", 'a') as f: #'with' command auto closes after opening and using
        #'w' means write (create a new file or override the file)
        #'r' means just read, can't write
        #'a' append to the file, create a new file if the file does not exist
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
        

while True:
    mode = input('would you like to add a new password or view existing ones (view, add)? or press q to quit: ').lower()
    
    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    elif mode == 'q':
        quit()
    else:
        print('invalid entry')
        continue