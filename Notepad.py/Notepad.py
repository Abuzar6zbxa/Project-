# from tkinter import *
# from tkinter import filedialog
#
# root = Tk()
# root.title('Notepad')
# root.geometry('500x500')
#
#
# def clear():
#     entry_box.delete(1.0, 'end')
#
#
# def save_file():
#     data = entry_box.get("1.0", 'end')
#     file = filedialog.asksaveasfile(mode='w', defaultextension=".txt", filetypes=[('text files', '*.txt')])
#     if file is not None:
#         file.write(data)
#
#
# def open_file():
#     file = filedialog.askopenfile(mode='r', filetypes=[('text files', '*.txt')])
#     if file is not None:
#         data = file.read()
#         entry_box.delete(1.0, 'end')
#         entry_box.insert(INSERT, data)
#
#
# lbl = Label(root, text='Notepad', font=('Arial', 20))
# lbl.place(x=170, y=0)
#
# clear_btn = Button(root, text='Clear', width=20, command=clear)
# clear_btn.place(x=10, y=40)
#
# save_btn = Button(root, text='Save File', width=20, command=save_file)
# save_btn.place(x=170, y=40)
#
# open_btn = Button(root, text='Open File', width=20, command=open_file)
# open_btn.place(x=330, y=40)
#
# entry_box = Text(root, height=25, width=60)
# entry_box.place(x=10, y=80)
#
# mainloop()











#######           mind reading          #################################

import random
import tkinter as tk
from tkinter import messagebox

def mind_reader():
    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)

    # Ask the user to guess the number
    def ask_guess():
        guess = int(entry.get())

        if guess == secret_number:
            messagebox.showinfo("Mind-Reading Game", "Congratulations! You guessed the correct number!")
        elif guess < secret_number:
            messagebox.showinfo("Mind-Reading Game", "Your guess is too low. Try again.")
        else:
            messagebox.showinfo("Mind-Reading Game", "Your guess is too high. Try again.")

    # Create a pop-up window
    window = tk.Tk()
    window.title("Mind-Reading Game")
    window.geometry("300x100")

    # Add a label and an entry field to the window
    label = tk.Label(window, text="I'm thinking of a number between 1 and 10. Can you guess what it is?")
    label.pack()

    entry = tk.Entry(window)
    entry.pack()

    # Add a button to the window that triggers the guess function
    button = tk.Button(window, text="Guess", command=ask_guess)
    button.pack()

    # Run the pop-up window
    window.mainloop()

# Call the mind-reading game function
mind_reader()