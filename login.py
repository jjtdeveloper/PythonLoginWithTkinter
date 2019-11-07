import tkinter as tk
import json
import encrypt_mod     # My own module that encrypts the passwords

HEIGHT = 700   # Height and Width of Tkinter Window
WIDTH = 800  

user_info_f = 'data/user_info'

def file_setup(): # This will set up the saved info file, if the file already exists then it will load it and save it while the program runs
    global user_info_f
    try:
        with open(user_info_f, 'r') as user_info_j:
            user_info = json.load(user_info_j)    
            user_info_j.close()
    except FileNotFoundError:
        with open(user_info_f, 'w') as user_info_j:
            user_info = {}
            json.dump(user_info, user_info_j)
            user_info_j.close()
    return user_info

def check_login():
    user_info = file_setup()
    entered_username = (username.get()).lower()          # Gets username and password entered by the user
    entered_password = password.get()
    total_pw_length = len(entered_password)          # Saves the length of password that was entered in order to delete it later if it is wrong
    try:
        saved_password = user_info[entered_username]     # Checks if a password can be found using the username, if it works then the user was found
        print("User Found")

        code_1 = saved_password[0]
        code_2 = saved_password[5]

        entered_password = encrypt_mod.encrypt(entered_password, code_1, code_2)       # Encrypts the entered password the same as the already saved password

        if entered_password == saved_password:
            print("Correct password")
            message_label.config(text="Correct Password", fg='white')
            window = tk.Toplevel(root) # Creates an empty window once a successful log-in is completed, it can be taken farther from here
        else:
            print("Incorrect password")
            message_label.config(text="Username or password is Incorrect", fg='red')
            password.delete(first=0, last=total_pw_length)   # This deletes entered password from the entry field
    
    except KeyError:
        print("User Not Found")
        message_label.config(text="Username or password is Incorrect", fg='red')
        password.delete(first=0, last=total_pw_length)       # This deletes entered password from the entry field
    
def new_account():
    global user_info_f                             # Yes I know global variable = bad but this was the simplest way
    user_info = file_setup()
    entered_username = (username.get()).lower()    # gets the username and password entered
    entered_password = (password.get()).lower()

    entered_password = encrypt_mod.encrypt(entered_password) # Encrypts Password to be saved

    user_info[entered_username] = entered_password
    with open(user_info_f, 'w') as user_info_j:              # Saves the user info into the json file
            json.dump(user_info, user_info_j)
            print("New Account Created")
            user_info_j.close()

root = tk.Tk()

#-------------------------------------Set-Up------------------------------------------
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='grey')
frame.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.8)

#-----------------------------------Text-Lables----------------------------------------
username_label = tk.Label(frame, text="Username:", bg="grey", fg="white", font=("Ariel", 15))
username_label.place(relx=0.1, rely=0.1, relwidth=0.25, relheight=0.05)

password_label = tk.Label(frame, text="Password:", bg="grey", fg="white", font=("Ariel", 15))
password_label.place(relx=0.1, rely=0.3, relwidth=0.25, relheight=0.05)

message_label = tk.Label(frame, text="Enter Password", bg="grey", fg="white", font=("Ariel", 10))
message_label.place(relx=0.1, rely=0.5)

#-----------------------------------Entry-boxes----------------------------------------
username = tk.Entry(frame)
username.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.05)

bullet = "\u2022" # The key for the password bullets
password = tk.Entry(frame, show=bullet, width=15)
password.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.05)

#-------------------------------------Buttons------------------------------------------
new_account_button = tk.Button(
    frame, text='Create New Account', command=new_account)
new_account_button.place(relx=0.1, rely=0.8, relwidth=0.3, relheight=0.05)

login_button = tk.Button(frame, text='Login', command=check_login)
login_button.place(relx=0.7, rely=0.8, relwidth=0.2, relheight=0.05)

tk.mainloop()
