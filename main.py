from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def saveData():
    dataFile = open("data.txt", "a")
    dataFile.write(f"{websiteEntry.get()} | {emailEntry.get()} | {passwordEntry.get()} \n")
    dataFile.close()
    websiteEntry.delete(0, END)
    emailEntry.delete(0, END)
    passwordEntry.delete(0, END)
        

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
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
generatePasswordBtn = Button(text="Generate Password")
generatePasswordBtn.grid(column=2, row=3)

addBtn = Button(text="Add", width=36, command=saveData)
addBtn.grid(column=1, row=4, columnspan=2)



window.mainloop()