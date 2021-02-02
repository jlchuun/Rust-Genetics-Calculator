import tkinter as tk
from tkinter import Entry, scrolledtext
from tkinter.scrolledtext import ScrolledText

codeFile = open('geneticCodes.txt', 'a+')


# Stores genetic codes
def retrieve():
    codeFile.write(genEntry.get() + '\n')


root = tk.Tk()

canvas = tk.Canvas(root, height=700, width=700)
canvas.pack()

frame = tk.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

genEntry = scrolledtext.ScrolledText(frame, width=40)
# genEntry = Entry(frame, width=30)
genEntry.pack(padx=5, pady=5)

submitGen = tk.Button(frame, text='Calculate', command=retrieve, padx=10, pady=5, fg='white', bg='gray')
submitGen.pack()


root.mainloop()
codeFile.close()
