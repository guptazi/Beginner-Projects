
from cryptography.fernet import Fernet




# def write_key():
#     key=Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)
# write_key()

def load_key():
    file=open("key.key",'rb')
    key = file.read()
    file.close()
    return key

imp_pwd = input("Enter your master password ")
key=load_key()
fer=Fernet(key)

def view():  
    with open('password_list.txt','r') as file:
        for line in file.readlines():
            data=line.rstrip()
            user,passwd= data.split("|")
            print("User: ",user ,"| Password: ",fer.decrypt(passwd.encode()).decode())
    
def add():
    name=input('Name : \n')
    password=input('Password :\n')
   
    with open('password_list.txt','a') as f:
        f.write(name + '|' + str(fer.encrypt(password.encode()).decode()) +'\n')

while True:

    opt=input("Do you want to add or see existing password (view,add), q for quit \n")

    if opt=='q':
        break

    elif opt=='view':
        view()

    elif opt=='add':
        add()
    
    else:
        print('Invalid Option')
        continue