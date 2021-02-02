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

genEntry = scrolledtext.ScrolledText(canvas, width=40)
# genEntry = Entry(frame, width=30)
genEntry.pack(padx=5, pady=5)

submitGen = tk.Button(canvas, text='Calculate', command=retrieve, padx=10, pady=5, fg='white', bg='gray')
submitGen.pack()


root.mainloop()
codeFile.close()
