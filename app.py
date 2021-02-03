import tkinter as tk
from tkinter import scrolledtext, Frame, Entry
from tkinter.scrolledtext import ScrolledText

codeFile = open('geneticCodes.txt', 'a+')


# Stores genetic codes
def retrieve():
    codeFile.write(genEntry.get() + '\n')


root = tk.Tk()
root.wm_title("Rust Genetics Calculator")
root.geometry("600x450+700+200")

# create all main containers
topLeftFrame = Frame(root, bg="#d0d9d2", width=300, height=150)
botLeftFrame = Frame(root, bg="#b8c2ba", width=300, height=200)
topRightFrame = Frame(root, bg="#a0a8a2", width=300, height=80)
botRightFrame = Frame(root, bg="#888f89", width=300, height=100)

# layout the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

topLeftFrame.grid(row=0, column=0, sticky="news")
botLeftFrame.grid(row=1, column=0, sticky="news")
topRightFrame.grid(row=0, column=1, sticky="news")
botRightFrame.grid(row=1, column=1, sticky="news")

# top left frame input and button
genEntry = Entry(topLeftFrame, width=30)
submitGen = tk.Button(topLeftFrame, text='Add crop', command=retrieve, padx=10, pady=5, fg='white', bg='gray')

genEntry.grid(row=0, column=0, padx=(30, 10), pady=(20, 10))
submitGen.grid(row=0, column=1, padx=(0, 20), pady=(10, 0))

codeFile.close()
root.mainloop()
