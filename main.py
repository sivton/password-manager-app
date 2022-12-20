from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generatePassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    passwordList = []

    lowerLetters = [choice(letters) for char in range(randint(3, 4))]
    upperLetters = [choice(letters).upper() for char in range(randint(3, 4))]
    symbols = [choice(symbols) for char in range(randint(2, 4))]
    numbers = [choice(numbers) for char in range(randint(2, 4))]

    passwordList = lowerLetters + upperLetters + symbols + numbers
    
    shuffle(passwordList)
    
    password = "".join(passwordList)
    passwordEntry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def saveData():
    website = websiteEntry.get()
    email = emailEntry.get()
    password = passwordEntry.get()
        
    if len(website)==0 or len(email)==0 or len(password)==0:
        messagebox.showerror(title=website, message="Error! \nOne or more fields are empty!")

    else:
        isOk = messagebox.askokcancel(title=website, message=f"Details you have entered are: "
                            f"\n\nWebsite: {website}" 
                            f"\nEmail: {email}"
                            f"\nPassword: {password}"
                            f"\n\nIs this OK to save?")
    
        if isOk:
            dataFile = open("data.txt", "a")
            dataFile.write(f"{website} | {email} | {password} \n")
            dataFile.close()
            websiteEntry.delete(0, END)
            passwordEntry.delete(0, END)
        

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("MyPass - Password Manager")
window.config(padx=100, pady=50)

# Canvas
canvas = Canvas(height=200, width=200)
logoImg = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logoImg)
canvas.grid(column=1, row=0)



# Labels
websiteLabel = Label(text="Website")
websiteLabel.grid(column=0, row=1)

emailLabel = Label(text="Email/Username")
emailLabel.grid(column=0, row=2)

passwordLabel = Label(text="Password")
passwordLabel.grid(column=0, row=3)




# Entries
websiteEntry = Entry(width=35)
websiteEntry.grid(column=1, row=1, columnspan=2)
websiteEntry.focus()

emailEntry = Entry(width=35)
emailEntry.grid(column=1, row=2, columnspan=2)
emailEntry.insert(END, "@gmail.com")

passwordEntry = Entry(width=19)
passwordEntry.grid(column=1, row=3)



# Buttons
generatePasswordBtn = Button(text="Generate Password", command=generatePassword)
generatePasswordBtn.grid(column=2, row=3)

addBtn = Button(text="Add", width=36, command=saveData)
addBtn.grid(column=1, row=4, columnspan=2)



window.mainloop()